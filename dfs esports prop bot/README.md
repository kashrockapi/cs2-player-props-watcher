# CS2 Player Props Watcher

Get your free API key

This bot uses your personal KashRock API key.
Create a free Sandbox account—no card required—then add your key to `.env`.

```bash
KASHROCK_API_KEY=your_key_here
```

Get a free key at KashRock → https://www.kashrock.com/#pricing

Free, open-source CS2 player-props watcher for terminal or Discord.
Uses a free KashRock Sandbox key—no card, no scraper maintenance.

## How It Works

```
Reddit / GitHub post
        ↓
Clone or download the free bot
        ↓
"Get a free KashRock API key"
        ↓
Create account / Google sign-in
        ↓
Copy their Sandbox key
        ↓
Paste it into .env
        ↓
Run the CS2 watcher
        ↓
Want more coverage or capacity?
        ↓
Upgrade their own KashRock plan
```

## What You Provide

- The free/open-source bot.
- The code and setup docs.
- A sample response with fake/redacted values.
- Optional filters and Discord output.
- The free CS2 Sandbox access path.

## What You Do Not Provide

- A shared live key.
- Unlimited requests.
- Paid LoL/Dota data through the free bot.
- A hosted bot that consumes your data indefinitely.

That makes the bot an **acquisition asset** — not a recurring cost or security risk.

## Quick Start

```bash
git clone <repo-url>
cd cs2-prop-watcher
cp .env.example .env
# Edit .env and add your KashRock API key
pip install -r requirements.txt
python watcher.py
```

## Configuration

| Variable | Description | Default |
|---|---|---|
| `KASHROCK_API_KEY` | Your KashRock Sandbox key | *(required)* |
| `POLL_INTERVAL` | Seconds between polls | `60` |
| `DISCORD_WEBHOOK_URL` | Optional Discord webhook URL | *(empty)* |

## Output

```
======================================================================
  CS2 PROPS — kashrock | 3 prop(s) | 2026-09-07 12:00:00 UTC
======================================================================
  fear (Fnatic) | ESPORTS_KILLS_MAPS_1_2 | Line: 25.5 | OVER @ -118 | Book: PrizePicks | Event: 2026-09-07T13:30:00Z
    IDs: prop=kr_prop_5992b0df9d7afc33 | offer=kr_prop_5992b0df9d7afc33_6_over | event=kr_ev_d9410a855f83

  mezii (Team Vitality) | CS2_HEADSHOTS_MAPS_1_2 | Line: 14.5 | OVER @ -105 | Book: Betr | Event: 2026-09-07T13:55:00Z
    IDs: prop=kr_prop_883ba7a1e090 | offer=kr_prop_883ba7a1e090_6_over | event=kr_ev_abc123
======================================================================
```

## Discord Output

Set `DISCORD_WEBHOOK_URL` in `.env` to receive prop updates as Discord embeds.

## Requirements

- Python 3.10+
- KashRock Sandbox key (free, no credit card)

## License

MIT
