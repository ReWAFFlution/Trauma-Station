# Edit Types

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Safe

- Add a hook call to fork-owned system.
- Add a prototype include/reference for `{FORK_DIR}` content.
- Add a localized entry for {FORK_NAME}-only content.

## Risky

- Change upstream component semantics.
- Change shared enum/list ordering.
- Change serialization shape.
- Change network state.

Risky edits need stronger review and validation.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
