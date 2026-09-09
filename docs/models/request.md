# Request models

[Model index](README.md) | [API reference](../../README.md)

JSON request bodies and related request objects. The endpoint references distinguish JSON bodies from form fields. Do not send fields from an unrelated request object simply because it exists here.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## AttachFile

Client symbol: `lt.zet.tamo.models.request.AttachFile`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `authToken` | `String` |  |
| `fileBody` | `String` |  |
| `fileName` | `String` |  |
| `messageId` | `long` |  |

## Auth

Client symbol: `lt.zet.tamo.models.request.Auth`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateTime` | `String` |  |
| `guid` | `String` |  |
| `password` | `String` |  |
| `typePhoneSystem` | `String` |  |
| `username` | `String` |  |

## Installation

Client symbol: `lt.zet.tamo.models.request.Installation`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `DeviceId` | `String` |  |
| `Id` | `String` |  |

## InstallationRequest

Client symbol: `lt.zet.tamo.models.request.InstallationRequest`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `Installation` | `Installation` | [request.Installation](request.md#installation) |

## Request

Client symbol: `lt.zet.tamo.models.request.Request`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `dateFrom` | `String` |  |
| `personId` | `String` |  |
| `dateTo` | `String` |  |
| `authToken` | `String` |  |
| `wType` | `String` |  |
