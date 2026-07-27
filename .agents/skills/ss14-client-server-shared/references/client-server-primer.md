# Client Server Primer

> **Config:** Resolve `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` from `.agents/fork-config.md`.

## Content.Shared

Shared holds data and logic both client and server need. Prediction normally requires shared systems and components.

## Content.Server

Server code is authoritative. It owns persistence, final validation, and server-only systems.

## Content.Client

Client code displays state and handles UI/visual presentation. It cannot be trusted for gameplay authority.

## Fork Placement

Use `{FORK_DIR}` under each assembly for new fork code (`FORK_DIR` from `.agents/fork-config.md`).
