# Related services and non-TAMO traffic

[Overview](../README.md) | [Push registration](workflows.md#push-registration) | [Scope](scope.md)

These are contextual findings from SDK code and app initialization, not additional TAMO diary endpoints. No third-party service was contacted during validation. A bundled URL or configuration value does not prove a request is sent at runtime.

## Firebase and push

The analyzed app includes Firebase Installations, Messaging, Crashlytics, Sessions, and Analytics. Its configured project is `tamo-mobile-app`. Firebase installation/authentication tokens and FCM registration tokens are separate from the token returned by TAMO login.

| Operation | Recovered endpoint or mechanism |
| --- | --- |
| Create Firebase installation | `POST https://firebaseinstallations.googleapis.com/v1/projects/{projectId}/installations` |
| Generate installation auth token | `POST https://firebaseinstallations.googleapis.com/v1/projects/{projectId}/installations/{fid}/authTokens:generate` |
| Obtain/delete FCM registration token | Google Play services RPC |
| Register token with TAMO | `POST https://api.tamo.lt/core/app/devices/installation` |

The FCM adapter exchanges registration bundles with Google Play services. Cloud host selection, ports, and the persistent push connection inside Play services are not present in the analyzed app's own RPC implementation. No TAMO-specific topic subscription was established.

The Firebase Installations request uses JSON with `fid`, `appId`, `authVersion`, and `sdkVersion`, plus app/package/certificate-related headers. Firebase handles its own token lifecycle. These fields must not be confused with TAMO's `username`, `password`, and `authToken`.

Realtime Database and Storage bucket settings are present in resources, but no first-party use of those products was established. Project configuration alone is not evidence of an exposed database, writable bucket, or usable replacement-client push integration.

## Telemetry endpoints

| Component | Recovered URL/template | Qualification |
| --- | --- | --- |
| Crashlytics and Sessions settings | `https://firebase-settings.crashlytics.com/spi/v2/platforms/android/gmp/{googleAppId}/settings` | Settings requests use app/build and SDK/device information |
| Crashlytics reports | `https://crashlyticsreports-pa.googleapis.com/v1/firelog/legacy/batchlog` | Google Data Transport destination |
| CCT default transport | `https://firebaselogging.googleapis.com/v0cc/log/batch?format=json_proto3` | Exact `v0cc` spelling recovered from bundled constants |
| Alternative transport | `https://firebaselogging-pa.googleapis.com/v1/firelog/legacy/batchlog` | Alternative bundled destination, not proof both are used |
| Firebase Analytics upload | `https://app-measurement.com/a` | Bundled measurement default |
| Analytics configuration | `https://app-measurement.com/config/app/{appId}?platform=android&gmp_version=97001&runtime_version=0` | Bundled configuration builder |
| Measurement tagging | `https://app-measurement.com/s` | Conditional SDK feature |
| Legacy Analytics | `https://ssl.google-analytics.com/collect`, `https://ssl.google-analytics.com/batch` | Tracker initialization and explicit screen-view calls found |
| Deferred deep links | `https://www.googleadservices.com/pagead/conversion/app/deeplink` | Conditional measurement SDK code |
| Advertising-ID diagnostics | `https://pagead2.googlesyndication.com/pagead/gen_204?id=gmob-apps` | Conditional SDK diagnostic code |
| Tag Manager | `https://www.googletagmanager.com` | Bundled host, no TAMO-specific container request established |

Some transport URLs are assembled by interleaving string constants rather than stored as a complete URL. They are Google telemetry destinations, not hidden TAMO API routes.

Although the manifest disables Crashlytics collection by default, application startup explicitly enables it. The content activity sets a Crashlytics user identifier from the TAMO person ID, and an error helper records exceptions. That establishes code paths, not a captured report payload. Optional SDK report fields and collection/sampling conditions should not be presented as observed transmissions.

Google Data Transport supports gzip-compressed JSON and encoded event payloads, redirect handling, and server-provided scheduling delays. Its transport behavior is separate from the TAMO OkHttp client.

## Images and web content

Glide loads some server-supplied images using a separate HttpURLConnection-based stack. The recovered fetcher has a 2.5-second default timeout and bounded redirect handling. TAMO Bearer headers are not added by the reviewed image call sites.

Push payloads can contain an image URL, while menus and WebViews can load downloaded HTML, scripts, images, and further requests. Those dynamic destinations cannot be exhaustively recovered from a static APK without the corresponding server responses and web assets.

None of these telemetry services is required by the supplied API examples. The examples send credentials only to the known TAMO login origin and make no third-party requests.
