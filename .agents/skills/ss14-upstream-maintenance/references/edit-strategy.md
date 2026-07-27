# Edit Strategy

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

Prefer:

1. new `{FORK_DIR}` file;
2. existing {FORK_NAME}-owned file;
3. tiny upstream integration edit with marker;
4. maintainer-approved broader upstream refactor.

Avoid:

- formatting upstream files;
- moving unrelated code;
- renaming upstream APIs for style;
- hiding large changes inside marker blocks.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
