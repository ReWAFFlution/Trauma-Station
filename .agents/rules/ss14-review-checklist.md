# SS14 Review Checklist

> **Config:** Actual fork values (`FORK_DIR`, `EDIT_MARKER`, `FORK_NAME`) are defined in `.agents/fork-config.md`.

Review AI-generated {FORK_NAME} changes against this list.

- No `RobustToolbox/**` modifications.
- New {FORK_NAME} code lives under `{FORK_DIR}`.
- Any non-`{FORK_DIR}` file change has a tight `{EDIT_MARKER}-Edit` marker block.
- Code is modular, data-driven, and does not duplicate an existing mechanic.
- Component data stays data-only; behavior is in systems.
- Shared/server/client placement matches prediction and security needs.
- Networked fields are dirtied correctly and do not leak hidden info.
- Client network input is validated server-side.
- Player-facing text is localized.
- Prototype IDs, sounds, sprites, CVars, and magic values are typed/configurable.
- Tests or manual validation cover the real behavior, especially prediction and networking.
- PR explains linked issue, balance impact, technical details, media, and licensing/attribution.
