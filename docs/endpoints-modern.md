# Modern API endpoints

[Overview](../README.md) | [Authentication](authentication.md) | [Models](models/README.md) | [Validation](validation.md)

Base URL: `https://api.tamo.lt/`.

All 15 operations declare `Accept: application/json` and `Authorization: Bearer <token>`. Role-scoped calls also declare `x-selected-role`, using `Role.id`. Modern JSON responses inherit `StatusResponse`, except installation operations with no typed body.

| Method | Route | Operation | Evidence |
| --- | --- | --- | --- |
| GET | [`core/app/settings/StyleRef`](#get-core-app-settings-styleref) | Read-oriented | Paid baseline: success |
| GET | [`core/app/roles`](#get-core-app-roles) | Read-oriented | Paid baseline: success |
| GET | [`core/app/settings/global`](#get-core-app-settings-global) | Read-oriented | Paid baseline: success |
| GET | [`core/app/dienynas`](#get-core-app-dienynas) | Read-oriented | Paid baseline: success |
| GET | [`core/app/darbai`](#get-core-app-darbai) | Read-oriented | Paid baseline: success |
| GET | [`core/app/calendar/badges`](#get-core-app-calendar-badges) | Read-oriented | Paid baseline: success |
| GET | [`core/app/calendar/events/allDay`](#get-core-app-calendar-events-allday) | Read-oriented | Paid baseline: success |
| GET | [`v2/app/calendar/events`](#get-v2-app-calendar-events) | Read-oriented | Paid baseline: success |
| GET | [`core/app/feeds`](#get-core-app-feeds) | Read-oriented | Paid baseline: success |
| GET | [`core/app/analytics/periodsummary`](#get-core-app-analytics-periodsummary) | Read-oriented | Static only |
| POST | [`files/filedownloadurl`](#post-files-filedownloadurl) | Download URL lookup | Static only |
| POST | [`core/app/darbai/namu/atlikimas`](#post-core-app-darbai-namu-atlikimas) | Changes state | Static only |
| POST | [`core/app/devices/installation`](#post-core-app-devices-installation) | Changes state | Static only |
| DELETE | [`core/app/devices/installation/{installationId}`](#delete-core-app-devices-installation-installationid) | Changes state | Static only |
| POST | [`core/app/utilities/sendnotification`](#post-core-app-utilities-sendnotification) | Changes state | Static only |

Live success is limited to the tested account and parameters, not every role, date range, or subscription state. Read-oriented describes the client's intent, not a guarantee of zero internal server effects.

<a id="get-core-app-settings-styleref"></a>

## GET core/app/settings/StyleRef

The app requests this before loading roles. Response content uses style references to control presentation.

Evidence: Paid baseline: success. Client declaration: `ye.p.c` in build 4.17.

Response type: `StyleRefResponse`.

Models: [response.StyleRefResponse](models/response.md#stylerefresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |

<a id="get-core-app-roles"></a>

## GET core/app/roles

Each role has both `id` and `roleId`. Send `id` in `x-selected-role`. Use only a role returned for the authenticated account.

Evidence: Paid baseline: success. Client declaration: `ye.p.f` in build 4.17.

Response type: `UserResponse`.

Models: [response.UserResponse](models/response.md#userresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |

<a id="get-core-app-settings-global"></a>

## GET core/app/settings/global

Returns the `settings` collection. The client also attempts this during startup, potentially before a token exists; anonymous acceptance was not established.

Evidence: Paid baseline: success. Client declaration: `ye.p.m` in build 4.17.

Response type: `GlobalSettingsResponse`.

Models: [response.GlobalSettingsResponse](models/response.md#globalsettingsresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |

<a id="get-core-app-dienynas"></a>

## GET core/app/dienynas

Returns `items` and `formativeGrades`. Dates use `YYYY-MM-DD`.

Evidence: Paid baseline: success. Client declaration: `ye.p.g` in build 4.17.

Response type: `DienynasResponse`.

Models: [response.DienynasResponse](models/response.md#dienynasresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-core-app-darbai"></a>

## GET core/app/darbai

Observed `workType` values are `home` and `class`. Both succeeded in the paid baseline. Completion filtering also occurs locally in the app.

Evidence: Paid baseline: success. Client declaration: `ye.p.j` in build 4.17.

Response type: `WorkResponse`.

Models: [response.WorkResponse](models/response.md#workresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |
| query | `workType` | `String` |

<a id="get-core-app-calendar-badges"></a>

## GET core/app/calendar/badges

The app usually requests a month range. A seven-day range also succeeded in the baseline.

Evidence: Paid baseline: success. Client declaration: `ye.p.i` in build 4.17.

Response type: `DayBadgesResponse`.

Models: [response.DayBadgesResponse](models/response.md#daybadgesresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-core-app-calendar-events-allday"></a>

## GET core/app/calendar/events/allDay

Returns `allDayEvents`. The paid baseline returned an empty list, so nonempty element behavior is static-only.

Evidence: Paid baseline: success. Client declaration: `ye.p.k` in build 4.17.

Response type: `AllDayEventsResponse`.

Models: [response.AllDayEventsResponse](models/response.md#alldayeventsresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-v2-app-calendar-events"></a>

## GET v2/app/calendar/events

The app aligns `date` to Monday. The paid baseline returned seven days. Also returns `grades` and `formatives`.

Evidence: Paid baseline: success. Client declaration: `ye.p.n` in build 4.17.

Response type: `DayEventsResponse`.

Models: [response.DayEventsResponse](models/response.md#dayeventsresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `date` | `String` |

<a id="get-core-app-feeds"></a>

## GET core/app/feeds

The payload is named `result`, even though the client getter is named `getItems()`.

Evidence: Paid baseline: success. Client declaration: `ye.p.o` in build 4.17.

Response type: `FeedsResponse`.

Models: [response.FeedsResponse](models/response.md#feedsresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |

<a id="get-core-app-analytics-periodsummary"></a>

## GET core/app/analytics/periodsummary

Uses an event SID supplied by the calendar response. Do not substitute a numeric lesson ID or enumerate values.

Evidence: Static only. Client declaration: `ye.p.a` in build 4.17.

Response type: `PeriodSummaryResponse`.

Models: [response.PeriodSummaryResponse](models/response.md#periodsummaryresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| query | `eventSid` | `String` |

<a id="post-files-filedownloadurl"></a>

## POST files/filedownloadurl

Read-oriented URL lookup implemented as POST. Sends `fileSid` as a form field and returns `url`. URL generation/download behavior was not live-tested. See [files](workflows.md#files-and-attachments).

Evidence: Static only. Client declaration: `ye.p.l` in build 4.17.

Response type: `FileUrlResponse`.

Models: [response.FileUrlResponse](models/response.md#fileurlresponse).

Request content type: `application/x-www-form-urlencoded`.

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| form | `fileSid` | `String` |

<a id="post-core-app-darbai-namu-atlikimas"></a>

## POST core/app/darbai/namu/atlikimas

Marks a homework item done or not done. This is the checkbox in the official app's homework list. Form field casing is significant: `MokinioId`, `PamokosId`, `Atliktas`.

| Field | Value sent by the app |
| --- | --- |
| `MokinioId` | `studentId` of the selected role (`core/app/roles`), not the work item's own `studentId` |
| `PamokosId` | `lessonId` of the work item from [`core/app/darbai`](#get-core-app-darbai) |
| `Atliktas` | The new state: `true` to mark done, `false` to unmark. Retrofit serializes it as the text `true` or `false` |

The request sets an explicit state; it is not a toggle. Completion is read back through the work item's `completionDate`: non-null means done, null means not done. The app's "completed" and "uncompleted" filters use that field locally. There is no separate completion flag. The response is a plain `StatusResponse` with no payload. See [homework completion](workflows.md#homework-completion) for the full flow and an example request.

Not tested. The client only shows the checkbox to accounts whose login `role` is `2` (a student's own login). Whether the server rejects parent roles, other students' IDs, or classwork lesson IDs is unknown.

Evidence: Static only. Client declaration: `ye.p.d` in build 4.17. Call sites: `af.j2` (work repository), `lt.zet.tamo.models.view.WorkViewModel`, `gf.b0` (work list adapter).

Response type: `StatusResponse`.

Models: [response.StatusResponse](models/response.md#statusresponse).

Request content type: `application/x-www-form-urlencoded`.

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| header | `x-selected-role` | `String` |
| form | `MokinioId` | `long` |
| form | `PamokosId` | `long` |
| form | `Atliktas` | `boolean` |

<a id="post-core-app-devices-installation"></a>

## POST core/app/devices/installation

Registers a Firebase installation and FCM token. The JSON body is `{"Installation":{"Id":"<FID>","DeviceId":"<FCM token>"}}`. This changes registration state; it was not tested.

Evidence: Static only. Client declaration: `ye.p.b` in build 4.17.

Response: an HTTP response with no typed body. No JSON payload schema is declared for this operation.

Request content type: `application/json; charset=UTF-8`.

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| body | `(whole JSON body)` | `InstallationRequest` |

<a id="delete-core-app-devices-installation-installationid"></a>

## DELETE core/app/devices/installation/{installationId}

Removes a push installation. The path value is the Firebase Installation ID, not the FCM token. Not tested.

Evidence: Static only. Client declaration: `ye.p.e` in build 4.17.

Response: an HTTP response with no typed body. No JSON payload schema is declared for this operation.

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
| path | `installationId` | `String` |

<a id="post-core-app-utilities-sendnotification"></a>

## POST core/app/utilities/sendnotification

Triggers a test notification. No request body is declared. The app's 60-second UI cooldown is not proof of a server rate limit.

Evidence: Static only. Client declaration: `ye.p.h` in build 4.17.

Response type: `StatusResponse`.

Models: [response.StatusResponse](models/response.md#statusresponse).

| Location | Name | Client type |
| --- | --- | --- |
| header | `Authorization` | `String` |
