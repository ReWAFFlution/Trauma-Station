# Audio Specifiers

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Use `SoundSpecifier` in components and prototypes.

Prefer:

- `SoundCollectionSpecifier` for reusable random sets;
- data fields for feature-specific sounds;
- prototype configuration over hardcoded paths.

Put SS14-ART-CORE audio under `Resources/Audio/{FORK_DIR}`.

Fork directory is configured in `.agents/fork-config.md` (`FORK_DIR`).
