---
name: kaxa-create-sandbox
description: Calls the kaxa MCP tool create_sandbox. Use when starting isolated remote work, copying a Git repo with sync, publishing an API at create time, or when local editor tools cannot reach the sandbox filesystem.
---

# create_sandbox

## Overview

Creates a named sandbox. With `sync: true`, copies a local Git repository, installs toolchains and dependencies, and returns `work_dir`. `no_install` copies the repository and skips both; the dependency commands come back in `skipped_commands`.

## When to use

- First sandbox for a task with repository copy and install.
- Empty sandbox without sync (provider-specific exec layout).

Use `sync_repository` for an additional repo on an existing synced sandbox. Use `exec` after create for commands.

Workspace paths: [workspaces.md](../kaxa-exec/workspaces.md).

## Call

Call `list_providers` first. Provider must be `available`.

Required `name`. Optional `provider`.

- `dir` and `no_install` require `sync`.
- `work_dir` in the result only when `sync` is true.
- `api` requires `api_cmd`; default `api_port` 8000; port 8080 reserved when `running` is true. Blaxel rejects ports 80, 443, and 8080.
- `public` with `running` and without `api` is refused (tmux has no login). `running` and `public` only when those capabilities are true. Blaxel has neither.
- `template` only when `capabilities.template` is true (E2B, Docker, Daytona, Blaxel). A Blaxel template keeps user `root` and home `/root`.

`api_env`: `KEY=VALUE`, or bare `KEY` only if listed in server `KAXA_MCP_API_ENV`. Reserved: `HOME`, `USER`, `PATH`, and names starting with `KAXA_`, `MODAL_TOKEN_`, `FLY_`, `SPRITES_`. No commas in values.

`env`: names only, never `KEY=VALUE`. Each name is copied from the server environment only when it is listed in `KAXA_MCP_ENV`. An empty allowlist refuses every name. `env_file`: pass a dotenv path inside the server root (`KAXA_MCP_ROOT` or the working directory). Do not open the file and do not paste secrets. Names in `env` replace the same key from the file. Do not print the environment with `exec`.

Create with sync can take minutes; progress goes to MCP stderr.

## Result

`id`, `provider`, optional `work_dir`, `skipped_commands` (with `no_install`), optional `url` and `auth`, optional `env_keys` (names only, never values).

Failed copy, install, or API publish deletes the sandbox. Failed `public` change keeps the sandbox; the error says so.

## Mistakes

- `dir` without `sync`.
- Assuming local file edits appear in the sandbox.
- Calling without checking `sync` / `api` / `template` capabilities.
- Pasting secrets into `api_env` instead of allowlisted bare keys.
- Putting `KEY=VALUE` in `env`, opening `env_file`, or printing variables with `exec`.
