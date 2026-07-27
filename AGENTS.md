# Agent Router

This repository is an SS14 fork. Before making changes:

1. Load `.agents/fork-config.md` — read `FORK_DIR`, `EDIT_MARKER`, and `FORK_NAME`.
2. Load `.agents/rules/ss14-art-hard-guardrails.md`.
3. Load `.agents/rules/ss14-art-upstream-edit-markers.md`.
4. Load `.agents/rules/ss14-skill-preflight-and-refresh.md`.
5. Load the smallest relevant skill under `.agents/skills/`.
6. If using Codex-specific automation, `.codex/config.toml` only bridges back to `.agents`; `.agents` remains canonical.

Hard rules:

- Never edit `RobustToolbox/**`.
- New fork-only code goes under `{FORK_DIR}` (from `.agents/fork-config.md`, default `_Art`).
- Any file changed outside `{FORK_DIR}` needs a tight `{EDIT_MARKER}-Edit` / `{EDIT_MARKER}-Start` / `{EDIT_MARKER}-End` marker block.
- Prefer prediction, localization, data-driven prototypes, modular ECS systems, and .NET 10-current code.
- Do not duplicate mechanics or hardcode one-off behavior.

Subtree `AGENTS.md` files add local routing; follow them in addition to this root file.
