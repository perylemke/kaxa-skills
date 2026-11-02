# kaxa-skills

Agent Skills for AI clients that use [kaxa](https://github.com/perylemke/kaxa) sandboxes over the Model Context Protocol (`kaxa mcp`). Each skill matches one MCP tool and teaches judgment the tool schema does not enforce: capabilities, sync boundaries, destructive calls, and workspace paths.

Argument details live in the running kaxa binary (tool descriptions and JSON schema). Human-oriented reference: [kaxa docs/agent.md](https://github.com/perylemke/kaxa/blob/main/docs/agent.md).

## Skills

| Skill directory | MCP tool |
| --- | --- |
| `kaxa-list-providers` | `list_providers` |
| `kaxa-create-sandbox` | `create_sandbox` |
| `kaxa-sync-repository` | `sync_repository` |
| `kaxa-exec` | `exec` |
| `kaxa-list-sandboxes` | `list_sandboxes` |
| `kaxa-inspect` | `inspect` |
| `kaxa-restart` | `restart` |
| `kaxa-upgrade` | `upgrade` |
| `kaxa-destroy` | `destroy` |
| `kaxa-create-snapshot` | `create_snapshot` |
| `kaxa-list-snapshots` | `list_snapshots` |
| `kaxa-restore-snapshot` | `restore_snapshot` |
| `kaxa-delete-snapshot` | `delete_snapshot` |
| `kaxa-publish-api` | `publish_api` |
| `kaxa-set-url-auth` | `set_url_auth` |

Shared workspace paths by provider: [skills/kaxa-exec/workspaces.md](skills/kaxa-exec/workspaces.md).

## Install

Requires [Node.js](https://nodejs.org/) 22.20 or later. Uses the open [Skills CLI](https://github.com/vercel-labs/skills) (`npx skills`), the same flow as [Daytona agent skills](https://www.daytona.io/docs/en/agent-skills/).

List skills in this repository without installing:

```bash
npx skills add perylemke/kaxa-skills --list
```

Install all 15 skills globally (available in every project; recommended):

```bash
npx skills add perylemke/kaxa-skills --skill '*' -g -y
```

Install one skill for Cursor globally:

```bash
npx skills add perylemke/kaxa-skills --skill kaxa-exec -a cursor -g -y
```

Add `-a claude-code` (or another agent the CLI supports) instead of `-a cursor` when needed. Omit `-g` to install into the current project only.

`kaxa-create-sandbox`, `kaxa-sync-repository`, and `kaxa-publish-api` link to [workspaces.md](skills/kaxa-exec/workspaces.md) inside `kaxa-exec`. Prefer installing the full set (`--skill '*'`) rather than a single skill.

### Manual

Copy or symlink each folder under `skills/` into your agent skills directory (`~/.cursor/skills/`, `.cursor/skills/`, or the path your client documents).

Connect `kaxa mcp` in the client before relying on these skills; they assume MCP tools are available.

## Check

From the repository root:

```bash
python3 scripts/check_skills.py
```

Expect `ok` and exit code 0.

## License

MIT — see [LICENSE](LICENSE).
