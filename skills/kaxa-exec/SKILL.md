---
name: kaxa-exec
description: Calls the kaxa MCP tool exec to run an argv in a sandbox. Use when building, testing, or editing inside a kaxa sandbox, or when a command needs a shell, times out, or returns truncated output.
---

# exec

## Overview

Runs `command` as argv in the sandbox and returns streams and exit code.

## When to use

- Tests, builds, package installs, file edits via shell tools.

Local editor or host shell tools do not change sandbox files; sandbox edits do not sync back. Move code with `git` inside `exec`, or new `create_sandbox` with `sync`.

Workspace paths: [workspaces.md](workspaces.md).

## Call

Required `name` and `command` (argv; first element is the binary). Optional `provider`, `timeout_seconds` (default 1800, max 7200).

Shell features require explicit `["bash", "-c", "cd <work_dir> && ..."]`. Never pass a single string expecting shell parsing.

With sync create, start project work from `work_dir` via `cd`.

## Result

`exit_code`, `stdout`, `stderr`, `truncated`. Non-zero exit is success of the tool with failed command semantics.

Tool error: missing sandbox, provider failure, or timeout. No stdin (EOF). Each stream keeps first 256 KiB; remainder dropped with marker when `truncated` is true.

## Mistakes

- Editing files on the host expecting sandbox visibility.
- Treating test failure exit code as MCP tool failure.
- Omitting `cd <work_dir>` for project commands.
- Relying on stdin.
