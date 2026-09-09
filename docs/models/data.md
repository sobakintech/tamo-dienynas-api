# Data models

[Model index](README.md) | [API reference](../../README.md)

Models used primarily by the modern service. The same short name can exist in the legacy `realm` group with a different shape.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## Analytics

Client symbol: `lt.zet.tamo.models.data.Analytics`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `average` | `Stat` | [data.Stat](data.md#stat) |
| `positionInClass` | `Stat` | [data.Stat](data.md#stat) |
| `positionInSchool` | `Stat` | [data.Stat](data.md#stat) |
| `schoolSubjectId` | `long` |  |
| `title` | `Content` | [data.Content](data.md#content) |

## AssessmentInfo

Client symbol: `lt.zet.tamo.models.data.AssessmentInfo`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `assessmentColor` | `String` |  |
| `assessmentDateTime` | `String` |  |
| `assessmentType` | `String` |  |
| `assessmentValue` | `String` |  |
| `attendanceDateTime` | `String` |  |
| `attendanceValue` | `String` |  |
| `studentId` | `Long` |  |
| `subject` | `String` |  |
| `subjectDate` | `LocalDate` |  |
| `type` | `Integer` |  |

## Calculator

Client symbol: `lt.zet.tamo.models.data.Calculator`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `html` | `String` |  |
| `plainText` | `String` |  |
| `title` | `String` |  |

## Content

Client symbol: `lt.zet.tamo.models.data.Content`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `content` | `String` |  |
| `contentType` | `String` |  |
| `key` | `String` |  |
| `styleRef` | `String` |  |
| `url` | `String` |  |

## DayBadge

Client symbol: `lt.zet.tamo.models.data.DayBadge`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `date` | `LocalDate` |  |
| `badges` | `List<Content>` | [data.Content](data.md#content) |

## DayEvents

Client symbol: `lt.zet.tamo.models.data.DayEvents`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `date` | `LocalDate` |  |
| `events` | `List<Event>` | [data.Event](data.md#event) |

## Event

Client symbol: `lt.zet.tamo.models.data.Event`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `timeBadges` | `List<Content>` | [data.Content](data.md#content) |
| `bottomIconsLeft` | `List<Content>` | [data.Content](data.md#content) |
| `bottomIconsRight` | `List<Content>` | [data.Content](data.md#content) |
| `currentDateTime` | `ZonedDateTime` |  |
| `displayType` | `String` |  |
| `timeToUtc` | `ZonedDateTime` |  |
| `eventDescription` | `Content` | [data.Content](data.md#content) |
| `eventDetails` | `List<EventDetails>` | [data.EventDetails](data.md#eventdetails) |
| `eventHighlight` | `Content` | [data.Content](data.md#content) |
| `eventIcon` | `Content` | [data.Content](data.md#content) |
| `eventLabel` | `Content` | [data.Content](data.md#content) |
| `eventSubtitle` | `Content` | [data.Content](data.md#content) |
| `eventTitle` | `Content` | [data.Content](data.md#content) |
| `formatives` | `List<FormativeGrade>` | [data.FormativeGrade](data.md#formativegrade) |
| `id` | `long` |  |
| `references` | `References` | [data.References](data.md#references) |
| `rightIconsBottom` | `Content` | [data.Content](data.md#content) |
| `rightIconsMiddle` | `Content` | [data.Content](data.md#content) |
| `rightIconsTop` | `Content` | [data.Content](data.md#content) |
| `sid` | `String` |  |
| `timeFromUtc` | `ZonedDateTime` |  |
| `type` | `String` |  |
| `usesFormatives` | `boolean` |  |

## EventDetails

Client symbol: `lt.zet.tamo.models.data.EventDetails`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `body` | `Content` | [data.Content](data.md#content) |
| `files` | `List<File>` | [data.File](data.md#file) |
| `icon` | `Content` | [data.Content](data.md#content) |
| `key` | `String` |  |
| `label` | `Content` | [data.Content](data.md#content) |
| `title` | `Content` | [data.Content](data.md#content) |

## FeedItem

Client symbol: `lt.zet.tamo.models.data.FeedItem`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `date` | `Date` |  |
| `eventDetails` | `FeedItemDetails` | [data.FeedItemDetails](data.md#feeditemdetails) |
| `eventId` | `Integer` |  |
| `id` | `Long` |  |
| `operationId` | `Integer` |  |

## FeedItemDetails

Client symbol: `lt.zet.tamo.models.data.FeedItemDetails`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Date` | `String` |  |
| `Deadline` | `LocalDate` |  |
| `Description` | `String` |  |
| `HomeWork` | `String` |  |
| `IconColor` | `String` |  |
| `IsViso` | `Integer` |  |
| `Location` | `String` |  |
| `Reiksme` | `Integer` |  |
| `ThingName` | `String` |  |
| `Tipas` | `String` |  |
| `Type` | `String` |  |
| `Value` | `String` |  |
| `Vertinimas` | `String` |  |
| `VertinimoSistemosKodas` | `String` |  |

## File

Client symbol: `lt.zet.tamo.models.data.File`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `content` | `String` |  |
| `contentType` | `String` |  |
| `friendlySize` | `String` |  |
| `fileSid` | `String` |  |
| `styleRef` | `String` |  |

## FormativeGrade

Client symbol: `lt.zet.tamo.models.data.FormativeGrade`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `date` | `LocalDate` |  |
| `isConverted` | `Boolean` |  |
| `lessonId` | `Long` |  |
| `percents` | `Integer` |  |
| `subject` | `String` |  |
| `subjectId` | `Long` |  |
| `system` | `String` |  |
| `title` | `String` |  |
| `type` | `String` |  |

## FormativeGroup

Client symbol: `lt.zet.tamo.models.data.FormativeGroup`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `items` | `List<FormativeGrade>` | [data.FormativeGrade](data.md#formativegrade) |
| `key` | `String` |  |

## Grade

Client symbol: `lt.zet.tamo.models.data.Grade`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `body` | `Content` | [data.Content](data.md#content) |
| `icon` | `Content` | [data.Content](data.md#content) |
| `key` | `String` |  |
| `title` | `Content` | [data.Content](data.md#content) |

## GradeGroup

Client symbol: `lt.zet.tamo.models.data.GradeGroup`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `items` | `List<Grade>` | [data.Grade](data.md#grade) |
| `key` | `String` |  |

## LegacyFile

Client symbol: `lt.zet.tamo.models.data.LegacyFile`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `description` | `String` |  |
| `fileName` | `String` |  |
| `fileType` | `String` |  |
| `fileId` | `String` |  |

## Message

Client symbol: `lt.zet.tamo.models.data.Message`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `String` |  |
| `messageTypeId` | `String` |  |
| `messagingFolder` | `String` |  |

## Period

Client symbol: `lt.zet.tamo.models.data.Period`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `current` | `boolean` |  |
| `id` | `long` |  |
| `subtitle` | `String` |  |
| `title` | `String` |  |

## PeriodSummary

Client symbol: `lt.zet.tamo.models.data.PeriodSummary`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `analytics` | `Analytics` | [data.Analytics](data.md#analytics) |
| `calculator` | `Calculator` | [data.Calculator](data.md#calculator) |
| `finalGrades` | `List<Grade>` | [data.Grade](data.md#grade) |
| `grades` | `List<Grade>` | [data.Grade](data.md#grade) |
| `period` | `Period` | [data.Period](data.md#period) |
| `references` | `References` | [data.References](data.md#references) |

## References

Client symbol: `lt.zet.tamo.models.data.References`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `formatives` | `String` |  |
| `grades` | `String` |  |

## Role

Client symbol: `lt.zet.tamo.models.data.Role`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `active` | `boolean` |  |
| `id` | `String` |  |
| `avatar` | `String` |  |
| `periodType` | `String` |  |
| `childPersonId` | `long` |  |
| `roleId` | `String` |  |
| `titleShort` | `String` |  |
| `childStudentId` | `long` |  |
| `subtitle` | `String` |  |
| `title` | `String` |  |

## Stat

Client symbol: `lt.zet.tamo.models.data.Stat`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `body` | `Content` | [data.Content](data.md#content) |
| `title` | `Content` | [data.Content](data.md#content) |
| `total` | `Content` | [data.Content](data.md#content) |

## UserInfo

Client symbol: `lt.zet.tamo.models.data.UserInfo`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `firstName` | `String` |  |
| `fullName` | `String` |  |
| `personId` | `long` |  |
| `avatar` | `String` |  |
| `lastName` | `String` |  |
| `subscriptionLevel` | `String` |  |

## Work

Client symbol: `lt.zet.tamo.models.data.Work`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `completionDate` | `Date` |  |
| `date` | `Date` |  |
| `deadline` | `Date` |  |
| `files` | `List<LegacyFile>` | [data.LegacyFile](data.md#legacyfile) |
| `homeWork` | `String` |  |
| `lessonId` | `long` |  |
| `studentFirstname` | `String` |  |
| `studentId` | `long` |  |
| `studentLastname` | `String` |  |
| `thingName` | `String` |  |
