# State models

[Model index](README.md) | [API reference](../../README.md)

Local client state, included to explain subscription handling. These objects are not declared API request bodies.

Field names preserve original DEX names and serialization aliases. Types describe the Android client, not server validation or requiredness. An absent, null, or additional field can still occur. Parent fields are documented under the parent model.

## SubscriptionState

Client symbol: `lt.zet.tamo.models.state.SubscriptionState`.

| Field | Client type | Referenced models |
| --- | --- | --- |
| `status` | `SubscriptionState.Status` | [state.SubscriptionState](state.md#subscriptionstate) |
| `subscription` | `Subscription` | [other.Subscription](other.md#subscription) |
