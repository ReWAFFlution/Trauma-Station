# {FORK_NAME} Gameplay Map

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Code

- Shared predicted logic: `Content.Shared/{FORK_DIR}`.
- Authority-only logic: `Content.Server/{FORK_DIR}`.
- Presentation: `Content.Client/{FORK_DIR}`.

## Resources

- Prototypes: `Resources/Prototypes/{FORK_DIR}`.
- FTL: `Resources/Locale/en-US/{FORK_DIR}`.
- Textures/audio: `Resources/Textures/{FORK_DIR}`, `Resources/Audio/{FORK_DIR}`.

## Integration

If upstream files need hooks, keep edits tiny and marked.

> Fork-specific values (`{FORK_DIR}`, `{FORK_NAME}`, `{EDIT_MARKER}`) defined in `.agents/fork-config.md`.
