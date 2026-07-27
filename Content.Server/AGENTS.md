# Content.Server Agent Rules

Use `ss14-client-server-shared`, `ss14-ecs-basics`, and domain skills for server-only systems.

- Put new {FORK_NAME} server code under `Content.Server/{FORK_DIR}` (see `.agents/fork-config.md`).
- Server code is authoritative; validate all client input.
- Use server-only code for persistence, admin/server services, and systems that cannot be predicted.
- If an upstream server file must be changed, wrap the exact diff in {EDIT_MARKER}-Start / {EDIT_MARKER}-End markers.
