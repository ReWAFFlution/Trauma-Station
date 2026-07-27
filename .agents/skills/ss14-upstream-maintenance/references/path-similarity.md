# Path Similarity

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Under `{FORK_DIR}`, mirror upstream subsystem structure when it helps comparison.

Example:

- upstream: `Content.Shared/Weapons/Ranged/...`
- {FORK_NAME}: `Content.Shared/{FORK_DIR}/Weapons/Ranged/...`

This makes future ports, blame, and merge conflict review easier.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
