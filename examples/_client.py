"""Shared HTTP plumbing for these read-only examples, not a general-purpose SDK."""

import argparse
from datetime import date, datetime, timedelta
import getpass
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
import warnings


LEGACY_BASE = "https://dienynas.tamo.lt/MobileServiceV3/"
MODERN_BASE = "https://api.tamo.lt/"
LOGIN_ROUTE = "AuthenticateV2"
READ_ROUTES = {
    "core/app/settings/StyleRef": frozenset(),
    "core/app/roles": frozenset(),
    "core/app/darbai": frozenset({"dateFrom", "dateTo", "workType"}),
    "v2/app/calendar/events": frozenset({"date"}),
}
ROLE_ROUTES = {"core/app/darbai", "v2/app/calendar/events"}
MAX_RESPONSE_BYTES = 4 * 1024 * 1024


class ApiError(Exception):
    """A safe-to-print error containing no raw response or credential values."""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Client:
    def __init__(self):
        self._token = None
        self._login_attempted = False
        self._opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({}), NoRedirect()
        )

    def close(self):
        self._token = None

    def _request(self, route, *, query=None, role=None, login_body=None):
        query = query or {}
        headers = {"Accept": "application/json", "User-Agent": "okhttp/4.9.1"}
        if login_body is not None:
            if route != LOGIN_ROUTE or query or role:
                raise ApiError("Only the documented login POST is supported.")
            if self._login_attempted:
                raise ApiError("This client allows only one login attempt.")
            self._login_attempted = True
            url = LEGACY_BASE + LOGIN_ROUTE
            method = "POST"
            body = json.dumps(login_body).encode("utf-8")
            headers["Content-Type"] = "application/json; charset=UTF-8"
        else:
            if route not in READ_ROUTES or set(query) != READ_ROUTES[route]:
                raise ApiError("Route or query fields are outside the example allowlist.")
            if not self._token:
                raise ApiError("Log in before reading data.")
            if route in ROLE_ROUTES and not role:
                raise ApiError("This read requires a role returned by the account.")
            url = MODERN_BASE + route
            if query:
                url += "?" + urllib.parse.urlencode(query)
            method, body = "GET", None
            headers["Authorization"] = "Bearer " + self._token
            if role:
                headers["x-selected-role"] = role

        try:
            request = urllib.request.Request(url, data=body, headers=headers, method=method)
            with self._opener.open(request, timeout=20) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ApiError("Response exceeded the example's 4 MiB safety limit.")
            payload = json.loads(raw)
        except urllib.error.HTTPError as error:
            code = error.code
            error.close()
            raise ApiError(f"HTTP {code}. No retry or redirect was attempted.") from None
        except (urllib.error.URLError, OSError, ValueError, UnicodeError):
            raise ApiError("Network/TLS failure or invalid JSON response; details withheld.") from None

        if not isinstance(payload, dict):
            raise ApiError("Expected a JSON object response.")
        if login_body is not None:
            if payload.get("Status") != 1 or payload.get("ErrorCode") != 0:
                code = payload.get("ErrorCode")
                detail = f" (ErrorCode {code})" if type(code) is int else ""
                raise ApiError("Login was not accepted" + detail + ".")
        elif payload.get("isSuccess") is not True:
            raise ApiError("The API reported an unsuccessful read; response text withheld.")
        return payload

    def login(self, username, password):
        body = {
            "username": username,
            "password": password,
            "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "typePhoneSystem": "Android",
            "guid": "1166cfd3-1be5-4dca-aa64-5aff7bbb8acc",
        }
        try:
            payload = self._request(LOGIN_ROUTE, login_body=body)
        finally:
            body.clear()
        result = payload.get("Result")
        if not isinstance(result, dict) or result.get("userRoleIsAllowed") is not True:
            raise ApiError("The account did not return an allowed role.")
        token = result.get("authToken")
        if not isinstance(token, str) or not token or any(ord(c) < 32 or ord(c) == 127 for c in token):
            raise ApiError("Login did not return a usable token.")
        self._token = token

    def roles(self):
        self._request("core/app/settings/StyleRef")
        payload = self._request("core/app/roles")
        roles = require_list(payload, "roles")
        if not roles or any(not isinstance(role, dict) for role in roles):
            raise ApiError("The account returned no usable role list.")
        return roles

    def homework(self, role, start, end, work_type):
        if work_type not in {"home", "class"}:
            raise ApiError("Unsupported work type.")
        return self._request(
            "core/app/darbai",
            role=role,
            query={"dateFrom": start.isoformat(), "dateTo": end.isoformat(), "workType": work_type},
        )

    def calendar(self, role, monday):
        return self._request("v2/app/calendar/events", role=role, query={"date": monday.isoformat()})


def require_list(payload, key):
    value = payload.get(key)
    if not isinstance(value, list):
        raise ApiError(f"Expected the '{key}' collection; its shape may have changed.")
    return value


def choose_role(roles, index):
    if index is None:
        if len(roles) != 1:
            raise ApiError("Multiple roles returned. Run login.py, then use --role-index.")
        index = 0
    if index < 0 or index >= len(roles):
        raise ApiError("Role index is outside the returned role list.")
    identifier = roles[index].get("id")
    if not isinstance(identifier, str) or not identifier or any(ord(c) < 32 or ord(c) == 127 for c in identifier):
        raise ApiError("Selected role has no usable id.")
    return identifier


def iso_date(value):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() != value:
            raise ValueError
        return parsed
    except ValueError:
        raise argparse.ArgumentTypeError("Use a date in YYYY-MM-DD format.") from None


def current_monday():
    today = date.today()
    return today - timedelta(days=today.weekday())


def print_content(value):
    # ASCII escaping prevents returned text from injecting terminal control sequences.
    print(json.dumps(value, ensure_ascii=True, indent=2))


def run_authenticated(action):
    client = Client()
    username = password = None
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", getpass.GetPassWarning)
            username = getpass.getpass("Username (hidden): ")
            password = getpass.getpass("Password (hidden): ")
        if not username or not password:
            raise ApiError("Username and password must not be empty.")
        client.login(username, password)
        username = password = None
        action(client)
        return 0
    except ApiError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except getpass.GetPassWarning:
        print("Error: hidden input is unavailable. Run in an interactive terminal.", file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print("Cancelled.", file=sys.stderr)
        return 130
    except Exception:
        print("Error: unexpected response or runtime failure; details withheld to protect account data.", file=sys.stderr)
        return 1
    finally:
        username = password = None
        client.close()
