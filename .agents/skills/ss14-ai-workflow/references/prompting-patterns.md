# Prompting Patterns

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Good Agent Prompts

- Name the subsystem and target assembly.
- Say whether prediction is required.
- Mention localization and `{FORK_DIR}` placement.
- Ask to search for existing mechanics first.
- Ask for reusable component/system APIs, not one-off prototype branches.

## Example

> Add a {FORK_NAME}-only reusable component/system under `{FORK_DIR}` for this interaction. Keep it predicted if possible, localize all text, do not edit RobustToolbox, and mark any non-`{FORK_DIR}` integration edits.

## Bad Prompt Smells

- "Just make it work."
- "Copy this other feature" without asking for adaptation.
- "Hardcode this prototype for now."

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
