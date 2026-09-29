"""Offline tests for the public reference: the examples and the docs that describe them.

No test here contacts TAMO. The transport is always mocked.
"""

import contextlib
from datetime import date
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import _client as client_module
import calendar_week
import homework
import login

DOCS = Path(__file__).resolve().parents[1] / "docs"

SUCCESS = {
    "Status": 1,
    "ErrorCode": 0,
    "Result": {
        "authToken": "token-value",
        "userRoleIsAllowed": True,
        "personId": 7,
        "role": 2,
    },
}


def payload(**keys):
    body = {"isSuccess": True}
    body.update(keys)
    return body


class FakeResponse:
    def __init__(self, body):
        self._raw = json.dumps(body).encode("utf-8")

    def read(self, limit=None):
        return self._raw

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class RecordingOpener:
    """Stands in for the client's opener and records every request made."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def open(self, request, timeout=None):
        self.requests.append(request)
        if not self.responses:
            raise AssertionError("The example made more requests than expected.")
        return FakeResponse(self.responses.pop(0))


def run_example(module, argv, responses):
    """Run an example's main() with hidden input and the transport mocked."""
    opener = RecordingOpener(responses)
    stdout, stderr = io.StringIO(), io.StringIO()
    with patch.object(client_module.urllib.request, "build_opener", Mock(return_value=opener)), \
            patch.object(sys, "argv", [module.__name__] + argv), \
            patch.object(client_module.getpass, "getpass", Mock(side_effect=["user", "pw"])), \
            contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        code = module.main()
    return code, stdout.getvalue(), stderr.getvalue(), opener


class ClientSafetyTests(unittest.TestCase):
    def build(self, responses):
        opener = RecordingOpener(responses)
        client = client_module.Client()
        client._opener = opener
        return client, opener

    def test_unauthenticated_reads_are_refused(self):
        client, opener = self.build([])
        with self.assertRaises(client_module.ApiError):
            client.homework("role-id", date(2026, 9, 7), date(2026, 9, 13), "home")
        self.assertEqual(opener.requests, [])

    def test_only_allowlisted_read_routes_are_reachable(self):
        client, _ = self.build([])
        for route in ("GetSchedule", "Impersonate", "Logout", "SetMessageRead", "CreatePayment"):
            with self.assertRaises(client_module.ApiError):
                client._request(route, query={}, role=None)

    def test_unexpected_query_fields_are_refused(self):
        client, _ = self.build([])
        with self.assertRaises(client_module.ApiError):
            client._request("core/app/darbai", role="r",
                            query={"dateFrom": "2026-09-07", "dateTo": "2026-09-13",
                                   "workType": "home", "extra": "1"})

    def test_role_routes_require_a_role(self):
        client, _ = self.build([])
        with self.assertRaises(client_module.ApiError):
            client._request("core/app/darbai", role=None,
                            query={"dateFrom": "2026-09-07", "dateTo": "2026-09-13", "workType": "home"})

    def test_only_one_login_attempt_is_allowed(self):
        client, _ = self.build([SUCCESS])
        client.login("user", "pw")
        with self.assertRaises(client_module.ApiError):
            client.login("user", "pw")

    def test_login_rejects_unsuccessful_envelope(self):
        client, _ = self.build([{"Status": 0, "ErrorCode": 0, "Result": None}])
        with self.assertRaises(client_module.ApiError):
            client.login("user", "pw")

    def test_login_requires_allowed_role(self):
        client, _ = self.build([{"Status": 1, "ErrorCode": 0,
                                 "Result": {"authToken": "t", "userRoleIsAllowed": False}}])
        with self.assertRaises(client_module.ApiError):
            client.login("user", "pw")

    def test_redirects_are_not_followed(self):
        self.assertIsNone(client_module.NoRedirect().redirect_request(
            Mock(), Mock(), 302, "Found", {}, "https://example.invalid"))


class HelperTests(unittest.TestCase):
    def test_iso_date_rejects_non_iso(self):
        with self.assertRaises(Exception):
            client_module.iso_date("07/09/2026")

    def test_choose_role_requires_usable_id(self):
        with self.assertRaises(client_module.ApiError):
            client_module.choose_role([{"title": "x"}], 0)

    def test_choose_role_rejects_out_of_range_index(self):
        with self.assertRaises(client_module.ApiError):
            client_module.choose_role([{"id": "a"}], 5)

    def test_content_output_is_ascii_escaped(self):
        """Print path must not let server text inject terminal control sequences."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            client_module.print_content({"title": "\x1b[31mred\x1b[0m"})
        self.assertNotIn("\x1b", buffer.getvalue())
        self.assertIn("\\u001b", buffer.getvalue())


class ExampleTests(unittest.TestCase):
    # client.roles() performs StyleRef then roles, so each example needs both.
    STYLE_REF = payload()
    ROLES = payload(roles=[{"id": "role-id", "title": "Student"}])

    @property
    def login_responses(self):
        return [SUCCESS, self.STYLE_REF, self.ROLES]

    def test_login_reports_counts_without_credentials(self):
        code, out, err, opener = run_example(login, [], self.login_responses)
        self.assertEqual(code, 0, err)
        self.assertIn("Roles returned: 1", out)
        self.assertNotIn("token-value", out)
        self.assertNotIn("Student", out)
        self.assertEqual([r.get_method() for r in opener.requests], ["POST", "GET", "GET"])

    def test_login_does_not_print_role_labels_by_default(self):
        _, out, _, _ = run_example(login, [], self.login_responses)
        self.assertNotIn("Student", out)

    def test_login_can_opt_into_role_labels(self):
        _, out, err, _ = run_example(login, ["--show-role-labels"], self.login_responses)
        self.assertIn("Student", out)

    def test_homework_prints_count_not_content_by_default(self):
        code, out, err, _ = run_example(homework, [], self.login_responses + [
            payload(items=[{"thingName": "secret", "date": "2026-09-08"}]),
        ])
        self.assertEqual(code, 0, err)
        self.assertIn("home: 1 items", out)
        self.assertNotIn("secret", out)

    def test_homework_show_content_opts_in(self):
        code, out, err, _ = run_example(homework, ["--show-content"], self.login_responses + [
            payload(items=[{"thingName": "secret"}]),
        ])
        self.assertEqual(code, 0, err)
        self.assertIn("secret", out)

    def test_calendar_prints_counts_only_by_default(self):
        code, out, err, _ = run_example(calendar_week, [], self.login_responses + [
            payload(days=[{"date": "2026-09-07", "events": [{"eventTitle": "secret"}]}]),
        ])
        self.assertEqual(code, 0, err)
        self.assertIn("1 days, 1 events", out)
        self.assertNotIn("secret", out)

    def test_calendar_show_content_opts_in(self):
        code, out, err, _ = run_example(calendar_week, ["--show-content"], self.login_responses + [
            payload(days=[{"date": "2026-09-07", "events": [{"eventTitle": "secret"}]}]),
        ])
        self.assertEqual(code, 0, err)
        self.assertIn("secret", out)

    def test_examples_never_send_a_write_verb(self):
        for module, argv, responses in (
            (login, [], self.login_responses),
            (homework, [], self.login_responses + [payload(items=[])]),
            (calendar_week, [], self.login_responses + [payload(days=[])]),
        ):
            _, _, _, opener = run_example(module, argv, responses)
            for request in opener.requests:
                self.assertIn(request.get_method(), ("GET", "POST"))
                if request.get_method() == "POST":
                    self.assertTrue(request.full_url.endswith("AuthenticateV2"))


class DocumentConsistencyTests(unittest.TestCase):
    """The published reference must not drift from the examples it documents."""

    def read(self, name):
        return (DOCS / name).read_text(encoding="utf-8")

    def test_modern_endpoint_docs_cover_every_allowlisted_route(self):
        modern = self.read("endpoints-modern.md")
        for route in client_module.READ_ROUTES:
            self.assertIn(route, modern, f"{route} is used by the examples but missing from the docs")

    def test_documented_success_conditions_match_the_client(self):
        readme = (DOCS.parent / "README.md").read_text(encoding="utf-8")
        self.assertIn("isSuccess == true", readme)
        self.assertIn("Status == 1", readme)
        self.assertIn("ErrorCode == 0", readme)

    def test_documented_bases_match_the_client(self):
        readme = (DOCS.parent / "README.md").read_text(encoding="utf-8")
        self.assertIn(client_module.MODERN_BASE, readme)
        self.assertIn(client_module.LEGACY_BASE, readme)

    def test_premium_doc_does_not_claim_expiry_is_untested(self):
        """The post-expiry run is documented; stale 'untested' claims must not return."""
        premium = self.read("premium.md")
        self.assertNotRegex(premium, r"expired-subscription access (remains |has not been )?untested")
        self.assertIn("After subscription expiry", self.read("validation.md"))

    def test_base_urls_are_https(self):
        for base in (client_module.MODERN_BASE, client_module.LEGACY_BASE):
            self.assertTrue(base.startswith("https://"))


if __name__ == "__main__":
    unittest.main()
