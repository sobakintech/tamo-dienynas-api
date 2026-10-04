# TAMO dienynas API

Unofficial TAMO dienynas API reference and Python examples.

Covers authentication, roles, diary entries, grades, homework, calendars, messages, files, subscriptions, and push registration, with endpoint parameters and response models.

Based on reverse engineering the **TAMO IŠMANIEMS** Android app, with selected read endpoints checked against the live API. See [scope and evidence](docs/scope.md) for the analyzed build and [validation](docs/validation.md) for test results.

<a id="disclaimer"></a>

> [!WARNING]
> TAMO's [Terms of Use](https://content.tamo.lt/taisykles/naudojimo.html), sections 9.1, 9.2, and 9.4, prohibit unofficial programmatic/API access outside documented integrations. This reference does not grant permission to use the API.
>
> **Use at your own risk.** Account restrictions or loss of access are possible. The likelihood of enforcement is unknown; successful requests do not imply approval or protection from a ban.

## Subscription requirement

**An active TAMO IŠMANIEMS subscription is still the safe assumption — but it is not required for the modern API in at least one tested case.**

After one account's subscription lapsed, every tested modern route still returned real data: diary, homework, classwork, grades, calendar, and feeds. What stopped returning data was the older legacy `MobileServiceV3` school-data routes, which came back empty (`Status: 0`).

Two caveats keep this from being a blanket answer: that account was still classified by the server as a paid *type* with no active subscription, which is a different state from never having paid; and a never-paid `free`-type account has not been tested. The modern routes may not be available to one.

See [premium behavior](docs/premium.md) and [after-expiry results](docs/validation.md#after-subscription-expiry).

## Start here

| Topic | Reference |
| --- | --- |
| First request | [Authentication and roles](docs/authentication.md), [Python examples](examples/README.md) |
| Endpoint lookup | [Modern API](docs/endpoints-modern.md), [legacy API](docs/endpoints-legacy.md) |
| Request and response details | [Models](docs/models/README.md), [dates, headers, and errors](docs/protocol.md) |
| Feature behavior | [Files, messaging, push, and other workflows](docs/workflows.md) |
| Subscription access | [Premium](docs/premium.md) |
| Evidence and limitations | [Live validation](docs/validation.md), [scope](docs/scope.md) |

## The two services

| Service | Base URL | Authentication | Success condition |
| --- | --- | --- | --- |
| Modern | `https://api.tamo.lt/` | `Authorization: Bearer <token>` | `isSuccess == true` in a successful HTTP response |
| Legacy | `https://dienynas.tamo.lt/MobileServiceV3/` | Usually query parameter `authToken` | `Status == 1` and `ErrorCode == 0` in a successful HTTP response |

Login happens on the legacy service. The returned token is also accepted by the modern service. Role-scoped modern requests send `x-selected-role` using the returned role's **`id`**, not `roleId` or `studentId`.

## What is confirmed

The analyzed app declares **43 fixed Retrofit routes** and **one dynamic-URL download method**. A separate authenticated WebView route is constructed manually. The reference includes **114 client model/support classes** and **559 direct fields**, with important caveats for local cache models.

Read-only checks covered 24 requests across 23 distinct routes, including login:

- Authentication and 21 read requests succeeded.
- `GetReceivedMessageHeaders` and `GetSendMessageHeaders` returned HTTP 404.
- No payment, upload, message change, homework change, push registration, or logout was tested.

After that account's subscription lapsed, the same checks were repeated: all modern routes still returned data, while the legacy school-data routes returned empty results. See [validation](docs/validation.md#after-subscription-expiry).

These results are from **one account**. An endpoint present in the APK is not necessarily available on the current server, and a never-paid account is untested. See [validation](docs/validation.md) for details.

## Run an example

Python 3.10 or newer is required. There are no third-party dependencies.

```sh
python examples/login.py
python examples/homework.py
python examples/calendar_week.py
```

Each example prompts for credentials with hidden input, logs in once, and keeps its token in memory. By default, it prints counts rather than personal content. Add `--show-content` to the homework or calendar example to display the returned school data. See [example options and privacy](examples/README.md) for details. These are small usage examples, not a full SDK.

## Used by

- [better-tamo](https://github.com/sobakintech/better-tamo) is built on this API reference.
- [tamo-dienynas-mcp](https://github.com/sobakintech/tamo-dienynas-mcp) is a read-only MCP server that lets AI assistants read the TAMO dienynas.

## Important limitations

- Some legacy **GET requests change state**, including payment creation, read-marking, message deletion, impersonation, and logout. HTTP method alone is not a safety classification.
- Token lifetime, server rate limits, upload limits, cross-account authorization, browser CORS behavior, and unpaid endpoint access remain unverified.
- API fields and behavior can change without notice. The app's response models do not describe every possible server field.
- Authentication tokens and signed download URLs can grant access to private account data.

Original APKs, decompiled source, analysis tools, account responses, and device metadata are intentionally not included. See [scope](docs/scope.md) for the build identifier and evidence boundaries.

This project is not affiliated with TAMO.
