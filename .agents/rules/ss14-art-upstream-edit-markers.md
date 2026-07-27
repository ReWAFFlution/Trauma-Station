# SS14-ART-CORE Upstream Edit Markers

> **Config:** Actual fork values (`FORK_DIR`, `EDIT_MARKER`, `FORK_NAME`) are defined in `.agents/fork-config.md`.

{FORK_NAME} must stay easy to merge with upstream.

## Rule

Any modification to a file outside a `{FORK_DIR}` path segment must be surrounded by `{EDIT_MARKER}` markers.

For multi-line changes:

```csharp
// {EDIT_MARKER}-Start: short reason
CODE
// {EDIT_MARKER}-End
```

For single-line changes:

```csharp
CODE // {EDIT_MARKER}-Edit: reason
```

Use the same marker shape for comments in C#, YAML, FTL, XAML, TOML, JSON-with-comments, and Markdown when practical. For formats where `//` is invalid, use the native comment delimiter:

```yaml
# {EDIT_MARKER}-Start: short reason
code: here
# {EDIT_MARKER}-End

single_line: here # {EDIT_MARKER}-Edit
```

```xml
<!-- {EDIT_MARKER}-Start: short reason -->
<Control />
<!-- {EDIT_MARKER}-End -->

<Control Property="Value" /> <!-- {EDIT_MARKER}-Edit -->
```

## Scope

- Marker blocks must be as small as possible.
- Do not wrap whole files unless the whole file is an {FORK_NAME}-owned adapter.
- Do not use markers in `RobustToolbox/**`; engine edits are forbidden.
- Do not hide unrelated formatting or reorder-only changes inside marker blocks.
- If a file already has a nearby `{EDIT_MARKER}` marker, extend the smallest existing block instead of creating marker noise.

## Preferred Alternative

Avoid upstream edits by adding or overriding fork-only code under `{FORK_DIR}`:

- `Content.Shared/{FORK_DIR}/...`
- `Content.Server/{FORK_DIR}/...`
- `Content.Client/{FORK_DIR}/...`
- `Resources/Prototypes/{FORK_DIR}/...`
- `Resources/Locale/en-US/{FORK_DIR}/...`
- `Resources/Textures/{FORK_DIR}/...`
- `Resources/Audio/{FORK_DIR}/...`
