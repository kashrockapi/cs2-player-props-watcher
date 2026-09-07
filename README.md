# CS2 Player Props Watcher

Free, open-source CS2 player-props watcher for terminal or Discord.
Uses a free KashRock Sandbox key—no card, no scraper maintenance.

## How It Works

## Get a free KashRock API key

This bot uses **your own** KashRock API key.

1. Create a free Sandbox account — no credit card needed  
2. Copy your API key  
3. Paste it into your `.env` file:

```env
KASHROCK_API_KEY=your_key_here
```

[Get your free API key →](https://www.kashrock.com/?utm_source=github&utm_campaign=cs2bot)



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
