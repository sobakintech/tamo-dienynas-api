# Protocol conventions

[Overview](../README.md) | [Authentication](authentication.md) | [Models](models/README.md)

This page describes the analyzed Android client's behavior. Transport defaults, retry policy, and caches are not server requirements. The Python examples intentionally use a smaller, more conservative request flow.

## Hosts and headers

| Purpose | Default URL |
| --- | --- |
| Modern service | `https://api.tamo.lt/` |
| Legacy service | `https://dienynas.tamo.lt/MobileServiceV3/` |
| Messaging web entry | `https://dienynas.tamo.lt/goto/bendrauk` |
| Password reset page | `https://dienynas.tamo.lt/Prisijungimas/ResetPassword` |

Modern operations declare `Accept: application/json` and `Authorization`. Role-scoped operations also declare `x-selected-role`. Legacy declarations place `authToken` in the query, form, or JSON body as specified by each endpoint; they do not declare the modern Bearer header.

The app reads default service URLs from preferences. A debug screen can override those values and restart the app. No server-driven replacement of the service base URLs was established. Returned menus, files, images, and content can contain other URLs.

Do not pass credentials through arbitrary proxies or make base URLs user-controlled without checking the intended destination. A native-client success also says nothing about whether a website can call the API cross-origin: browser CORS behavior was not tested.

## Response envelopes and errors

Legacy responses use:

```json
{"Status": 1, "ErrorCode": 0, "ErrorMessage": null, "Result": {}}
```

The client considers `Status == 1 && ErrorCode == 0` successful. The `Result` shape depends on the operation. `ItemsResponse` accepts both `items` and `Items`, preferring the lowercase collection when non-null. Both spellings occurred in successful live responses.

Modern responses have common status fields:

```json
{"isSuccess": true, "message": null, "errors": [], "items": []}
```

This is an illustrative shape. `items` is specific to some payloads, and fields can be absent or null. Modern success requires `isSuccess == true` as well as an acceptable HTTP status. The payload can instead be named `roles`, `settings`, `styleRef`, `days`, `allDayEvents`, `result`, or `url`.

| Condition | Observed client handling or live result |
| --- | --- |
| Legacy `ErrorMessage == "User is not authenticated."` | Starts the app's authentication/logout handling |
| Legacy `ErrorCode == -13` | Opens subscription UI; exact server policy remains inferred |
| Modern `isSuccess == false` | Converted to an error by the common repository adapter |
| HTTP failure | Handled separately from a successful JSON envelope |
| Legacy message-header requests in the paid baseline | HTTP 404, non-JSON response |

Never assume an error body is JSON. Do not automatically interpret a 404 as a premium denial or a 200 as successful access. Avoid logging raw error bodies because they can contain account information or request details.

## Dates and serialization

- Modern date query parameters use `YYYY-MM-DD`. The calendar-week request aligns the selected date to Monday.
- Legacy date-range reads accepted `YYYY-MM-DD` in the baseline. Maximum ranges and boundary inclusivity were not tested.
- Login uses a device-local datetime with a space between date and time and no timezone suffix.
- The client has adapters for `LocalDate`, `Date`, `LocalDateTime`, and `ZonedDateTime`; these should not all be parsed identically.
- The explicit `LocalDateTime` adapter uses `yyyy-MM-dd'T'HH:mm:ss.SSSSSSS'Z'`. Its `Z` is a literal character in that parser, not evidence of a timezone-aware value.
- The `Date` adapter reads `yyyy-MM-dd`. Subscription date conversion separately uses `yyyy-MM-dd HH:mm:ss`.
- JSON fields preserve wire casing and explicit `SerializedName` aliases. Names changed by the decompiler are not wire names.
- Query/form values use normal URL encoding. Repeated `paramKeys` are repeated query parameters, not a comma-separated string. Boxed null query arguments can be omitted.
- JSON bodies use `application/json; charset=UTF-8`. Form bodies use `application/x-www-form-urlencoded`.

The [model reference](models/README.md) lists client types. It does not prove server requiredness, outgoing support, or all possible values. In particular, an internal Realm model can mix server fields with locally derived dates and cache metadata.

## Transport in the Android app

The two service interfaces use Retrofit with Gson and RxJava adapters, sharing an OkHttp client. The recovered default user agent is `okhttp/4.9.1`.

| Setting | Recovered behavior |
| --- | --- |
| Protocols | HTTP/2 and HTTP/1.1 configured |
| Connect/read/write timeouts | 10 seconds each |
| Overall call timeout | No override found |
| Redirects | Enabled |
| Connection retry | Enabled |
| Response cache | No HTTP cache configured |
| Cookies | Empty Retrofit/OkHttp cookie jar; WebViews use a separate store |
| Compression | Gzip acceptance and decompression through OkHttp |
| Network logging | Interceptor level `NONE` |
| TLS trust | Platform trust and hostname verification |
| Certificate pinning | No app-specific pin set found |

`ProviderInstaller` is called to update the security provider. The app targets SDK 35 and declares no custom network security configuration. Actual TLS negotiation, trusted roots, Android cleartext policy, and proxy behavior depend on the runtime environment. None was established by a packet capture here.

## Retries and caches

Modern repositories commonly retry up to three times with delays of 1, 4, and 9 seconds. That wrapper also appears around mutation operations, including homework completion. Several legacy flows have analogous retry handling. These are descriptions of the official client, not a recommended policy for replaying writes.

The common modern repository cache has a 60-second freshness period. Subscription state uses 5 seconds. Global settings have a one-hour preference freshness check. Legacy data is also stored in Realm. These intervals do not establish a server rate limit, polling allowance, or data freshness guarantee.

The example programs do not automatically retry or follow redirects. They stop on failure and avoid printing request URLs or raw server error text.

## Evidence

Relevant build 4.17 symbols include `lt.zet.tamo.a`, `lt.zet.tamo.n`, `ye.p`, `ye.g0`, `ye.b`, `ye.a`, `ze.z`, `af.l0`, `af.l1`, `af.y0`, and `of.c`. Live-validated behavior is listed separately in [validation](validation.md).
