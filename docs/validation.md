# Live validation

[Overview](../README.md) | [Modern endpoints](endpoints-modern.md) | [Legacy endpoints](endpoints-legacy.md)

## Baseline

Read-only checks covered **24 requests across 23 distinct routes**, including login. The homework route was checked twice, once for `home` and once for `class`.

These results apply with an active paid subscription. Free, trial, and expired-subscription access is untested.

- Login and **21 read requests succeeded**, with successful HTTP responses and API status fields.
- Two legacy message-header reads returned **HTTP 404** with non-JSON responses.
- The same login token worked with legacy query authentication and modern Bearer authentication.
- Role-scoped reads accepted the returned role's `id` in `x-selected-role`.

Results can vary by role, request parameters, and server changes.

## Successful requests

| Service | Routes |
| --- | --- |
| Legacy authentication | `AuthenticateV2` |
| Legacy subscriptions/configuration | `GetSubscriptionType`, `GetUserSubscriptions`, `GetProducts`, `GetGlobalSettings`, `GetAdditionalMenu` |
| Legacy school data | `GetAssessments`, `GetAwards`, `GetLessons`, `GetNextEvents`, `GetSchedule`, `GetRatingSubjects` |
| Modern account/configuration | `core/app/settings/StyleRef`, `core/app/roles`, `core/app/settings/global` |
| Modern school data | `core/app/dienynas`, `core/app/darbai` with both work types, `core/app/calendar/badges`, `core/app/calendar/events/allDay`, `v2/app/calendar/events`, `core/app/feeds` |

Date-range checks covered one week, with Monday as the calendar start date.

Legacy settings checks covered `premium_headertxt` and `premium_days`. Additional menus used `MoreWnd.BelowStatic`; returned links were not opened. The all-day events request returned an empty list, so individual event fields remain unverified.

## Failed requests

| Request | Result |
| --- | --- |
| `GET MobileServiceV3/GetReceivedMessageHeaders` | HTTP 404; non-JSON response |
| `GET MobileServiceV3/GetSendMessageHeaders` | HTTP 404; non-JSON response |

Alternate paths, versions, and the message WebView remain untested. These 404 responses do not explain whether the routes were removed or why they failed. They also say nothing about access without premium.

## Useful protocol confirmations

- The documented login JSON worked without push registration, an Android installation identity, or WebView cookies.
- `Role.id`, not `roleId`, worked as the selected-role header.
- Both `workType=home` and `workType=class` returned data.
- A Monday request to `v2/app/calendar/events` returned seven days.
- Legacy collection casing varied: both `Items` and `items` occurred.
- Modern feeds used the JSON property `result`.
- Modern responses included extra fields not listed in the client models. The model reference does not cover every server field.

## Write checks

Later, `POST core/app/darbai/namu/atlikimas` was tested on one student account, marking one homework item done and then not done:

- Both requests returned `isSuccess: true`, and the official app showed the same state after a refresh.
- `MokinioId` had to be the role's `childStudentId`. The work item's `studentId` (the person ID) returned HTTP 200 with `isSuccess: false` and a "nesutampa su prisijungusio mokinio id" error, without changing anything.
- `core/app/roles` returned a different role `id` on each request; an earlier `id` still worked in `x-selected-role`.

## Exclusions

Apart from homework completion (see above), authentication was the only POST. No other state-changing endpoints were tested, including GET routes for impersonation, logout, payments, read-marking, and deletion. Message sending, uploads, device registration/removal, and test notifications also remain untested.

Full messages were not opened because fetching them might mark them as read. File URL lookup, downloads, recipient lists, WebViews, arbitrary URLs, and third-party services remain untested. Period, subject, and filter requests that require a prior selection are documented from static analysis only.

Unauthenticated access, role enumeration, authorization bypass, upload quotas, rate limits, and token revocation were not tested. These checks were not a security audit or a capture of the app's network traffic.

## Test setup

Requests ran one at a time over verified HTTPS, with no automatic retries or redirects and a response-size limit. The checks did not reproduce every detail of the app's OkHttp client. Read-only requests can still create server logs or update internal state.

The included Python examples were tested offline with synthetic responses. Their complete command-line flows have not been tested against the live API.
