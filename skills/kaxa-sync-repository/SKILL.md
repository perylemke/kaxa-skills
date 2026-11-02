---
name: kaxa-sync-repository
description: Calls the kaxa MCP tool sync_repository to add another Git repo to a synced sandbox. Use when a second repository is needed, not when refreshing local changes or replacing an existing copy.
---

# sync_repository

## Overview

Copies one more local Git repository into a sandbox that was created with `sync`, then installs dependencies unless `no_install`.

## When to use

- Monorepo or multi-repo work inside one sandbox.

Does not refresh an already copied repo (use new sandbox with `sync` or `git` via `exec`). Never replaces an existing directory name in the sandbox.

Workspace paths: [workspaces.md](../kaxa-exec/workspaces.md).

## Call

`list_providers`: provider needs `sync` capability.

Required `name` (sandbox). Optional `provider`, `dir` (defaults to MCP server working directory), `no_install`.

Modal sandboxes created without `sync` reject this tool.

`dir` must lie inside a Git repo that contains or sits below the server working directory. Server cwd must not be `$HOME` or `/`.

Failed copy or install keeps the sandbox (other repos may remain).

## Result

`id`, `provider`, `work_dir` for the new repository. `skipped_commands` when `no_install` is true.

## Mistakes

- Expecting to update code after local edits without re-sync or git inside sandbox.
- Re-syncing the same repo name (error: directory exists).
- Using on Modal create-without-sync sandboxes.
