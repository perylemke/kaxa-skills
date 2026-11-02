---
name: kaxa-list-sandboxes
description: Calls the kaxa MCP tool list_sandboxes to enumerate sandboxes. Use when finding existing sandbox names, checking status across providers, or before inspect when the name is unknown.
---

# list_sandboxes

## Overview

Returns sandboxes from configured providers, optionally filtered to one provider.

## When to use

- Discover names before `inspect`, `exec`, or lifecycle tools.
- Inventory sandboxes across accounts.

Use `inspect` for URL, auth, and timestamps on one sandbox. Use `list_providers` first only when you need to confirm a provider name.

## Call

Optional `provider` from `list_providers`. Omit to list every provider that has credentials, in provider name order.

Each item includes `provider`; use it when calling other tools on that sandbox.

## Result

`sandboxes[]` with `id`, `provider`, `status`, `labels`.

Without `provider`, partial failures appear in `warnings` while other providers still list. If every provider fails, the call is an error.

## Mistakes

- Assuming a single global namespace; names are scoped per provider.
- Ignoring `warnings` when some providers failed.
- Using list output as proof a sandbox still exists before a destructive call without user confirmation.
