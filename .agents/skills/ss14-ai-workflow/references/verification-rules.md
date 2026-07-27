# Verification Rules

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Before Calling Work Done

- Check `git diff` for accidental upstream churn.
- Check non-`{FORK_DIR}` edits for `{EDIT_MARKER}-Edit` markers.
- Check every player-facing string has FTL.
- Check networked fields are dirtied.
- Check client-origin actions are server-validated.
- Run the smallest meaningful validation command.

## Report Format

Say:

- what changed;
- what validation ran;
- what was not validated;
- any residual prediction, UI, DB, or asset risk.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
