---
name: kaxa-publish-api
description: Calls the kaxa MCP tool publish_api to start an HTTP service in an existing sandbox. Use when exposing an app on the sandbox URL after list_providers shows api capability, not at initial create unless using create_sandbox api flags.
---

# publish_api

## Overview

Starts one HTTP service in an existing sandbox and routes the sandbox URL to it.

## When to use

- Publish or republish API after sandbox exists.

Alternative: `create_sandbox` with `api` and `api_cmd` at create time.

Workspace paths: [workspaces.md](../kaxa-exec/workspaces.md).

## Call

`list_providers`: need `api` capability (not Modal).

Required `name`, `api_cmd` (argv). Process must listen on `0.0.0.0` and `api_port` (default 8000). Optional `provider`, `api_env` (same rules as create), `work_dir` (absolute path inside sandbox; empty uses provider home from layout).

E2B: publish port must match create-time API port when applicable.

Blaxel rejects ports 80, 443, and 8080. Its preview is named `kaxa-api` and is always public.

Public preview URLs on E2B, Docker, Daytona, and Blaxel are reachable by anyone with the link.

## Result

`id`, `provider`, `status` (e.g. published), and `url` and `auth` when the provider reports them. A failed inspect after a successful publish leaves the service up and omits the URL.

## Mistakes

- Calling on Modal (`api` false).
- Relative `work_dir` or path traversal.
- Reserved or unallowlisted `api_env` keys.
- Binding service to localhost only inside container.
