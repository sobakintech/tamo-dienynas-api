# Style models

[Model index](README.md) | [API reference](../../README.md)

Presentation rules returned by `core/app/settings/StyleRef`. Content objects can reference a style by key. These fields describe the Android client's model, not mandatory server values or instructions that every consumer must render identically.

## StyleRef

Client symbol: `lt.zet.tamo.utils.style.StyleRef`.

| Field | Client type |
| --- | --- |
| `allCaps` | `boolean` |
| `backgroundColor` | `String` |
| `backgroundShape` | `String` |
| `borderColor` | `String` |
| `color` | `String` |
| `fontSize` | `Integer` |
| `key` | `String` |
| `layoutGravity` | `String` |
| `linkable` | `boolean` |
| `minFontSize` | `Integer` |
| `singleLine` | `boolean` |
| `typeface` | `String` |
| `viewGravity` | `String` |

## Local style helpers

The original inventory also includes these five rendering helpers. They have no direct fields in the recovered model table and do not define additional JSON request or response schemas.

### Defaults

Client symbol: `lt.zet.tamo.utils.style.Defaults`. No direct JSON fields cataloged.

### Stylable

Client symbol: `lt.zet.tamo.utils.style.Stylable`. No direct JSON fields cataloged.

### Style

Client symbol: `lt.zet.tamo.utils.style.Style`. No direct JSON fields cataloged.

### StyleableContent

Client symbol: `lt.zet.tamo.utils.style.StyleableContent`. No direct JSON fields cataloged.

### StyleUtils

Client symbol: `lt.zet.tamo.utils.style.StyleUtils`. No direct JSON fields cataloged.
