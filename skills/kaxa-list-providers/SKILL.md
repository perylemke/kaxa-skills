---
name: kaxa-list-providers
description: Calls the kaxa MCP tool list_providers before any sandbox work. Use when choosing a provider, checking availability, reading capabilities, or when another kaxa tool fails with a missing feature or unavailable provider.
---

# list_providers

## Overview

Lists registered sandbox providers, whether each can serve requests, the server default, and optional features (`capabilities`).

## When to use

- Start of any kaxa sandbox workflow.
- Before `create_sandbox`, `sync_repository`, snapshots, `publish_api`, `set_url_auth`, `restart`, or `upgrade`.
- After credential or `KAXA_DEFAULT_PROVIDER` changes (restart the MCP server first).

Not for listing sandboxes (`list_sandboxes`) or one sandbox detail (`inspect`).

## Call

No arguments.

Pick a provider with `available: true`. If `available: false`, other tools reject it before calling the provider.

Read `capabilities` booleans (`sync`, `setup`, `api`, `public_url`, `restart`, `upgrade`, `running`, `template`, `snapshot`, `workspace_layout`). When `snapshot` is true, read `snapshot_restore`: `in_place` or `new_sandbox` (not a boolean).

There is no `warnings` field on this tool.

## Result

`providers[]` with `name`, `available`, `default`, and `capabilities`. Exactly one entry may have `default: true`.

## Mistakes

- Calling create/exec/destroy without checking `available`.
- Assuming every provider supports `api`, `snapshot`, or `upgrade`.
- Treating `snapshot_restore` as a capability flag instead of a mode string.
