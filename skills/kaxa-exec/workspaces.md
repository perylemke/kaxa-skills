# Sandbox workspace paths

After `create_sandbox` with `sync: true`, the response `work_dir` is where the repository lives. `exec` starts in the provider workspace directory (parent of `work_dir`), not in `work_dir`. Run project commands with `cd <work_dir>`.

| Provider | User | With `sync` (`work_dir`) | Without `sync` (exec start) |
| --- | --- | --- | --- |
| sprites | sprite | `/home/sprite/workspace/<repo>` | sprite home / workspace per provider |
| modal | modal | `/home/modal/workspace/<repo>` | root at image root; `sync_repository` fails if create had no `sync` |
| e2b | user | `/home/user/workspace/<repo>` | `/home/user` |
| docker | agent | `/home/agent/workspace/<repo>` | image default (not workspace) |
| daytona | daytona | `/home/daytona/workspace/<repo>` | image default (not workspace) |
| blaxel | root | `/root/workspace/<repo>` | `/root` |

`<repo>` is the basename of the copied local directory.

Custom `template` images must keep the same user and home as the provider base layout (E2B: `user`, `/home/user`; Docker: `agent`, `/home/agent`; Daytona: `daytona`, `/home/daytona`; Blaxel: `root`, `/root`). kaxa does not detect a wrong user.

`publish_api` with empty `work_dir` uses the provider home from workspace layout, not `work_dir` from create.
