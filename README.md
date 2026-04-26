# wariobot

### Quick Description
Just a personal tool for automating certain tasks through Discord. For example, starting/stopping a dedicated game server shared with friends.

Currently, the extent of the functionality is replying to a `!hello` message, and starting and stopping an instance of a Windrose dedicated server.

### Install
##### (This was written off the top of my head the day after setup, I'll verify and improve later)
- Copy repo to Windows machine where Windrose dedicated server is installed.
- Create venv at repo root directory, load requirements.
- Copy or rename `env` to `.env`.
- Add a Discord bot token from your Discord dev portal, ensure bot is allowed to view usernames, write messages, and read messages.
- Invite bot to Discord server.
- Add a dedicated channel ID to broadcastChannel to restrict system messages to (not replies).
- Add path to windroseServerExe. I strongly recommend using the WindroseServer-Win64-Shipping.exe file until this tool is further developed, this
	can be found at `*\\SteamLibrary\\steamapps\\common\\Windrose Dedicated Server\\R5\\Binaries\\Win64\\WindroseServer-Win64-Shipping.exe`
- Run tool from repo directory with `python3 ./bot.py`

### Immediate Plans
- Improve pythonics, structure, commenting, etc. Just do better.
- Improve process control.
	- By identifying running processes, I can check if a server is already running that the bot didn't start.
	- Terminate the task tree, allowing for edge cases where child or parent tasks are running.
	- Will let us use `WindroseServer.exe`, simplifying setup. As-is, it won't properly terminate that task because it spawns the child `*-Win64-Shipping.exe'.
- Add optional flags.
	- Launch server along with bot, if one is not running.
	- Launch server quietly (maybe should be default, then option to launch with greeting).
	- Launch server in background.
	- Launch a silent bot (maybe?).
	- Limit idle CPU usage.
- Error handling and logs.
- Support multiple servers.
- Server status/health monitoring.
	- Enables implementing a server timeout if no connections are active for a configurable amount of time.
- Support install on Linux.
- Optional server and/or personal save backup features.
- Support server functions on a remote PC (in the same LAN).

### Future
- Plex integration (only for me).
- Whatever other game servers my friends and I want to have available.

