# Localization In Code

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Use:

```csharp
Loc.GetString("art-core-feature-message", ("user", user), ("target", target))
```

Avoid:

- raw English strings;
- string concatenation for grammar;
- comparing localized output;
- showing raw IDs to players.

Put matching FTL under `Resources/Locale/en-US/{FORK_DIR}`.
