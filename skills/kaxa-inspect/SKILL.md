---
name: kaxa-inspect
description: Calls the kaxa MCP tool inspect for one sandbox. Use when checking status, labels, URL, or URL auth, or after list_sandboxes when detail is needed.
---

# inspect

## Overview

Read-only detail for one sandbox by name.

## When to use

- Confirm status, labels, public URL, or auth mode.
- Verify a sandbox exists before `exec` or API publish.

Does not create sandboxes (`create_sandbox`) or list all (`list_sandboxes`).

## Call

Required `name`. Optional `provider` (defaults to server default).

Provider must be `available` from `list_providers`.

## Result

`id`, `provider`, `status`, `labels`, optional `organization`, `url`, `auth`, `created_at`, `updated_at`.

Missing sandbox or unavailable provider is a tool error; read the parenthesized hint.

## Mistakes

- Calling inspect instead of create when no sandbox exists yet.
- Omitting `provider` when the same name could exist on another backend (rare but possible across separate accounts).
