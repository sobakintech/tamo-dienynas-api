# Realm models

[Model index](README.md) | [API reference](../../README.md)

Models stored by the app in Realm. These combine fields read from legacy responses with derived/cache state. For example, `filterHash`, parsed dates, selection state, and local file paths are not automatically server fields. This is not a list of writable server properties.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## Assessment

Client symbol: `lt.zet.tamo.models.realm.Assessment`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `assessmentColor` | `String` |  |
| `assessmentType` | `String` |  |
| `assessmentValue` | `String` |  |
| `attendanceValue` | `String` |  |
| `dateAssessment` | `Date` |  |
| `dateAttendance` | `Date` |  |
| `dateSubject` | `Date` |  |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `assessmentDateTime` | `String` |  |
| `attendanceDateTime` | `String` |  |
| `subjectDate` | `String` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subject` | `String` |  |
| `themeLesson` | `String` |  |
| `type` | `int` |  |

## Award

Client symbol: `lt.zet.tamo.models.realm.Award`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateAward` | `Date` |  |
| `dateSubject` | `Date` |  |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `awardDateTime` | `String` |  |
| `subjectDate` | `String` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subject` | `String` |  |
| `teacherName` | `String` |  |
| `awardTypeName` | `String` |  |
| `awardValue` | `String` |  |

## Child

Client symbol: `lt.zet.tamo.models.realm.Child`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `childId` | `long` |  |
| `firstName` | `String` |  |
| `lastName` | `String` |  |

## Contact

Client symbol: `lt.zet.tamo.models.realm.Contact`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `childPersonId` | `Long` |  |
| `firstName` | `String` |  |
| `groupName` | `String` |  |
| `id` | `int` |  |
| `lastName` | `String` |  |
| `personId` | `long` |  |

## Event

Client symbol: `lt.zet.tamo.models.realm.Event`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateFrom` | `Date` |  |
| `dateTo` | `Date` |  |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `eventDateFrom` | `String` |  |
| `eventDateTo` | `String` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `eventBody` | `String` |  |
| `eventTime` | `String` |  |
| `eventTitle` | `String` |  |
| `eventType` | `int` |  |

## File

Client symbol: `lt.zet.tamo.models.realm.File`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `description` | `String` |  |
| `fileId` | `String` |  |
| `fileName` | `String` |  |
| `fileType` | `String` |  |

## FilterGroup

Client symbol: `lt.zet.tamo.models.realm.FilterGroup`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `collapsed` | `boolean` |  |
| `id` | `String` |  |
| `identifier` | `int` |  |
| `filteritems` | `RealmList<FilterItem>` | [realm.FilterItem](realm.md#filteritem) |
| `name` | `String` |  |
| `score` | `int` |  |
| `type` | `String` |  |

## FilterItem

Client symbol: `lt.zet.tamo.models.realm.FilterItem`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `String` |  |
| `identifier` | `int` |  |
| `name` | `String` |  |
| `selected` | `Boolean` |  |
| `type` | `String` |  |
| `values` | `RealmList<RealmString>` | [realm.RealmString](realm.md#realmstring) |

## Lesson

Client symbol: `lt.zet.tamo.models.realm.Lesson`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `classWork` | `String` |  |
| `dateAssign` | `Date` |  |
| `dateDeadline` | `Date` |  |
| `files` | `RealmList<File>` | [realm.File](realm.md#file) |
| `filterHash` | `long` |  |
| `homeWork` | `String` |  |
| `id` | `int` |  |
| `hwDeadline` | `String` |  |
| `subjectDate` | `String` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subjectName` | `String` |  |
| `subjectId` | `String` |  |
| `subjectTheme` | `String` |  |
| `teacherName` | `String` |  |

## Mark

Client symbol: `lt.zet.tamo.models.realm.Mark`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `isTest` | `boolean` |  |
| `value` | `double` |  |

## Message

Client symbol: `lt.zet.tamo.models.realm.Message`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `body` | `String` |  |
| `childPersonId` | `String` |  |
| `fileItems` | `RealmList<RealmAttachment>` | [realm.RealmAttachment](realm.md#realmattachment) |
| `filterHash` | `long` |  |
| `formattedDate` | `Date` |  |
| `from` | `String` |  |
| `hasAttachments` | `boolean` |  |
| `header` | `boolean` |  |
| `id` | `long` |  |
| `messageId` | `long` |  |
| `person` | `String` |  |
| `senderGroup` | `String` |  |
| `senderId` | `long` |  |
| `readStatus` | `boolean` |  |
| `sender` | `String` |  |
| `status` | `int` |  |
| `date` | `String` |  |
| `subject` | `String` |  |
| `to` | `String` |  |
| `type` | `int` |  |

## Notification

Client symbol: `lt.zet.tamo.models.realm.Notification`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `EventId` | `int` |  |
| `FeedsId` | `long` |  |
| `formattedDate` | `Date` |  |
| `formattedDateTime` | `Date` |  |
| `Operation` | `int` |  |
| `FeedEventParam` | `NotificationData` | [realm.NotificationData](realm.md#notificationdata) |
| `Stamp` | `String` |  |

## NotificationData

Client symbol: `lt.zet.tamo.models.realm.NotificationData`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Date` | `String` |  |
| `Description` | `String` |  |
| `HomeWork` | `String` |  |
| `Location` | `String` |  |
| `MessageLink` | `String` |  |
| `PictureLink` | `String` |  |
| `StudentFirstname` | `String` |  |
| `StudentId` | `long` |  |
| `StudentLastname` | `String` |  |
| `ThingName` | `String` |  |
| `Text` | `String` |  |
| `Type` | `String` |  |
| `Value` | `String` |  |

## Period

Client symbol: `lt.zet.tamo.models.realm.Period`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `int` |  |
| `periodtext` | `String` |  |
| `periodId` | `long` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |

## PeriodAssessment

Client symbol: `lt.zet.tamo.models.realm.PeriodAssessment`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `average` | `double` |  |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `main` | `String` |  |
| `mainForecast` | `String` |  |
| `mainForecastDesired` | `String` |  |
| `marks` | `RealmList<Mark>` | [realm.Mark](realm.md#mark) |
| `periodId` | `long` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subject` | `String` |  |
| `teacherName` | `String` |  |
| `TextMarks` | `RealmList<RealmString>` | [realm.RealmString](realm.md#realmstring) |
| `type` | `int` |  |

## Rating

Client symbol: `lt.zet.tamo.models.realm.Rating`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `int` |  |
| `current` | `int` |  |
| `ratingInfos` | `RealmList<RatingData>` | [realm.RatingData](realm.md#ratingdata) |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subjectId` | `long` |  |

## RatingData

Client symbol: `lt.zet.tamo.models.realm.RatingData`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `nr` | `int` |  |
| `value` | `String` |  |

## RatingSubjectData

Client symbol: `lt.zet.tamo.models.realm.RatingSubjectData`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Id` | `long` |  |
| `subject` | `String` |  |

## RatingSubjects

Client symbol: `lt.zet.tamo.models.realm.RatingSubjects`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `int` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `subjectsInfos` | `RealmList<RatingSubjectData>` | [realm.RatingSubjectData](realm.md#ratingsubjectdata) |

## RealmAttachment

Client symbol: `lt.zet.tamo.models.realm.RealmAttachment`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `FileId` | `long` |  |
| `messageId` | `long` |  |
| `FileName` | `String` |  |

## RealmReadNotification

Client symbol: `lt.zet.tamo.models.realm.RealmReadNotification`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `feedId` | `long` |  |

## RealmString

Client symbol: `lt.zet.tamo.models.realm.RealmString`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `name` | `String` |  |

## ReceivedMessageHeader

Client symbol: `lt.zet.tamo.models.realm.ReceivedMessageHeader`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `childPersonId` | `String` |  |
| `formattedDate` | `Date` |  |
| `hasAttachments` | `boolean` |  |
| `id` | `long` |  |
| `messageId` | `long` |  |
| `readStatus` | `boolean` |  |
| `from` | `String` |  |
| `date` | `String` |  |
| `subject` | `String` |  |

## ScheduleDay

Client symbol: `lt.zet.tamo.models.realm.ScheduleDay`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `numberday` | `int` |  |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `dayInfos` | `RealmList<ScheduleSubject>` | [realm.ScheduleSubject](realm.md#schedulesubject) |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `week` | `int` |  |
| `year` | `int` |  |

## ScheduleSubject

Client symbol: `lt.zet.tamo.models.realm.ScheduleSubject`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `timefrom` | `String` |  |
| `number` | `int` |  |
| `subject` | `String` |  |
| `teacher` | `String` |  |
| `timeto` | `String` |  |

## SentMessageHeader

Client symbol: `lt.zet.tamo.models.realm.SentMessageHeader`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `formattedDate` | `Date` |  |
| `MessageId` | `long` |  |
| `to` | `String` |  |
| `date` | `String` |  |
| `subject` | `String` |  |

## User

Client symbol: `lt.zet.tamo.models.realm.User`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `children` | `RealmList<Child>` | [realm.Child](realm.md#child) |
| `firstName` | `String` |  |
| `lastName` | `String` |  |
| `personId` | `int` |  |
| `role` | `int` |  |
| `token` | `String` |  |

## Work

Client symbol: `lt.zet.tamo.models.realm.Work`.

Parent: `RealmObject`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateAssign` | `Date` |  |
| `dateDeadline` | `Date` |  |
| `files` | `RealmList<File>` | [realm.File](realm.md#file) |
| `filterHash` | `long` |  |
| `id` | `int` |  |
| `date` | `String` |  |
| `deadline` | `String` |  |
| `studentFirstName` | `String` |  |
| `studentId` | `long` |  |
| `studentLastName` | `String` |  |
| `thingName` | `String` |  |
| `type` | `String` |  |
| `homeWork` | `String` |  |
