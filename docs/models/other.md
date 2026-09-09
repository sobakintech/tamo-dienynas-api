# Other models

[Model index](README.md) | [API reference](../../README.md)

Supporting models, including subscriptions, menus, products, and local helper objects. Objects such as `DataStoreResponse`, `Attachment`, and filter state can contain client-only fields.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## Attachment

Client symbol: `lt.zet.tamo.models.other.Attachment`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `body` | `String` |  |
| `id` | `long` |  |
| `messageId` | `long` |  |
| `name` | `String` |  |
| `path` | `String` |  |
| `status` | `int` |  |
| `uri` | `Uri` |  |

## Badge

Client symbol: `lt.zet.tamo.models.other.Badge`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `value` | `int` |  |

## DataStoreResponse

Client symbol: `lt.zet.tamo.models.other.DataStoreResponse`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `done` | `boolean` |  |
| `error` | `Throwable` |  |
| `response` | `T` |  |
| `source` | `int` |  |
| `status` | `int` |  |

## DownloadableFile

Client symbol: `lt.zet.tamo.models.other.DownloadableFile`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `description` | `String` |  |
| `fileId` | `String` |  |
| `fileName` | `String` |  |
| `fileType` | `String` |  |

## Filter

Client symbol: `lt.zet.tamo.models.other.Filter`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateRangeFrom` | `String` |  |
| `dateRangeTo` | `String` |  |
| `itemTypes` | `List<String>` |  |
| `periodId` | `long` |  |
| `studentId` | `long` |  |
| `type` | `String` |  |

## FilterOptions

Client symbol: `lt.zet.tamo.models.other.FilterOptions`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `filterType` | `String` |  |
| `showClearFilters` | `Boolean` |  |
| `showFilterTitle` | `Boolean` |  |

## KeyValue

Client symbol: `lt.zet.tamo.models.other.KeyValue`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `key` | `String` |  |
| `value` | `String` |  |

## Language

Client symbol: `lt.zet.tamo.models.other.Language`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `id` | `int` |  |
| `title` | `String` |  |

## LocalContact

Client symbol: `lt.zet.tamo.models.other.LocalContact`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `firstName` | `String` |  |
| `groupName` | `String` |  |
| `id` | `long` |  |
| `lastName` | `String` |  |
| `personId` | `long` |  |

## MenuGroup

Client symbol: `lt.zet.tamo.models.other.MenuGroup`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `backroundColorhex` | `String` |  |
| `iconUrl` | `String` |  |
| `id` | `String` |  |
| `groupItems` | `List<MenuItem>` | [other.MenuItem](other.md#menuitem) |
| `textColorhex` | `String` |  |
| `title` | `String` |  |

## MenuItem

Client symbol: `lt.zet.tamo.models.other.MenuItem`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `backroundColorhex` | `String` |  |
| `doAuth` | `boolean` |  |
| `iconUrl` | `String` |  |
| `id` | `String` |  |
| `menuUrl` | `String` |  |
| `rootIconUrl` | `String` |  |
| `textColorhex` | `String` |  |
| `title` | `String` |  |

## MoreItem

Client symbol: `lt.zet.tamo.models.other.MoreItem`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `children` | `List<MoreItem<T>>` | [other.MoreItem](other.md#moreitem) |
| `item` | `T` |  |
| `title` | `String` |  |
| `type` | `String` |  |

## PaymentButton

Client symbol: `lt.zet.tamo.models.other.PaymentButton`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `code` | `String` |  |
| `color` | `String` |  |
| `smscode` | `String` |  |
| `smsnumber` | `String` |  |
| `text` | `String` |  |

## Product

Client symbol: `lt.zet.tamo.models.other.Product`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `prodCode` | `String` |  |
| `prodDescription` | `String` |  |
| `prodId` | `long` |  |
| `prodName` | `String` |  |
| `prodPeriod` | `String` |  |
| `premium_price` | `String` |  |
| `prodPrice` | `double` |  |
| `sms_price_desc` | `String` |  |
| `prodPriceId` | `long` |  |
| `smsNumber` | `String` |  |

## r

Client symbol: `lt.zet.tamo.models.other.r`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `a` | `String` |  |

## RatingItem

Client symbol: `lt.zet.tamo.models.other.RatingItem`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `item` | `T` |  |
| `selected` | `boolean` |  |
| `type` | `int` |  |

## Sms

Client symbol: `lt.zet.tamo.models.other.Sms`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `message` | `String` |  |
| `number` | `String` |  |

## Subscription

Client symbol: `lt.zet.tamo.models.other.Subscription`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `alertUntil` | `int` |  |
| `dateActive` | `int` |  |
| `friendlyTitle` | `String` |  |
| `fromDate` | `String` |  |
| `prodName` | `String` |  |
| `showStartTrial` | `int` |  |
| `subscrStatus` | `String` |  |
| `toDate` | `String` |  |
| `subscrType` | `String` |  |
