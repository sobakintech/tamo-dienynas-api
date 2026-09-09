# Python examples

[API overview](../README.md) | [Authentication details](../docs/authentication.md)

Three small programs demonstrate login, role selection, homework, and calendar reads. They are usage examples, not a full SDK.

The [unofficial-access warning](../README.md#disclaimer) applies to these examples, even when using your own account.

## Requirements

- Python 3.10 or newer.
- An interactive terminal that supports hidden input.
- A valid TAMO account. Assume an active TAMO IŠMANIEMS subscription for school-data reads; unpaid and expired-subscription access is untested. See [premium](../docs/premium.md).

No packages need to be installed. The examples use the Python standard library. Run the commands below from the repository root. If your system uses `python3` or the Windows `py` launcher, substitute that command for `python`.

Start with `python examples/login.py`. Use `--help` on any program to see its options without logging in.

## Login and roles

```sh
python examples/login.py
```

You will be prompted for username and password, both hidden. The program logs in, requests the style reference and roles, then prints the number of roles. It does not print or save the token.

For an account with multiple roles, explicitly reveal labels to identify the role you want:

```sh
python examples/login.py --show-role-labels
```

Labels can contain personal or school information. The displayed `index` is a local, zero-based array position, not the value sent to the API. A data example uses that position to select a role returned by its own fresh login, then sends the role's actual `id` in the header. Role ordering is not a stable identifier and may change between logins.

If more than one role is returned, data examples refuse to choose silently. Specify `--role-index 0` or the appropriate returned index. The examples never construct or guess server role IDs.

## Homework and classwork

```sh
python examples/homework.py
python examples/homework.py --work-type class
python examples/homework.py --from 2025-01-06 --to 2025-01-12 --role-index 0
```

The default date range is the current Monday through Sunday. If only `--from` is supplied, the range ends six days later. Custom ranges are limited to 31 calendar days by the example, not by a verified server rule.

Output is an item count unless you explicitly request content:

```sh
python examples/homework.py --show-content
```

That prints subject labels, lesson dates, deadlines, homework text, and completion dates. It does not change completion status, download attachments, or print the complete server response.

## Calendar week

```sh
python examples/calendar_week.py
python examples/calendar_week.py --date 2025-01-08 --role-index 0
python examples/calendar_week.py --show-content
```

`--date` can be any day in the desired week. The program aligns it to Monday before calling `v2/app/calendar/events`, matching the recovered app flow. Default output contains the returned day and event counts. `--show-content` prints selected event times and display-content objects. It does not open linked pages or files.

## Requests made

| Program | Requests |
| --- | --- |
| `login.py` | Login POST, style-reference GET, roles GET |
| `homework.py` | The same three requests, then one homework/classwork GET |
| `calendar_week.py` | The same three requests, then one calendar-week GET |

Every execution performs a new login. There is no background polling or automatic retry. Do not run the examples in a rapid loop. `--help` performs no login or network request.

The shared `_client.py` only allows the documented login POST and four specific modern GET routes. It contains no upload, message, payment, completion, logout, or push-registration operation. Authentication can create a server session; the remaining operations are read-oriented API requests.

## Privacy and failure behavior

- Passwords/tokens are not accepted as command-line arguments, written to files, or included in normal output.
- Credentials and responses exist in process memory while needed. Python object disposal is not a secure-memory-erasure guarantee.
- The programs make direct verified HTTPS connections to the two known TAMO service origins. Environment-configured HTTP proxies are disabled in these examples.
- Redirects are rejected rather than followed with credentials. Requests use a 20-second timeout and a 4 MiB response limit.
- HTTP errors and unsuccessful JSON envelopes produce a nonzero exit status. Raw URLs, bodies, and server error messages are withheld to avoid leaking account data.
- Missing or changed collection shapes are reported as errors, not silently replaced with empty results.
- Printed content uses JSON escaping, including Unicode escapes, to avoid executing terminal-control characters.
- Tokens are discarded locally on exit. No server logout or revocation request is sent.

An HTTP 404, 401, 403, 429, transport failure, or unsuccessful business envelope should be investigated without blindly retrying. A successful login does not prove that a selected data endpoint is included in the account's subscription.

## What was tested

The request formats are based on static analysis and [live read-only checks](../docs/validation.md). The examples themselves were tested offline with synthetic responses, covering rejected writes, failed authentication, role selection, malformed data, timeouts, redirects, and output redaction. Their complete command-line flows have not been tested against the live API.
