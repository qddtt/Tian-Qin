#!/usr/bin/env python3
"""Hermes no-agent cron script for Qin Tian's website analytics."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


ENV_FILE = Path("/etc/qin-site-analytics.env")
SUMMARY_URL = "http://127.0.0.1:18080/summary?days=1"
ADMIN_URL = "https://tianqin.netlify.app/site-analytics/admin?days=7"


def read_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def fetch_summary(token: str) -> dict:
    request = urllib.request.Request(
        SUMMARY_URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "Hermes site analytics monitor",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def table(rows: list[dict], columns: list[tuple[str, str]]) -> str:
    if not rows:
        return "None."
    header = "| " + " | ".join(label for label, _ in columns) + " |"
    divider = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, divider]
    for row in rows:
        values = [str(row.get(key, "") or "-").replace("\n", " ") for _, key in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def main() -> int:
    if not ENV_FILE.exists():
        print("Website analytics monitor failed: /etc/qin-site-analytics.env is missing.")
        return 1

    config = read_env(ENV_FILE)
    token = config.get("ANALYTICS_API_TOKEN", "")
    if not token:
        print("Website analytics monitor failed: ANALYTICS_API_TOKEN is not configured.")
        return 1

    try:
        summary = fetch_summary(token)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"Website analytics monitor failed: {exc}")
        return 1

    pageviews = int(summary.get("pageviews") or 0)
    visitors = int(summary.get("visitors") or 0)
    if pageviews == 0:
        print("[SILENT]\nWebsite analytics: no visits in the last 24 hours.")
        return 0

    print("# Website analytics daily report")
    print()
    print(f"Site: {summary.get('site', 'tianqin.netlify.app')}")
    print(f"Window: last {summary.get('days', 1)} day")
    print(f"Pageviews: {pageviews}")
    print(f"Visitors: {visitors}")
    print(f"Dashboard: {ADMIN_URL}")
    print()
    print("## Top pages")
    print(table(summary.get("top_pages", [])[:8], [("Path", "path"), ("Views", "views"), ("Visitors", "visitors")]))
    print()
    print("## Referrers")
    print(table(summary.get("top_referrers", [])[:8], [("Referrer", "referrer_host"), ("Views", "views")]))
    print()
    print("## Recent visits")
    print(
        table(
            summary.get("recent", [])[:8],
            [("UTC time", "ts_utc"), ("Path", "path"), ("Referrer", "referrer_host")],
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
