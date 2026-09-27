# API workflows

[Overview](../README.md) | [Modern routes](endpoints-modern.md) | [Legacy routes](endpoints-legacy.md)

The workflows below are reconstructed from the Android client. Unless a result is listed in [validation](validation.md), it is static-only. Request shapes containing placeholders are illustrative and are not live account data.

## Diary, homework, and calendar

After login, obtain a role from `core/app/roles` and use its `id` in `x-selected-role`.

| View | Request | Payload |
| --- | --- | --- |
| Diary/assessments | `GET core/app/dienynas?dateFrom=...&dateTo=...` | `items`, `formativeGrades` |
| Homework | `GET core/app/darbai?dateFrom=...&dateTo=...&workType=home` | `items` |
| Classwork | Same route with `workType=class` | `items` |
| Calendar badges | `GET core/app/calendar/badges?dateFrom=...&dateTo=...` | `days` |
| All-day events | `GET core/app/calendar/events/allDay?dateFrom=...&dateTo=...` | `allDayEvents` |
| Calendar week | `GET v2/app/calendar/events?date=...` | `days`, `grades`, `formatives` |
| Event period summary | `GET core/app/analytics/periodsummary?eventSid=...` | `title`, `periods` |
| Feed | `GET core/app/feeds` | `result` |

Date queries use `YYYY-MM-DD`. The app aligns the week request to Monday, while badge/all-day repositories usually request a month. Start with a bounded date range rather than requesting all history. No pagination parameters, maximum date window, or rate limit were established by the recovered declarations.

The modern calendar separates event records from grade/formative collections and uses references to join them client-side. Period summaries take a string event SID, not a numeric lesson ID.

Modern content includes presentation-oriented objects such as `Content` and `StyleRef`. Labels, icons, styling, and actions can be driven by server data. A custom client should not assume every content string is plain text or every returned URL is a Tamo API path.

### Homework completion

Completion state is stored on the server. Ticking a homework item in the official app sends it to TAMO, and later homework reads return it. A client that only saves ticks locally will not sync with the official app or other devices.

**Reading.** Each item from `GET core/app/darbai` has a `completionDate`. A non-null value means the item is done. The app's completed/uncompleted filters check this field locally; the route has no completion filter parameter.

**Writing.** The app sends `POST core/app/darbai/namu/atlikimas` with URL-encoded form fields:

| Field | Source |
| --- | --- |
| `MokinioId` | Selected role's `studentId` from `core/app/roles` |
| `PamokosId` | The work item's `lessonId` |
| `Atliktas` | `true` to mark done, `false` to unmark |

Illustrative request with placeholder values:

```http
POST https://api.tamo.lt/core/app/darbai/namu/atlikimas
Accept: application/json
Authorization: Bearer <token>
x-selected-role: <Role.id>
Content-Type: application/x-www-form-urlencoded

MokinioId=<Role.studentId>&PamokosId=<Work.lessonId>&Atliktas=true
```

Success is the usual modern `isSuccess == true`. The response has no payload, so it does not return the new `completionDate`. Read the homework again to get the server's value.

Recovered client behavior:

- The checkbox appears only when the login `role` is `2`, which is a student's own account. Parent logins do not see it.
- The same list adapter serves classwork (`workType=class`), so a student can also tick classwork items. The request still goes to the `namu` (homework) route.
- `Atliktas` is an absolute state, not a toggle. Unticking sends `false`.
- The request is retried up to three times on failure, like other modern calls.
- After the call finishes, the app updates the displayed item even when the request failed. It sets `completionDate` to the device time for `true` and clears it for `false`. It matches the item by the work item's `studentId` and `lessonId`. A failed tick can therefore look saved until the next refresh.

A homework item is identified only by `lessonId` here. It is unknown what the server does when one lesson has several homework entries. It is also unknown whether it validates `MokinioId` against the token, how it sets `completionDate`, or whether it accepts classwork lesson IDs.

This is a write operation. It was not validated and is not implemented in the examples. Reading homework does not require calling it.

### Subject names and grouping

Legacy lesson models contain `subjectId`, `subjectName`, `teacherName`, and `subjectTheme`. Modern work items expose `lessonId` and `thingName`. These are useful inputs for joining records, but the app declarations do not establish a universal mapping between courses, teachers, timetable slots, and displayed subject groups.

Do not infer that two lessons with the same display name necessarily have the same underlying identity, or that every grade can be assigned to a distinct lesson. A client-side alias/grouping feature should preserve original identifiers and leave ambiguous records unresolved.

## Messages

The legacy interface declares separate received/sent header lists, individual messages, recipient lookup, read-marking, deletion, sending, and attachment operations. In the paid baseline, both header-list routes returned HTTP 404. No message body was opened and no message operation was changed.

The native send flow calls `SaveMessage` once per selected recipient, then calls `AttachMessageFile` for each attachment using the returned message ID. `SaveMessage` sends URL-encoded form fields `authToken`, `recipientGroup`, `recipientPersonId`, `subject`, and `body`. The recipient fields are the `groupName` and `personId` of a contact from `GetRecipients`. Attachments go to the `messageId` of the `Message` that `SaveMessage` returns. Replies prefill the body with the quoted original under a `<<<<< Jums rašė: >>>>>` line; this is client-side text, not a server reply-threading field.

`SetMessageRead` and `DeleteMessage` use GET despite changing state. Both take the server `messageId`, not the app's local Realm `id`. Opening an unread message in the app calls `GetMessage` and then `SetMessageRead` automatically. The separate read-marking route does not prove that `GetMessage` has no implicit read effects. Do not use message opening as a read-only availability probe.

The app also uses an authenticated messaging WebView. Successful mobile login or diary access does not prove that this web flow, its cookies, or all of its message routes work in another client.

## Files and attachments

### Legacy upload

`POST AttachMessageFile` sends JSON:

```json
{
  "authToken": "<token>",
  "messageId": 123,
  "fileName": "example.txt",
  "fileBody": "<Base64-encoded bytes>"
}
```

This is not multipart form data. The app's Android Base64 mode can produce line breaks, which JSON serialization escapes. Local attachment-selection size checks exist, but they do not establish a server maximum, quota, allowed file types, retention policy, or authorization boundary.

No upload was performed. The existence of this endpoint does not establish unlimited storage or unrestricted attachment access.

### Legacy retrieval

`GetMessageFiles` returns `fileName`, `fileType`, and `fileBody` inside the legacy envelope:

| `fileType` | Client interpretation |
| --- | --- |
| `bs` | Decode `fileBody` as Base64 and write a local file |
| `aws` | Treat `fileBody` as a download URL |
| Other values | No reliable alternative protocol established |

The interface's dynamic GET accepts a complete URL and returns raw bytes. It has no declared token header or query parameter, and the shared client has no global token injector. Credentials needed by a returned URL must already be carried by that URL or otherwise supplied by the server's download mechanism.

`GetFileUrl` is a separate legacy URL lookup using string `fileId`.

### Modern retrieval

`POST files/filedownloadurl` is a read-oriented URL lookup with form field `fileSid`, Bearer authentication, and the selected-role header. Its response contains `url`.

The app passes this URL to Android DownloadManager. That helper sets a destination/MIME type but does not add the Tamo Authorization or Cookie header. A separate WebView download path explicitly copies the relevant WebView cookie. These are different paths, not interchangeable authentication rules.

Final file hosts, URL signatures, expiry, redirect behavior, size limits, and access checks remain unverified. Do not forward a Tamo token to an arbitrary attachment host or treat a signed URL as public.

## Authenticated web navigation

Outside Retrofit, the app constructs:

```text
GET https://dienynas.tamo.lt/MobileServiceV3/NavigateDirect
    ?authtoken=<token>
    &hideMenuBar=true
    &childStudentId=<active role student ID>
    &url=<destination path and query>
```

Query values are URL-encoded. The token key is lowercase `authtoken`, unlike legacy `authToken`. The `url` value contains the destination path and query, not the destination hostname.

The client concatenates a question mark and the destination query directly. A missing query can therefore produce a literal `?null` suffix. A missing active role can similarly produce a literal `null` child value. These are recovered implementation details, not recommended values for a new client.

The server's redirect sequence, cookie names/attributes, session lifetime, and downloaded web scripts are outside the static APK evidence. A URL containing `/MobileService/NavigateClose` is recognized as a navigation-close sentinel; no separate API request to that path was established.

The default messaging entry is `https://dienynas.tamo.lt/goto/bendrauk`. Messaging navigation can add `messagingFolder`, `id`, and `messageTypeId` from filters or push data. Menu `doAuth` controls authenticated navigation versus direct loading. The `app_dourlauth_domains` setting influences navigation handling; a special substring check also exists for `tamo-prod.s3` hosts. Neither is a complete server authorization or safe-host policy.

The WebView enables JavaScript and file selection, so opening it can trigger requests and effects not represented by its initial URL. Web navigation was deliberately excluded from read-only validation.

## Menus and filters

`GetAdditionalMenu` is called with `location=MoreWnd.BelowStatic`. Menu groups can contain links, icons, and authentication flags. Validation read the menu response without following any link.

`GetWindowFilters` declares `windowName` and `userType`. Known window names are `remarks`, `diary`, `nextevents`, `homework`, `lessons`, `messages`, `periods`, and `schedule`. The message branch actually loads a packaged local filter asset instead of calling the route. The complete server-accepted `userType`/filter value sets remain unknown.

Legacy schedule/rating flows can issue person-scoped requests for multiple children and merge results locally. Only IDs from the authenticated account's legitimate context should be used.

## Subscriptions and payments

See [premium](premium.md) for the entitlement decision. The app obtains products/prices with `GetProducts`, creates an order through `CreatePayment`, and reads UI/payment configuration through `GetGlobalSettings`.

Recovered setting keys include:

```text
premium_headertxt
premium_days
premium_price
payment_option_desc
monthly_desc
msubscr_desc
payment_buttons
sms_price_desc
paybtn_title
web_payment_url
web_payment_end_text
app_dourlauth_domains
acc_not_approved
```

`CreatePayment` takes `prodId` and `prodPriceId` from a `Product` and returns an `orderId`. In the SMS flow, the app composes an SMS with the product description and that order ID to the product's `smsNumber`. The user then taps a button that rechecks the subscription. The app recognizes these `ErrorMessage` values:

| `ErrorMessage` | App reaction |
| --- | --- |
| `Subscribe bill has an active payment. Paying with another price or created by another user.` | Shows a payment-already-exists screen |
| `In the role lacks permission.` | Shows a screen for roles that cannot pay, such as a child account |
| Anything else | Generic error with retry |

The client can hand off to web payment pages or an SMS intent. Those destinations and any additional provider requests are not a fixed mobile API inventory. Payment creation, payment pages, SMS handoff, and purchase behavior were not tested. Do not call `CreatePayment` to display prices.

## Push registration

The app obtains a Firebase Installation ID and Firebase Cloud Messaging registration token, then sends:

```json
{
  "Installation": {
    "Id": "<Firebase Installation ID>",
    "DeviceId": "<FCM registration token>"
  }
}
```

The request is `POST core/app/devices/installation` with Bearer auth. `DeviceId` is the FCM token, not an Android hardware ID or ADB serial. A `PLATFORM="gcm"` constant exists in the model but is not a serialized request field.

The app caches registration state/time, requests registration if missing or older than one day, and registers again when the Firebase token callback runs. Deletion uses the installation ID in `DELETE core/app/devices/installation/{installationId}`. `POST core/app/utilities/sendnotification` triggers a test notification; the app UI applies a 60-second cooldown.

The notification service renders title/body and passes the data map into the launch intent. Message-related keys include `id`, `messagingFolder`, and `messageTypeId`. Firebase may handle background notifications before the app callback.

Registration and test notifications change state or cause an external effect. Neither was tested. The presence of a registration route is not proof that a token from an independently configured Firebase project will receive TAMO pushes. See [related services](integrations.md) for the distinction between TAMO authentication and Firebase tokens.

## Evidence

Build 4.17 symbols include `af.j0`, `af.j2`, `gf.b0`, `lt.zet.tamo.models.view.WorkViewModel`, `af.p0`, `af.u0`, `ye.o`, `ye.f0`, `of.l`, `df.j`, `lt.zet.tamo.ui.web.j`, and `lt.zet.tamo.fcm.TamoFcmListenerService`. The endpoint declarations are independently checked against DEX annotations; these workflow descriptions also use the recovered call sites. See [scope](scope.md).
