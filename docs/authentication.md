# Authentication and roles

[Overview](../README.md) | [Protocol](protocol.md) | [Read-only examples](../examples/README.md)

## Login

Send a JSON POST to:

```text
https://dienynas.tamo.lt/MobileServiceV3/AuthenticateV2
```

```http
Content-Type: application/json; charset=UTF-8
```

Illustrative body, with placeholders instead of credentials:

```json
{
  "username": "<username>",
  "password": "<password>",
  "dateTime": "2025-01-01 12:00:00",
  "typePhoneSystem": "Android",
  "guid": "1166cfd3-1be5-4dca-aa64-5aff7bbb8acc"
}
```

| Field | Meaning |
| --- | --- |
| `username` | Account username, serialized as supplied |
| `password` | Account password, serialized as supplied |
| `dateTime` | Device-local time, formatted `yyyy-MM-dd HH:mm:ss`, without a timezone suffix |
| `typePhoneSystem` | The analyzed Android app sends `Android` |
| `guid` | The build constant shown above, not a per-device identifier |

The request path contains no client-side password hash, payload encryption, or request signature. HTTPS is required. Login can create a server-side session.

## Login response

This is a reconstructed shape, not a captured account response. Numeric values are examples, not defaults to reuse.

```json
{
  "Status": 1,
  "ErrorCode": 0,
  "ErrorMessage": null,
  "Result": {
    "authToken": "<server-issued token>",
    "personId": 123,
    "role": 2,
    "accessLevel": 0,
    "userRoleIsAllowed": true,
    "firstName": "<first name>",
    "lastName": "<last name>",
    "children": []
  }
}
```

Check the HTTP result and both `Status == 1` and `ErrorCode == 0`. An HTTP 200 alone is not successful authentication. Confirm that `Result.authToken` is a nonempty string and that the role is allowed before continuing.

The app opens an account-limitation screen when `userRoleIsAllowed` is false. Numeric legacy role `2` constructs a child entry for the authenticated person; role `3` enters an impersonation-related flow. These branches do not establish server permissions for another account. The examples do not implement impersonation.

## Reuse the token across services

Modern requests use a header:

```http
Authorization: Bearer <server-issued token>
Accept: application/json
```

Legacy GETs normally use a query parameter:

```text
GetSubscriptionType?authToken=<URL-encoded token>
```

Legacy JSON and form requests carry the token in their declared body field instead. Use the returned token unchanged. The official app's local preference encryption is not a network requirement.

Do not attach the token to third-party telemetry, arbitrary links, or attachment hosts. A token in a query string is especially easy to expose through logs, copied URLs, and HTTP error messages.

## Select a modern role

The app requests `core/app/settings/StyleRef`, then `core/app/roles`, using the Bearer token. The role response contains `roles` and `userInfo` alongside the modern status fields.

For role-scoped requests:

```http
x-selected-role: <roles[n].id>
```

| Field | Use |
| --- | --- |
| `Role.id` | Value of `x-selected-role` |
| `Role.roleId` | Separate role identifier used by client comparisons/cache keys |
| `Role.studentId` | Student identifier, including `MokinioId` in the homework-completion request |
| `Role.personId` | Person identifier carried by the role model |
| `AuthResponse.personId` | Person identifier returned by legacy login |
| `Role.active` | Client role-selection state; do not assume all roles are active or interchangeable |

Never manufacture a role header from a display name, array index, or student ID. If an account exposes several roles, explicitly select one from that response. See the [Role model](models/data.md#role) for all fields.

## Expiry, errors, and logout

No refresh-token endpoint is declared in the two recovered service interfaces. Token format, lifetime, concurrent-session limits, and revocation behavior have not been established. Do not assume the token is a JWT or invent a refresh route.

The legacy client treats the exact message `User is not authenticated.` as a logout-related condition. It also handles `ErrorCode == -13` by opening subscription UI. See [protocol errors](protocol.md#response-envelopes-and-errors) and [premium](premium.md).

The official logout workflow unregisters the push installation, requests Firebase token deletion, and calls legacy `GET Logout`. The examples deliberately do none of these. Exiting a program discards its local token but is not proof that the server session was revoked.

## Evidence

Login JSON, field names, and token reuse were confirmed in the paid-account baseline. Source-level references for build 4.17 include `lt.zet.tamo.models.request.Auth`, its generated field implementation, `lt.zet.tamo.models.response.AuthResponse`, `af.d2`, `of.c`, and service interfaces `ye.g0` and `ye.p`. See [scope](scope.md) for how to interpret these references.
