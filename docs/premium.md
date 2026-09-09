# Subscriptions and premium

[Overview](../README.md) | [Subscription endpoints](endpoints-legacy.md) | [Validation](validation.md)

## Short answer

**For normal diary, grades, homework, and calendar access, assume an active TAMO IŠMANIEMS subscription is required.** The app checks subscription status, and live checks only covered access with premium enabled. The server's requirement for each endpoint is still unverified.

The app has a client-side navigation gate driven by server subscription responses. It also handles a legacy server error by opening subscription UI. **The available evidence does not establish that every mobile endpoint works without premium.**

Core reads worked with an active paid subscription. Free, trial, and expired-subscription access remains untested.

This is not a blanket paid-subscription requirement for every route: login and subscription-management calls precede the client gate, and trials or the server-defined `free` classification can grant full client navigation.

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

This shows that the app anticipates a server-side refusal after a data request. It does not establish the exact server definition of `-13`, the endpoint-by-endpoint policy, or whether every current service uses that code. No such refusal was observed in the paid baseline.

Modern responses use `isSuccess`, `message`, and `errors`, with HTTP failures handled separately. No distinct premium-specific modern HTTP mapping was found in the reviewed client code. A generic error mechanism can still carry an entitlement denial.

## What another client sends

Modern requests carry the token and, when required, the selected role. Legacy requests carry `authToken`. The recovered interfaces send no separate `isPremium` header, client entitlement assertion, or purchase receipt on ordinary data reads.

Another client can implement this request format without reproducing the official app's navigation gate. That does not change server authorization. The server can associate the token with an account's subscription.

| Question | Answer supported by the evidence |
| --- | --- |
| Does login occur before the premium gate? | Yes, in the official client flow. |
| Are subscription/product endpoints used in limited mode? | Yes, by the client. Paid reads succeeded; unpaid behavior is untested. |
| Can the app grant full navigation without a paid record? | Yes, for the server's `free` classification or an active trial. Eligibility is unknown. |
| Can a custom client read diary/calendar/homework with a paid account? | Yes, these reads worked with an active paid subscription. |
| Will those same requests work after expiry? | Unknown. Expired-subscription access has not been tested. |
| Does changing a local premium flag grant server access? | No such effect has been demonstrated. |

## Validation limits

An HTTP 200, an empty list, or a successful login alone does not establish free access to a data endpoint. Subscription-changing operations were not tested.

## Evidence

Build 4.17 symbols: `af.l1`, `lt.zet.tamo.models.other.Subscription`, `lt.zet.tamo.models.response.SubscriptionTypeResponse`, `lt.zet.tamo.models.state.SubscriptionState`, `lt.zet.tamo.ui.content.ContentActivity`, and `ze.z`. See [live validation](validation.md) for test results.
