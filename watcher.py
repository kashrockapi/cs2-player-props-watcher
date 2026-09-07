#!/usr/bin/env python3
"""CS2 Player Props Watcher — polls KashRock for live CS2 player props."""

import os
import sys
import time
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KASHROCK_API_KEY")
BASE_URL = "https://kashrock.up.railway.app"
PROPS_ENDPOINT = f"{BASE_URL}/v6/esports/props?game=cs2"
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "60"))
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL", "")

if not API_KEY:
    print("Error: KASHROCK_API_KEY not set. Copy .env.example to .env and add your key.")
    print("Get a free key at https://www.kashrock.com/#pricing")
    sys.exit(1)

HEADERS = {"X-API-Key": API_KEY}


def fetch_props():
    try:
        resp = requests.get(PROPS_ENDPOINT, headers=HEADERS, timeout=15)
        if resp.status_code == 429:
            print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Rate limited. Waiting...")
            time.sleep(30)
            return None
        if resp.status_code == 401:
            print("Error: Invalid API key. Check your KASHROCK_API_KEY.")
            sys.exit(1)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Request failed: {e}")
        return None


def format_prop(p):
    direction = p.get("direction", "N/A")
    sign = "+" if p.get("odds", 0) > 0 else ""
    odds_str = f"{sign}{p.get('odds', 'N/A')}"
    return (
        f"  {p.get('player_name', '?')} ({p.get('team', '?')}) "
        f"| {p.get('stat_type', '?')} "
        f"| Line: {p.get('line', '?')} "
        f"| {direction.upper()} @ {odds_str} "
        f"| Book: {p.get('book_name', '?')} "
        f"| Event: {p.get('event_time', 'N/A')}"
    )


def display_props(data):
    props = data.get("props", [])
    source = data.get("source", "kashrock")
    sport = data.get("sport", "cs2")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"\n{'='*70}")
    print(f"  CS2 PROPS — {source} | {len(props)} prop(s) | {ts}")
    print(f"{'='*70}")

    if not props:
        print("  No active props found. Waiting for live matches...")
        return

    for p in props:
        print(format_prop(p))
        prop_id = p.get("propId", "")
        offer_id = p.get("offerId", "")
        event_id = p.get("eventId", "")
        print(f"    IDs: prop={prop_id} | offer={offer_id} | event={event_id}")
        print()

    if DISCORD_WEBHOOK:
        send_discord(data, props)


def send_discord(data, props):
    if not DISCORD_WEBHOOK:
        return
    embed = {
        "title": "CS2 Props Update",
        "description": f"{len(props)} active prop(s) detected.",
        "color": 0x00ff88,
        "fields": [
            {
                "name": p.get("player_name", "?"),
                "value": f"{p.get('team', '?')} | {p.get('stat_type', '?')} | Line: {p.get('line', '?')} | {p.get('direction', '?').upper()} @{p.get('odds', '?')}",
                "inline": True,
            }
            for p in props[:10]
        ],
        "footer": {"text": "Powered by KashRock — get your free key"},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    payload = {"embeds": [embed]}
    try:
        requests.post(DISCORD_WEBHOOK, json=payload, timeout=10)
    except Exception:
        pass


def run():
    print("CS2 Props Watcher — started")
    print(f"Polling every {POLL_INTERVAL}s | Source: {BASE_URL}")
    print(f"Get your free key: https://www.kashrock.com/#pricing\n")

    while True:
        data = fetch_props()
        if data:
            display_props(data)
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nWatcher stopped.")
        sys.exit(0)
