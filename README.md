<div align="center">

# Discord Bot Python

**A modern, modular Discord bot built with Python and discord.py**

Ready-to-use commands, error handling, and a clean architecture designed to scale from a small community to a professional server.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.3+-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/davi713albano-coder/discord-bot-python?style=for-the-badge&color=gold)](https://github.com/davi713albano-coder/discord-bot-python/stargazers)
[![Issues](https://img.shields.io/github/issues/davi713albano-coder/discord-bot-python?style=for-the-badge&color=red)](https://github.com/davi713albano-coder/discord-bot-python/issues)

</div>

---

## Commands

| Command | Description | Status |
|---------|-------------|--------|
| `!ping` | Check bot latency in real time | Ready |
| `!info` | Bot info -- library, prefix, server count | Ready |
| `!serverinfo` | Server details -- owner, members, roles, channels | Ready |
| `!help` | List all available commands with embeds | Ready |
| `!play` | Play music in voice channels | Planned |
| `!ai` | AI chat via external API | Planned |
| `!moderation` | Advanced moderation tools | Planned |

---

## Feature Highlights

- **Built-in commands** -- `ping`, `info`, `serverinfo`, and `help` ready out of the box with rich embed responses
- **Global error handler** -- automatically catches missing permissions, missing arguments, and unknown commands
- **Dynamic presence** -- bot status shows `Listening to !help` while online
- **Environment-based config** -- token and prefix loaded from `.env`, never hardcoded
- **Modular architecture** -- single-file design that is easy to extend with cogs
- **Rich embeds** -- all info commands respond with styled Discord embeds, not plain text
- **Bilingual foundation** -- developed in Portuguese (BR), ready for internationalization

---

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip
- Git
- A [Discord Bot Token](https://discord.com/developers/applications)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/davi713albano-coder/discord-bot-python.git
cd discord-bot-python

# 2. Create and activate a virtual environment
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and add your bot token:

```bash
cp .env.example .env
```

Edit `.env`:

```bash
DISCORD_TOKEN=your_token_here
BOT_PREFIX=!
```

To get a token: open the [Discord Developer Portal](https://discord.com/developers/applications), create a New Application, go to Bot, and reset/copy the token.

### Run

```bash
python bot.py
```

You should see:

```
Bot conectado como YourBot#1234
ID: 123456789012345678
Conectado em 1 servidor(es)
```

---

## Usage

Once the bot is running and invited to your server, use any command with the configured prefix (default `!`):

```
!ping          -> Pong! Latencia: 45ms
!info          -> Shows bot info embed (library, prefix, commands, servers)
!serverinfo    -> Shows server embed (owner, members, roles, channels, creation date)
!help          -> Lists all available commands
```

### Error Handling

The bot automatically handles common errors:

- **CommandNotFound** -- silently ignored (no spam in chat)
- **MissingPermissions** -- tells the user they lack permission
- **MissingRequiredArgument** -- tells the user which argument is missing
- **All other errors** -- displayed to the user with the error message

---

## How It Works

```
  Discord Gateway
       |
   discord.py
       |
     bot.py
       |
  +----+----+----+----+
  | ping | info | server | help |
  +----+----+----+----+
       |
  on_command_error  (global handler)
```

1. **Connection** -- `bot.py` loads the token from `.env` and connects to the Discord gateway
2. **Intents** -- `message_content` and `members` intents are enabled for reading messages and member info
3. **Commands** -- each `@bot.command()` decorator registers a command with automatic argument parsing
4. **Embeds** -- `info`, `serverinfo`, and `help` respond with structured Discord embeds for a clean look
5. **Error handler** -- `on_command_error` catches and formats all command errors globally

---

## Project Structure

```
discord-bot-python/
  .env.example        # Template for environment variables
  .gitignore           # Files ignored by git
  bot.py               # Bot entry point and all commands
  requirements.txt     # Python dependencies
  LICENSE              # MIT License
  README.md            # This file
```

---

## Roadmap

- [ ] Music system (YouTube, Spotify, SoundCloud)
- [ ] AI integration (ChatGPT and others)
- [ ] Automatic moderation (spam filter, anti-raid)
- [ ] Web dashboard for configuration
- [ ] Economy and points system
- [ ] Leveling and XP system
- [ ] TTS (Text to Speech)
- [ ] Docker support
- [ ] CI/CD with GitHub Actions
- [ ] Advanced logging
- [ ] Multi-language support (i18n)
- [ ] External API integrations

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit with [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add music command"
git commit -m "fix: correct ping latency calculation"
git commit -m "docs: update README"
```

4. Push to the branch: `git push origin feat/my-feature`
5. Open a Pull Request

### Commit Conventions

| Prefix | Use | Example |
|--------|----|---------|
| `feat:` | New feature | `feat: add play command` |
| `fix:` | Bug fix | `fix: correct ping latency` |
| `docs:` | Documentation | `docs: update README` |
| `style:` | Formatting, no code change | `style: format with black` |
| `refactor:` | Code refactoring | `refactor: simplify command handler` |
| `test:` | Add or fix tests | `test: add tests for ping` |
| `chore:` | Build or CI tasks | `chore: add GitHub Actions` |

---

## License

[MIT](LICENSE) -- see the LICENSE file for details.

---

<div align="center">

Built by [davi713albano-coder](https://github.com/davi713albano-coder)

If this project helped you, consider giving it a star.

</div>
