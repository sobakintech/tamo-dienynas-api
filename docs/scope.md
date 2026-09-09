# Scope and evidence

[Overview](../README.md) | [Validation](validation.md)

## Analyzed build

| Property | Value |
| --- | --- |
| App | TAMO IŠMANIEMS |
| Package | `lt.zet.tamo` |
| Version name | `4.17` |
| Version code | `4170000` |
| Minimum Android SDK | `24` |
| Target/compile SDK | `35` |
| Reference period | September 2026 |
| Base APK SHA-256 | `80b3db568a16e97b70a1ba8d1e8a064694ff63fd01a0400b2e2a2e589d9883a1` |

The analysis covered the base APK and its ARM64, English, and xxhdpi configuration splits. The reference period is the month of analysis, not the app's release date.

Original APKs, signing material, decompiled code, extraction metadata, and analysis scripts are not distributed in this repository. The build identifier and source symbols provide context without publishing those artifacts.

## Evidence levels

| Label | Meaning |
| --- | --- |
| Static | Recovered from this build's declarations, models, resources, or call sites |
| Paid baseline: success | The request succeeded with an active paid subscription and the tested parameters |
| Paid baseline: HTTP 404 | The tested request failed with that HTTP status |
| Inferred | A conclusion drawn from client behavior, not an observed server implementation |
| Unknown/not tested | No supporting live result or sufficiently complete static evidence |

Examples in fenced JSON/HTTP blocks use placeholders or illustrative values. They are not raw captured responses.

## What was checked

The two Retrofit interfaces declare 15 modern and 28 legacy fixed operations, plus one GET taking a complete URL at runtime. HTTP methods, paths, and parameter annotations were independently compared against the original DEX data. All 44 declarations matched, and each had at least one recovered direct caller.

The 114 model/support classes contain 559 direct fields. Original field names and serialization aliases were independently checked against DEX data. The inventory includes response/request models and related local state, so it must not be treated as 559 guaranteed server properties.

The source tree was also examined for manually constructed requests, WebView navigation, DownloadManager use, image loading, and relevant SDK transports. This established the extra `MobileServiceV3/NavigateDirect` navigation route and the contextual integrations described separately.

JADX 1.5.6 reported 130 decompilation errors across the full app. The emitted source contained 77 explicit error comments, with none in the reviewed first-party namespace set (`lt.zet.tamo`, `af`, `of`, `ye`, `ze`, `df`, `ff`). These are different measurements, and warnings or imperfect reconstruction can exist without an explicit error marker. Decompiled output is not the original source or a guaranteed recompilable program.

Native inspection covered packaged library inventories, strings, and imported symbols. No separate TAMO native network implementation was identified. This was not a full disassembly of every third-party library. No bundled web application JavaScript was found in the base assets.

## Interpreting source references

Symbols such as `ye.p`, `ye.g0`, and `af.l1` refer to obfuscated classes in the analyzed build. They are evidence locators, not stable public API names. Another build can assign different names.

## What remains unknown

- Server endpoints not referenced by this build, older/newer versions, and unpublished server logic.
- The full endpoint-by-endpoint entitlement policy for ordinary unpaid accounts.
- Token format, lifetime, refresh alternatives outside these declarations, concurrent sessions, and revocation behavior.
- Complete server schemas, requiredness, validation rules, nullability, dynamic objects, and ignored extra fields.
- Server rate limits, upload/download quotas, permitted file types, attachment retention, signed-URL expiry, and cross-account authorization.
- Browser CORS policy, web cookie/redirect behavior, and all requests made by remotely downloaded web content.
- Current behavior of the write routes and dependent reads excluded from validation.
- Runtime Google Play services cloud connections, dynamically loaded SDK behavior, and dormant/conditional telemetry paths.
- Full Android APK signature-scheme verification. A content hash identifies the analyzed bytes but does not replace signature verification.
