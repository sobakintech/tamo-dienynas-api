# Subscriptions and premium

[Overview](../README.md) | [Subscription endpoints](endpoints-legacy.md) | [Validation](validation.md)

## Short answer

**An expired subscription did not stop the modern API.** After one account's paid subscription lapsed, every tested modern route still returned real data — diary, homework, classwork, grades, calendar, and feeds included. The access that disappeared was on the legacy service.

**An active subscription is still the safe assumption**, because that test used an account the server still classified as a paid *type* with no active subscription — not an account that never paid. A never-paid `free`-type account may be treated differently, and that remains untested.

The app has a client-side navigation gate driven by server subscription responses, and it also handles a legacy server error by opening subscription UI. That gate is what changes for an unpaid user; it is not the same thing as the server withholding data.

## What actually changed after expiry

Re-running the read-only checks against the same account after its subscription lapsed, the server reported no active subscription while still classifying the account as a paid type:

| Service group | Result after expiry |
| --- | --- |
| Modern `api.tamo.lt` — diary, homework, classwork, grades, calendar, feeds, roles, settings | **All succeeded with real content** (for example 10 homework items, 28 classwork items, 27 feed entries) |
| Legacy `MobileServiceV3` — `GetAssessments`, `GetAwards`, `GetLessons`, `GetNextEvents`, `GetSchedule`, `GetRatingSubjects` | HTTP 200 but **empty**: `Status: 0`, `ErrorCode: 0` |
| Legacy pre-premium reads — `GetProducts`, `GetGlobalSettings`, `GetAdditionalMenu`, login | Unchanged, still `Status: 1` |
| `GetReceivedMessageHeaders`, `GetSendMessageHeaders` | Still HTTP 404, exactly as with the subscription active |

Two alternative explanations were ruled out. The legacy emptiness was **not** an empty date window: a control run pinned to the exact date range that had returned data under the active subscription produced the same empty result. And it was **not** the `-13` subscription refusal described below — the server returned `ErrorCode: 0`, not `-13`, so the app's subscription-redirect path was never triggered.

The mechanism behind the legacy emptiness is not identified by this evidence. Legacy-specific entitlement lapsing, retirement of the legacy service, or account-role behavior all remain consistent with what was observed. What is supported is narrower: the modern routes, which carry the content the current app actually uses, continued to serve the account.

Scope limit: this is **one account, after expiry, still classified as a paid type**. It does not establish that a never-paid free account can read the modern routes.

## Client decision

1. Request `GetSubscriptionType` and read `Result.TypeName`.
2. If it is exactly `free`, the client assigns `PREMIUM` without requiring a paid subscription lookup.
3. Otherwise request `GetUserSubscriptions` and find records where `subscrStatus == "active"` and `dateActive == 1`.
4. No usable subscription produces `LIMITED`.
5. An active record produces `TRIAL` when `showStartTrial == 1`, otherwise `PREMIUM`.
6. Both `PREMIUM` and `TRIAL` allow the full navigation. Limited mode exposes subscription/settings navigation instead.

The distinction in step 5 uses `showStartTrial`, not simply `subscrType == "trial"`. The server's special `free` classification also must not be confused with any account that happens not to have paid.

The state is cached locally. Subscription retrieval failures map to limited mode. The app uses the server-provided activity flag rather than independently verifying a signed purchase receipt in this path.

## Server refusal handling

The legacy response handler checks for `ErrorCode == -13` and publishes a subscription-navigation action. Activities respond by opening the subscription screen.

This shows that the app anticipates a server-side refusal after a data request. It does not establish the exact server definition of `-13`, the endpoint-by-endpoint policy, or whether every current service uses that code. No such refusal was observed in either live run.

Notably, the post-expiry legacy failures used `ErrorCode: 0`, not `-13`. The server emptied those responses without invoking the app's subscription-redirect path, so that path is not the mechanism behind what was observed.

Modern responses use `isSuccess`, `message`, and `errors`, with HTTP failures handled separately. No distinct premium-specific modern HTTP mapping was found in the reviewed client code. A generic error mechanism can still carry an entitlement denial.

## What another client sends

Modern requests carry the token and, when required, the selected role. Legacy requests carry `authToken`. The recovered interfaces send no separate `isPremium` header, client entitlement assertion, or purchase receipt on ordinary data reads.

Another client can implement this request format without reproducing the official app's navigation gate. That does not change server authorization. The server can associate the token with an account's subscription.

| Question | Answer supported by the evidence |
| --- | --- |
| Does login occur before the premium gate? | Yes, in the official client flow. |
| Are subscription/product endpoints used in limited mode? | Yes, by the client. They succeeded both with an active subscription and after expiry. |
| Can the app grant full navigation without a paid record? | Yes, for the server's `free` classification or an active trial. Eligibility is unknown. |
| Can a custom client read diary/calendar/homework with a paid account? | Yes, these reads worked with an active paid subscription. |
| Will those same requests work after expiry? | **Yes, on the modern service**, for the account tested: all tested modern routes still returned real data. The legacy school-data routes went empty. Untested for a never-paid free account. |
| Does changing a local premium flag grant server access? | No such effect has been demonstrated. |

## Validation limits

An HTTP 200, an empty list, or a successful login alone does not establish free access to a data endpoint. Subscription-changing operations were not tested.

The post-expiry result is a single-account observation. A lapsed paid subscription and a never-paid free account are different server states, and only the first was tested.

## Evidence

Build 4.17 symbols: `af.l1`, `lt.zet.tamo.models.other.Subscription`, `lt.zet.tamo.models.response.SubscriptionTypeResponse`, `lt.zet.tamo.models.state.SubscriptionState`, `lt.zet.tamo.ui.content.ContentActivity`, and `ze.z`. See [live validation](validation.md) for test results.
