# Response models

[Model index](README.md) | [API reference](../../README.md)

Service envelopes and payload wrappers. Modern payloads inherit `StatusResponse`; legacy payloads sit inside `BaseResponse.Result`. A response class in the app does not by itself establish a reachable endpoint.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## Agenda

Client symbol: `lt.zet.tamo.models.response.Agenda`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `currentDateTime` | `ZonedDateTime` |  |
| `description` | `String` |  |
| `end` | `ZonedDateTime` |  |
| `header` | `String` |  |
| `id` | `long` |  |
| `number` | `String` |  |
| `start` | `ZonedDateTime` |  |
| `title` | `String` |  |

## AgendaDay

Client symbol: `lt.zet.tamo.models.response.AgendaDay`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `date` | `LocalDate` |  |
| `indicators` | `List<String>` |  |
| `label` | `String` |  |

## AllDayEventsResponse

Client symbol: `lt.zet.tamo.models.response.AllDayEventsResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `allDayEvents` | `List<Event>` | [data.Event](data.md#event) |

## AuthResponse

Client symbol: `lt.zet.tamo.models.response.AuthResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `accessLevel` | `int` |  |
| `authToken` | `String` |  |
| `children` | `List<Child>` | [realm.Child](realm.md#child) |
| `firstName` | `String` |  |
| `lastName` | `String` |  |
| `personId` | `int` |  |
| `role` | `int` |  |
| `userRoleIsAllowed` | `boolean` |  |

## BaseResponse

Client symbol: `lt.zet.tamo.models.response.BaseResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `ErrorCode` | `int` |  |
| `ErrorMessage` | `String` |  |
| `Result` | `Type` |  |
| `Status` | `int` |  |

## DayBadgesResponse

Client symbol: `lt.zet.tamo.models.response.DayBadgesResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `days` | `List<DayBadge>` | [data.DayBadge](data.md#daybadge) |

## DayEventsResponse

Client symbol: `lt.zet.tamo.models.response.DayEventsResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `days` | `List<DayEvents>` | [data.DayEvents](data.md#dayevents) |
| `formatives` | `List<FormativeGroup>` | [data.FormativeGroup](data.md#formativegroup) |
| `grades` | `List<GradeGroup>` | [data.GradeGroup](data.md#gradegroup) |

## DeleteResponse

Client symbol: `lt.zet.tamo.models.response.DeleteResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `isDeleted` | `boolean` |  |

## DienynasResponse

Client symbol: `lt.zet.tamo.models.response.DienynasResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `formativeGrades` | `List<FormativeGrade>` | [data.FormativeGrade](data.md#formativegrade) |
| `items` | `List<AssessmentInfo>` | [data.AssessmentInfo](data.md#assessmentinfo) |

## FeedsResponse

Client symbol: `lt.zet.tamo.models.response.FeedsResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `result` | `List<FeedItem>` | [data.FeedItem](data.md#feeditem) |

## FileResponse

Client symbol: `lt.zet.tamo.models.response.FileResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `fileBody` | `String` |  |
| `fileName` | `String` |  |
| `fileType` | `String` |  |

## FileUrlResponse

Client symbol: `lt.zet.tamo.models.response.FileUrlResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `url` | `String` |  |

## FiltersResponse

Client symbol: `lt.zet.tamo.models.response.FiltersResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `groups` | `RealmList<FilterGroup>` | [realm.FilterGroup](realm.md#filtergroup) |

## GlobalSettingsResponse

Client symbol: `lt.zet.tamo.models.response.GlobalSettingsResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `settings` | `List<KeyValue>` | [other.KeyValue](other.md#keyvalue) |

## ImpersonateResponse

Client symbol: `lt.zet.tamo.models.response.ImpersonateResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `accessLevel` | `int` |  |
| `allowed` | `int` |  |
| `authToken` | `String` |  |
| `children` | `List<Child>` | [realm.Child](realm.md#child) |
| `firstName` | `String` |  |
| `lastName` | `String` |  |
| `personId` | `int` |  |
| `role` | `int` |  |

## ItemsResponse

Client symbol: `lt.zet.tamo.models.response.ItemsResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Items` | `List<Type>` |  |
| `items` | `List<Type>` |  |

## MenuGroupResponse

Client symbol: `lt.zet.tamo.models.response.MenuGroupResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `menuGroups` | `List<MenuGroup>` | [other.MenuGroup](other.md#menugroup) |

## Notification

Client symbol: `lt.zet.tamo.models.response.Notification`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `FeedEventParam` | `NotificationData` | [response.NotificationData](response.md#notificationdata) |
| `Stamp` | `String` |  |
| `EventId` | `int` |  |
| `FeedsId` | `long` |  |
| `Operation` | `int` |  |

## NotificationData

Client symbol: `lt.zet.tamo.models.response.NotificationData`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Date` | `String` |  |
| `Description` | `String` |  |
| `HomeWork` | `String` |  |
| `Location` | `String` |  |
| `MessageLink` | `String` |  |
| `PictureLink` | `String` |  |
| `Pupil` | `String` |  |
| `ThingName` | `String` |  |
| `Text` | `String` |  |
| `Type` | `int` |  |
| `Value` | `int` |  |

## PaymentResponse

Client symbol: `lt.zet.tamo.models.response.PaymentResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `prodCode` | `String` |  |
| `orderId` | `long` |  |

## PeriodSummaryResponse

Client symbol: `lt.zet.tamo.models.response.PeriodSummaryResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `periods` | `List<PeriodSummary>` | [data.PeriodSummary](data.md#periodsummary) |
| `title` | `String` |  |

## PushTagResponse

Client symbol: `lt.zet.tamo.models.response.PushTagResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `channels` | `List<String>` |  |

## SetReadResponse

Client symbol: `lt.zet.tamo.models.response.SetReadResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `isRead` | `boolean` |  |

## SettingsResponse

Client symbol: `lt.zet.tamo.models.response.SettingsResponse`.

Parent: `ItemsResponse<KeyValue>` ([response.ItemsResponse](response.md#itemsresponse), [other.KeyValue](other.md#keyvalue)).

| Field | Client type | Referenced models |
| --- | --- | --- |

No direct fields; see the parent type.

## StatusResponse

Client symbol: `lt.zet.tamo.models.response.StatusResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `errors` | `List<String>` |  |
| `isSuccess` | `boolean` |  |
| `message` | `String` |  |

## StyleRefResponse

Client symbol: `lt.zet.tamo.models.response.StyleRefResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `styleRef` | `List<StyleRef>` | [lt.zet.tamo.utils.style.StyleRef](style.md#styleref) |

## SubscriptionTypeResponse

Client symbol: `lt.zet.tamo.models.response.SubscriptionTypeResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `TypeName` | `String` |  |

## TokenCodeResponse

Client symbol: `lt.zet.tamo.models.response.TokenCodeResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `tokenCode` | `String` |  |

## UnreadResponse

Client symbol: `lt.zet.tamo.models.response.UnreadResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `value` | `int` |  |

## UrlResponse

Client symbol: `lt.zet.tamo.models.response.UrlResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `url` | `String` |  |

## UserResponse

Client symbol: `lt.zet.tamo.models.response.UserResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `roles` | `List<Role>` | [data.Role](data.md#role) |
| `userInfo` | `UserInfo` | [data.UserInfo](data.md#userinfo) |

## WorkResponse

Client symbol: `lt.zet.tamo.models.response.WorkResponse`.

Parent: `StatusResponse` ([response.StatusResponse](response.md#statusresponse)).

| Field | Client type | Referenced models |
| --- | --- | --- |
| `items` | `List<Work>` | [data.Work](data.md#work) |
