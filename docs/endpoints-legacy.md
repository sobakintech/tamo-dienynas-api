# Legacy API endpoints

[Overview](../README.md) | [Authentication](authentication.md) | [Models](models/README.md) | [Validation](validation.md)

Base URL: `https://dienynas.tamo.lt/MobileServiceV3/`.

All 28 fixed operations are listed below. Authenticated GETs send `authToken` in the query. JSON/form operations place credentials as explicitly shown. A modern Bearer header is not declared on this service. Typed bodies use `BaseResponse<T>`; `T` is the value inside `Result`.

**Several GET routes change state.** In particular, do not treat impersonation, logout, payment creation, read-marking, or deletion as read-only.

| Method | Route | Operation | Evidence |
| --- | --- | --- | --- |
| POST | [`AuthenticateV2`](#post-authenticatev2) | Authentication | Paid baseline: success |
| GET | [`GetSubscriptionType`](#get-getsubscriptiontype) | Read-oriented | Paid baseline: success |
| GET | [`GetUserSubscriptions`](#get-getusersubscriptions) | Read-oriented | Paid baseline: success |
| GET | [`GetProducts`](#get-getproducts) | Read-oriented | Paid baseline: success |
| GET | [`GetGlobalSettings`](#get-getglobalsettings) | Read-oriented | Paid baseline: success |
| GET | [`GetAdditionalMenu`](#get-getadditionalmenu) | Read-oriented | Paid baseline: success |
| GET | [`GetWindowFilters`](#get-getwindowfilters) | Read-oriented | Static only |
| GET | [`GetAssessments`](#get-getassessments) | Read-oriented | Paid baseline: success |
| GET | [`GetAwards`](#get-getawards) | Read-oriented | Paid baseline: success |
| GET | [`GetLessons`](#get-getlessons) | Read-oriented | Paid baseline: success |
| GET | [`GetNextEvents`](#get-getnextevents) | Read-oriented | Paid baseline: success |
| GET | [`GetSchedule`](#get-getschedule) | Read-oriented | Paid baseline: success |
| GET | [`GetPeriodAssessments`](#get-getperiodassessments) | Read-oriented | Static only |
| GET | [`GetRatingSubjects`](#get-getratingsubjects) | Read-oriented | Paid baseline: success |
| GET | [`GetRatings`](#get-getratings) | Read-oriented | Static only |
| GET | [`GetReceivedMessageHeaders`](#get-getreceivedmessageheaders) | Read-oriented | Paid baseline: HTTP 404 |
| GET | [`GetSendMessageHeaders`](#get-getsendmessageheaders) | Read-oriented | Paid baseline: HTTP 404 |
| GET | [`GetMessage`](#get-getmessage) | Read; side effects unverified | Static only |
| GET | [`GetRecipients`](#get-getrecipients) | Read-oriented | Static only |
| GET | [`GetMessageFiles`](#get-getmessagefiles) | Read-oriented | Static only |
| GET | [`GetFileUrl`](#get-getfileurl) | Read-oriented | Static only |
| POST | [`SaveMessage`](#post-savemessage) | Changes state | Static only |
| POST | [`AttachMessageFile`](#post-attachmessagefile) | Changes state | Static only |
| GET | [`SetMessageRead`](#get-setmessageread) | Changes state | Static only |
| GET | [`DeleteMessage`](#get-deletemessage) | Changes state | Static only |
| GET | [`CreatePayment`](#get-createpayment) | Changes state | Static only |
| GET | [`Impersonate`](#get-impersonate) | Changes state | Static only |
| GET | [`Logout`](#get-logout) | Changes state | Static only |

Live success is limited to the tested account and parameters, not every role, date range, or subscription state. Read-oriented describes the client's intent, not a guarantee of zero internal server effects.

<a id="post-authenticatev2"></a>

## POST AuthenticateV2

JSON fields and a complete request example are in [authentication](authentication.md). Login can create a session; it is not a read operation.

Evidence: Paid baseline: success. Client declaration: `ye.g0.w` in build 4.17.

Response type: `BaseResponse<AuthResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.AuthResponse](models/response.md#authresponse).

Request content type: `application/json; charset=UTF-8`.

| Location | Name | Client type |
| --- | --- | --- |
| body | `(whole JSON body)` | `Auth` |

<a id="get-getsubscriptiontype"></a>

## GET GetSubscriptionType

`Result.TypeName == "free"` bypasses the app's paid-subscription lookup. This is a server classification, not a client-controlled free-access flag. See [premium](premium.md).

Evidence: Paid baseline: success. Client declaration: `ye.g0.m` in build 4.17.

Response type: `BaseResponse<SubscriptionTypeResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.SubscriptionTypeResponse](models/response.md#subscriptiontyperesponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |

<a id="get-getusersubscriptions"></a>

## GET GetUserSubscriptions

Subscription activity uses `subscrStatus == "active"` and `dateActive == 1`. `showStartTrial == 1` selects the client trial state.

Evidence: Paid baseline: success. Client declaration: `ye.g0.f` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Subscription>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [other.Subscription](models/other.md#subscription).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |

<a id="get-getproducts"></a>

## GET GetProducts

Reads product/pricing information. Prices in live responses can change; none are published here.

Evidence: Paid baseline: success. Client declaration: `ye.g0.r` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Product>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [other.Product](models/other.md#product).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |

<a id="get-getglobalsettings"></a>

## GET GetGlobalSettings

Repeat `paramKeys` for multiple keys. The baseline requested only `premium_headertxt` and `premium_days`. Other settings are listed in [workflows](workflows.md#subscriptions-and-payments).

Evidence: Paid baseline: success. Client declaration: `ye.g0.y` in build 4.17.

Response type: `BaseResponse<SettingsResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.SettingsResponse](models/response.md#settingsresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `paramKeys` | `List<String>` |

<a id="get-getadditionalmenu"></a>

## GET GetAdditionalMenu

Observed location: `MoreWnd.BelowStatic`. Returned links can target web pages or other origins; the baseline did not follow them.

Evidence: Paid baseline: success. Client declaration: `ye.g0.i` in build 4.17.

Response type: `BaseResponse<MenuGroupResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.MenuGroupResponse](models/response.md#menugroupresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `location` | `String` |

<a id="get-getwindowfilters"></a>

## GET GetWindowFilters

Known `windowName` values: `remarks`, `diary`, `nextevents`, `homework`, `lessons`, `messages`, `periods`, `schedule`. The app's message branch uses local filter data instead. `userType` is a string; a complete accepted-value set was not established.

Evidence: Static only. Client declaration: `ye.g0.A` in build 4.17.

Response type: `BaseResponse<FiltersResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.FiltersResponse](models/response.md#filtersresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `windowName` | `String` |
| query | `userType` | `String` |

<a id="get-getassessments"></a>

## GET GetAssessments

Reads legacy assessment/attendance items for a date range. The `realm.Assessment` model includes derived/cache fields as well as response data.

Evidence: Paid baseline: success. Client declaration: `ye.g0.h` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Assessment>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Assessment](models/realm.md#assessment).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getawards"></a>

## GET GetAwards

Reads legacy award/remark items for a date range.

Evidence: Paid baseline: success. Client declaration: `ye.g0.b` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Award>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Award](models/realm.md#award).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getlessons"></a>

## GET GetLessons

Returns legacy lesson data, including `subjectId`, `subjectName`, `teacherName`, and `subjectTheme`. Actual availability of each field can vary.

Evidence: Paid baseline: success. Client declaration: `ye.g0.o` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Lesson>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Lesson](models/realm.md#lesson).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getnextevents"></a>

## GET GetNextEvents

Reads dated event items. This is not the modern calendar-week endpoint.

Evidence: Paid baseline: success. Client declaration: `ye.g0.s` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Event>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Event](models/realm.md#event).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getschedule"></a>

## GET GetSchedule

Person-scoped schedule lookup. The paid baseline used a `personId` returned for the authenticated account.

Evidence: Paid baseline: success. Client declaration: `ye.g0.d` in build 4.17.

Response type: `BaseResponse<ItemsResponse<ScheduleDay>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.ScheduleDay](models/realm.md#scheduleday).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `personId` | `long` |
| query | `dateFrom` | `String` |

<a id="get-getperiodassessments"></a>

## GET GetPeriodAssessments

Requires a person and period ID from legitimate account context. No guessed IDs or live requests were used for this route.

Evidence: Static only. Client declaration: `ye.g0.l` in build 4.17.

Response type: `BaseResponse<ItemsResponse<PeriodAssessment>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.PeriodAssessment](models/realm.md#periodassessment).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `personId` | `long` |
| query | `periodId` | `long` |

<a id="get-getratingsubjects"></a>

## GET GetRatingSubjects

Lists subjects for ratings for a specified person. The paid baseline used an identifier returned for the authenticated account.

Evidence: Paid baseline: success. Client declaration: `ye.g0.C` in build 4.17.

Response type: `BaseResponse<ItemsResponse<RatingSubjects>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.RatingSubjects](models/realm.md#ratingsubjects).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `personId` | `long` |

<a id="get-getratings"></a>

## GET GetRatings

Requires `subjectId` as a numeric value here. Other routes use string subject/file identifiers; do not assume all IDs share a type.

Evidence: Static only. Client declaration: `ye.g0.k` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Rating>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Rating](models/realm.md#rating).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `personId` | `long` |
| query | `subjectId` | `long` |

<a id="get-getreceivedmessageheaders"></a>

## GET GetReceivedMessageHeaders

Returned HTTP 404 with a non-JSON body in the paid baseline. This does not prove global removal or a premium restriction.

Evidence: Paid baseline: HTTP 404. Client declaration: `ye.g0.a` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Message>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Message](models/realm.md#message).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getsendmessageheaders"></a>

## GET GetSendMessageHeaders

The recovered spelling is `GetSendMessageHeaders`, not `GetSentMessageHeaders`. Returned HTTP 404 in the paid baseline.

Evidence: Paid baseline: HTTP 404. Client declaration: `ye.g0.z` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Message>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Message](models/realm.md#message).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `dateFrom` | `String` |
| query | `dateTo` | `String` |

<a id="get-getmessage"></a>

## GET GetMessage

Not tested. Opening a message might have implicit server-side effects even though a separate read-marking endpoint exists.

Evidence: Static only. Client declaration: `ye.g0.x` in build 4.17.

Response type: `BaseResponse<Message>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [realm.Message](models/realm.md#message).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `messageId` | `long` |

<a id="get-getrecipients"></a>

## GET GetRecipients

Contact/recipient listing. `personId` is boxed/optional and can be omitted; the other declared parameters are shown below. Accepted `groupType` values were not exhaustively established. Not tested.

Evidence: Static only. Client declaration: `ye.g0.v` in build 4.17.

Response type: `BaseResponse<ItemsResponse<Contact>>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ItemsResponse](models/response.md#itemsresponse), [realm.Contact](models/realm.md#contact).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `groupType` | `String` |
| query | `personId` | `Long` |

<a id="get-getmessagefiles"></a>

## GET GetMessageFiles

Returns `fileName`, `fileType`, and `fileBody`. `bs` means Base64; `aws` means a URL. No message files were retrieved.

Evidence: Static only. Client declaration: `ye.g0.B` in build 4.17.

Response type: `BaseResponse<FileResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.FileResponse](models/response.md#fileresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `messageId` | `long` |
| query | `fileId` | `long` |

<a id="get-getfileurl"></a>

## GET GetFileUrl

Returns a download URL for string `fileId`. Not live-tested. Do not add the Tamo token to arbitrary returned hosts.

Evidence: Static only. Client declaration: `ye.g0.n` in build 4.17.

Response type: `BaseResponse<UrlResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.UrlResponse](models/response.md#urlresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `fileId` | `String` |

<a id="post-savemessage"></a>

## POST SaveMessage

Sends a message. The native flow calls it once per selected recipient. `recipientGroup` and `recipientPersonId` come from that recipient's `groupName` and `personId` in [`GetRecipients`](#get-getrecipients). If there are attachments, the app then calls [`AttachMessageFile`](#post-attachmessagefile) with the returned `Message.messageId`. Attachments are only sent when the envelope reports success. No sending example or live write is included.

Evidence: Static only. Client declaration: `ye.g0.u` in build 4.17. Call sites: `ye.o`, `ff.x2` (compose screen).

Response type: `BaseResponse<Message>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [realm.Message](models/realm.md#message).

Request content type: `application/x-www-form-urlencoded`.

| Location | Name | Client type |
| --- | --- | --- |
| form | `authToken` | `String` |
| form | `recipientGroup` | `String` |
| form | `recipientPersonId` | `long` |
| form | `subject` | `String` |
| form | `body` | `String` |

<a id="post-attachmessagefile"></a>

## POST AttachMessageFile

Uploads a Base64-encoded attachment in JSON, not multipart form data. No upload, quota, storage-ownership, or unlimited-upload claim was tested.

Evidence: Static only. Client declaration: `ye.g0.j` in build 4.17.

Response type: `BaseResponse`.

Models: [response.BaseResponse](models/response.md#baseresponse).

Request content type: `application/json; charset=UTF-8`.

| Location | Name | Client type |
| --- | --- | --- |
| body | `(whole JSON body)` | `AttachFile` |

<a id="get-setmessageread"></a>

## GET SetMessageRead

Marks a message read. This is a mutation despite using GET.

The app calls it automatically when an unread message is opened, after loading it with `GetMessage`. It sends the message's server `messageId`, not the local Realm `id`. The client checks only the envelope and does not read `isRead`. On success it updates its local copy and decrements its unread counter.

Evidence: Static only. Client declaration: `ye.g0.e` in build 4.17. Call sites: `ze.f4`, `ff.l3` (message view).

Response type: `BaseResponse<SetReadResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.SetReadResponse](models/response.md#setreadresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `messageId` | `long` |

<a id="get-deletemessage"></a>

## GET DeleteMessage

Deletes a message. This is a mutation despite using GET.

The app calls it from the open message's delete action with the server `messageId`. The client checks only the envelope and does not read `isDeleted`. On success it removes the local copy. Whether deletion is per-user, recoverable, or also affects the other party is unknown.

Evidence: Static only. Client declaration: `ye.g0.g` in build 4.17. Call sites: `ze.f4`, `ff.l3` (message view).

Response type: `BaseResponse<DeleteResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.DeleteResponse](models/response.md#deleteresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `messageId` | `long` |

<a id="get-createpayment"></a>

## GET CreatePayment

Creates a payment/order. Never call this as a harmless price lookup. No payment was created during validation.

`prodId` and `prodPriceId` come from a `Product` returned by [`GetProducts`](#get-getproducts). The result's `orderId` is used in the SMS payment flow: the app composes an SMS containing the product description followed by the order ID, addressed to the product's `smsNumber`. See [subscriptions and payments](workflows.md#subscriptions-and-payments) for the error messages the app recognizes.

Evidence: Static only. Client declaration: `ye.g0.q` in build 4.17. Call sites: `lt.zet.tamo.ui.subscription.p1` and `lt.zet.tamo.ui.subscription.s`.

Response type: `BaseResponse<PaymentResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.PaymentResponse](models/response.md#paymentresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `prodId` | `long` |
| query | `prodPriceId` | `long` |

<a id="get-impersonate"></a>

## GET Impersonate

An account-changing operation in the privileged login flow. Its presence does not grant permission to impersonate other users. Not tested.

The app only offers it after a login that returns `role == 3`. On success, the app replaces its stored token, person, role, and access level with the returned values. If the server answers `This function requires the Administrator role.`, the app logs out.

Evidence: Static only. Client declaration: `ye.g0.p` in build 4.17. Call sites: `lt.zet.tamo.ui.login.LoginActivity`, `lt.zet.tamo.ui.login.ImpersonateActivity`.

Response type: `BaseResponse<ImpersonateResponse>`.

Models: [response.BaseResponse](models/response.md#baseresponse), [response.ImpersonateResponse](models/response.md#impersonateresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |
| query | `userName` | `String` |
| query | `accessLevel` | `int` |

<a id="get-logout"></a>

## GET Logout

Invalidates/logs out the session according to the app workflow. GET does not make this read-only. Server revocation behavior was not tested.

Evidence: Static only. Client declaration: `ye.g0.t` in build 4.17.

Response type: `BaseResponse`.

Models: [response.BaseResponse](models/response.md#baseresponse).

| Location | Name | Client type |
| --- | --- | --- |
| query | `authToken` | `String` |

## Dynamic download method

The interface also declares a GET with a complete URL supplied at runtime, returning raw response bytes. It has no fixed path and no declared auth parameter. This is the 44th Retrofit method, not another known server route. See [file downloads](workflows.md#files-and-attachments) for credential and host handling.
