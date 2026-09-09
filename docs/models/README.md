# Response and request models

This reference covers 114 client model/support classes and 559 direct fields recovered from Android build 4.17. Original DEX field names and explicit serialization aliases were checked independently. No proprietary source code is included.

These are the structures the client knows about, not an exhaustive server schema. Live responses contained additional fields, and some successful lists were empty. Requiredness, general nullability, and all response alternatives remain unknown.

| Group | Contents | Classes |
| --- | --- | ---: |
| [response](response.md) | Service envelopes and payload wrappers. | 32 |
| [request](request.md) | JSON request bodies and related request objects. | 5 |
| [data](data.md) | Models used primarily by the modern service. | 24 |
| [other](other.md) | Supporting models, including subscriptions, menus, products, and local helper objects. | 18 |
| [realm](realm.md) | Models stored by the app in Realm. | 28 |
| [state](state.md) | Local client state, included to explain subscription handling. | 1 |
| [style](style.md) | StyleRef and five local rendering helpers. | 6 |

## Reading the types

- `String`, `boolean`, integer, and numeric fields describe client-side representations. Do not infer a mandatory field from a Java primitive.
- `long` may require 64-bit integer handling. JavaScript consumers should preserve large IDs without rounding.
- `List<T>` and `RealmList<T>` represent collections. A Realm collection does not mean every contained property originated on the server.
- `Date`, `LocalDate`, `LocalDateTime`, and `ZonedDateTime` are parsed values. See [dates and serialization](../protocol.md#dates-and-serialization) before choosing a JSON date parser.
- `Type` and `T` are generic placeholders for the payload declared by an endpoint.
- `Object` and map-like values are intentionally unspecified. Do not invent their nested structure.
- Names such as `data.Event` and `realm.Event` are different types. The reference column resolves model names using client imports where possible.

## Common entry points

| Purpose | Model |
| --- | --- |
| Legacy success/error envelope | [BaseResponse](response.md#baseresponse) |
| Modern success/error fields | [StatusResponse](response.md#statusresponse) |
| Login result | [AuthResponse](response.md#authresponse) |
| Role selection | [Role](data.md#role) |
| Modern diary | [DienynasResponse](response.md#dienynasresponse) |
| Modern homework/classwork | [WorkResponse](response.md#workresponse) |
| Calendar week | [DayEventsResponse](response.md#dayeventsresponse) |
| Legacy collections | [ItemsResponse](response.md#itemsresponse) |
| Subscription records | [Subscription](other.md#subscription) |

## Model index

### response

[Agenda](response.md#agenda) · [AgendaDay](response.md#agendaday) · [AllDayEventsResponse](response.md#alldayeventsresponse) · [AuthResponse](response.md#authresponse) · [BaseResponse](response.md#baseresponse) · [DayBadgesResponse](response.md#daybadgesresponse) · [DayEventsResponse](response.md#dayeventsresponse) · [DeleteResponse](response.md#deleteresponse) · [DienynasResponse](response.md#dienynasresponse) · [FeedsResponse](response.md#feedsresponse) · [FileResponse](response.md#fileresponse) · [FileUrlResponse](response.md#fileurlresponse) · [FiltersResponse](response.md#filtersresponse) · [GlobalSettingsResponse](response.md#globalsettingsresponse) · [ImpersonateResponse](response.md#impersonateresponse) · [ItemsResponse](response.md#itemsresponse) · [MenuGroupResponse](response.md#menugroupresponse) · [Notification](response.md#notification) · [NotificationData](response.md#notificationdata) · [PaymentResponse](response.md#paymentresponse) · [PeriodSummaryResponse](response.md#periodsummaryresponse) · [PushTagResponse](response.md#pushtagresponse) · [SetReadResponse](response.md#setreadresponse) · [SettingsResponse](response.md#settingsresponse) · [StatusResponse](response.md#statusresponse) · [StyleRefResponse](response.md#stylerefresponse) · [SubscriptionTypeResponse](response.md#subscriptiontyperesponse) · [TokenCodeResponse](response.md#tokencoderesponse) · [UnreadResponse](response.md#unreadresponse) · [UrlResponse](response.md#urlresponse) · [UserResponse](response.md#userresponse) · [WorkResponse](response.md#workresponse)

### request

[AttachFile](request.md#attachfile) · [Auth](request.md#auth) · [Installation](request.md#installation) · [InstallationRequest](request.md#installationrequest) · [Request](request.md#request)

### data

[Analytics](data.md#analytics) · [AssessmentInfo](data.md#assessmentinfo) · [Calculator](data.md#calculator) · [Content](data.md#content) · [DayBadge](data.md#daybadge) · [DayEvents](data.md#dayevents) · [Event](data.md#event) · [EventDetails](data.md#eventdetails) · [FeedItem](data.md#feeditem) · [FeedItemDetails](data.md#feeditemdetails) · [File](data.md#file) · [FormativeGrade](data.md#formativegrade) · [FormativeGroup](data.md#formativegroup) · [Grade](data.md#grade) · [GradeGroup](data.md#gradegroup) · [LegacyFile](data.md#legacyfile) · [Message](data.md#message) · [Period](data.md#period) · [PeriodSummary](data.md#periodsummary) · [References](data.md#references) · [Role](data.md#role) · [Stat](data.md#stat) · [UserInfo](data.md#userinfo) · [Work](data.md#work)

### other

[Attachment](other.md#attachment) · [Badge](other.md#badge) · [DataStoreResponse](other.md#datastoreresponse) · [DownloadableFile](other.md#downloadablefile) · [Filter](other.md#filter) · [FilterOptions](other.md#filteroptions) · [KeyValue](other.md#keyvalue) · [Language](other.md#language) · [LocalContact](other.md#localcontact) · [MenuGroup](other.md#menugroup) · [MenuItem](other.md#menuitem) · [MoreItem](other.md#moreitem) · [PaymentButton](other.md#paymentbutton) · [Product](other.md#product) · [r](other.md#r) · [RatingItem](other.md#ratingitem) · [Sms](other.md#sms) · [Subscription](other.md#subscription)

### realm

[Assessment](realm.md#assessment) · [Award](realm.md#award) · [Child](realm.md#child) · [Contact](realm.md#contact) · [Event](realm.md#event) · [File](realm.md#file) · [FilterGroup](realm.md#filtergroup) · [FilterItem](realm.md#filteritem) · [Lesson](realm.md#lesson) · [Mark](realm.md#mark) · [Message](realm.md#message) · [Notification](realm.md#notification) · [NotificationData](realm.md#notificationdata) · [Period](realm.md#period) · [PeriodAssessment](realm.md#periodassessment) · [Rating](realm.md#rating) · [RatingData](realm.md#ratingdata) · [RatingSubjectData](realm.md#ratingsubjectdata) · [RatingSubjects](realm.md#ratingsubjects) · [RealmAttachment](realm.md#realmattachment) · [RealmReadNotification](realm.md#realmreadnotification) · [RealmString](realm.md#realmstring) · [ReceivedMessageHeader](realm.md#receivedmessageheader) · [ScheduleDay](realm.md#scheduleday) · [ScheduleSubject](realm.md#schedulesubject) · [SentMessageHeader](realm.md#sentmessageheader) · [User](realm.md#user) · [Work](realm.md#work)

### state

[SubscriptionState](state.md#subscriptionstate)

### style

[Defaults](style.md#defaults) · [Stylable](style.md#stylable) · [Style](style.md#style) · [StyleableContent](style.md#styleablecontent) · [StyleRef](style.md#styleref) · [StyleUtils](style.md#styleutils)
