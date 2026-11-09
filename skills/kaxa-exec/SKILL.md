---
name: kaxa-exec
description: Calls the kaxa MCP tool exec to run an argv in a sandbox. Use when building, testing, or editing inside a kaxa sandbox, or when a command needs a working directory, a shell, times out, or returns truncated output.
---

# exec

## Overview

Runs `command` as argv in the sandbox and returns streams and exit code.

## When to use

- Tests, builds, package installs, file edits via shell tools.

Local editor or host shell tools do not change sandbox files; sandbox edits do not sync back. Move code with `git` inside `exec`, or new `create_sandbox` with `sync`.

Workspace paths: [workspaces.md](workspaces.md).

## Call

Required `name` and `command` (argv; first element is the binary). Optional `provider`, `cwd`, `timeout_seconds` (default 1800, max 7200).

`cwd` is an absolute path inside the sandbox. Pass the `work_dir` from `create_sandbox` or `sync_repository`. Omit it and the command starts in the provider workspace or home.

Shell features require explicit `["bash", "-c", "..."]`. Never pass a single string expecting shell parsing. Use `cwd` for the directory; reserve `bash -c` for pipes, globs, and redirection.

## Result

`exit_code`, `stdout`, `stderr`, `truncated`, and `timed_out` when the command was stopped. Non-zero exit is success of the tool with failed command semantics.

Tool error: missing sandbox or provider failure. A timeout is a result with `timed_out` true, `exit_code` `-1`, and the output captured so far. No stdin (EOF). Each stream keeps the last 256 KiB; earlier bytes are dropped with a marker when `truncated` is true.

## Mistakes

- Editing files on the host expecting sandbox visibility.
- Treating test failure exit code as MCP tool failure.
- Omitting `cwd` set to `work_dir` for project commands.
- Relying on stdin. Blaxel has no MCP console; the interactive terminal is the CLI `kaxa console`.
