#!/usr/bin/env python3
"""Small self-hosted analytics service for Qin Tian's personal site."""

from __future__ import annotations

import base64
import hashlib
import hmac
import html
import json
import os
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


DEFAULT_ALLOWED_ORIGINS = "https://tianqin.netlify.app,http://127.0.0.1:1313,http://localhost:1313"
MAX_BODY_BYTES = 16 * 1024


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


DB_PATH = env("ANALYTICS_DB", "/var/lib/qin-site-analytics/analytics.sqlite3")
SALT = env("ANALYTICS_SALT", "change-this-analytics-salt")
API_TOKEN = env("ANALYTICS_API_TOKEN")
ADMIN_USER = env("ANALYTICS_ADMIN_USER", "admin")
ADMIN_PASSWORD = env("ANALYTICS_ADMIN_PASSWORD")
SITE_NAME = env("ANALYTICS_SITE", "tianqin.netlify.app")
TIMEZONE_NAME = env("ANALYTICS_TIMEZONE", "Asia/Shanghai")
try:
    TZ = ZoneInfo(TIMEZONE_NAME)
except ZoneInfoNotFoundError:
    TZ = timezone(timedelta(hours=8), TIMEZONE_NAME)
ALLOWED_ORIGINS = {
    origin.rstrip("/")
    for origin in env("ANALYTICS_ALLOWED_ORIGINS", DEFAULT_ALLOWED_ORIGINS).split(",")
    if origin.strip()
}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def local_date(dt: datetime) -> str:
    return dt.astimezone(TZ).date().isoformat()


def trim(value: Any, limit: int) -> str:
    if not isinstance(value, str):
        return ""
    value = value.strip()
    return value[:limit]


def int_or_zero(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def hash_value(value: str) -> str:
    if not value:
        return ""
    digest = hmac.new(SALT.encode("utf-8"), value.encode("utf-8"), hashlib.sha256).hexdigest()
    return digest[:32]


def client_ip(handler: BaseHTTPRequestHandler) -> str:
    forwarded = handler.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",", 1)[0].strip()
    real_ip = handler.headers.get("X-Real-IP", "")
    if real_ip:
        return real_ip.strip()
    return handler.client_address[0]


def ensure_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS pageviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ts_utc TEXT NOT NULL,
                local_date TEXT NOT NULL,
                path TEXT NOT NULL,
                title TEXT NOT NULL,
                referrer TEXT NOT NULL,
                referrer_host TEXT NOT NULL,
                visitor_hash TEXT NOT NULL,
                ip_hash TEXT NOT NULL,
                user_agent TEXT NOT NULL,
                language TEXT NOT NULL,
                screen_width INTEGER,
                created_at INTEGER NOT NULL
            )
            """
        )
        db.execute("CREATE INDEX IF NOT EXISTS idx_pageviews_created_at ON pageviews(created_at)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_pageviews_local_date ON pageviews(local_date)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_pageviews_path ON pageviews(path)")
        db.commit()


def db_connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def authorized_summary(handler: BaseHTTPRequestHandler, query: dict[str, list[str]]) -> bool:
    if not API_TOKEN:
        return False
    auth = handler.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return hmac.compare_digest(auth.removeprefix("Bearer ").strip(), API_TOKEN)
    token = query.get("token", [""])[0]
    return hmac.compare_digest(token, API_TOKEN)


def authorized_admin(handler: BaseHTTPRequestHandler) -> bool:
    if not ADMIN_PASSWORD:
        return False
    auth = handler.headers.get("Authorization", "")
    if not auth.startswith("Basic "):
        return False
    try:
        decoded = base64.b64decode(auth.removeprefix("Basic ").strip()).decode("utf-8")
    except Exception:
        return False
    username, _, password = decoded.partition(":")
    return hmac.compare_digest(username, ADMIN_USER) and hmac.compare_digest(password, ADMIN_PASSWORD)


def parse_days(query: dict[str, list[str]], default: int = 7) -> int:
    try:
        days = int(query.get("days", [str(default)])[0])
    except ValueError:
        days = default
    return max(1, min(days, 90))


def summarize(days: int) -> dict[str, Any]:
    since = int(time.time()) - days * 86400
    with db_connect() as db:
        totals = db.execute(
            """
            SELECT
                COUNT(*) AS pageviews,
                COUNT(DISTINCT COALESCE(NULLIF(visitor_hash, ''), ip_hash)) AS visitors
            FROM pageviews
            WHERE created_at >= ?
            """,
            (since,),
        ).fetchone()
        pages = db.execute(
            """
            SELECT path, COUNT(*) AS views,
                   COUNT(DISTINCT COALESCE(NULLIF(visitor_hash, ''), ip_hash)) AS visitors
            FROM pageviews
            WHERE created_at >= ?
            GROUP BY path
            ORDER BY views DESC, path ASC
            LIMIT 12
            """,
            (since,),
        ).fetchall()
        referrers = db.execute(
            """
            SELECT referrer_host, COUNT(*) AS views
            FROM pageviews
            WHERE created_at >= ? AND referrer_host != ''
            GROUP BY referrer_host
            ORDER BY views DESC, referrer_host ASC
            LIMIT 12
            """,
            (since,),
        ).fetchall()
        daily = db.execute(
            """
            SELECT local_date, COUNT(*) AS views,
                   COUNT(DISTINCT COALESCE(NULLIF(visitor_hash, ''), ip_hash)) AS visitors
            FROM pageviews
            WHERE created_at >= ?
            GROUP BY local_date
            ORDER BY local_date DESC
            LIMIT 31
            """,
            (since,),
        ).fetchall()
        recent = db.execute(
            """
            SELECT ts_utc, path, title, referrer_host, language, screen_width
            FROM pageviews
            WHERE created_at >= ?
            ORDER BY created_at DESC, id DESC
            LIMIT 20
            """,
            (since,),
        ).fetchall()
    return {
        "site": SITE_NAME,
        "generated_at": utc_now().isoformat(),
        "timezone": str(TZ),
        "days": days,
        "pageviews": int(totals["pageviews"] or 0),
        "visitors": int(totals["visitors"] or 0),
        "top_pages": [dict(row) for row in pages],
        "top_referrers": [dict(row) for row in referrers],
        "daily": [dict(row) for row in daily],
        "recent": [dict(row) for row in recent],
    }


def render_table(headers: list[str], rows: list[dict[str, Any]], fields: list[str]) -> str:
    if not rows:
        return '<p class="empty">No data yet.</p>'
    head = "".join(f"<th>{html.escape(label)}</th>" for label in headers)
    body = []
    for row in rows:
        cells = "".join(f"<td>{html.escape(str(row.get(field, '')))}</td>" for field in fields)
        body.append(f"<tr>{cells}</tr>")
    return f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>"


def render_admin(summary: dict[str, Any]) -> bytes:
    cards = (
        f'<div class="card"><span>Pageviews</span><strong>{summary["pageviews"]}</strong></div>'
        f'<div class="card"><span>Visitors</span><strong>{summary["visitors"]}</strong></div>'
        f'<div class="card"><span>Window</span><strong>{summary["days"]}d</strong></div>'
    )
    pages = render_table(["Path", "Views", "Visitors"], summary["top_pages"], ["path", "views", "visitors"])
    referrers = render_table(["Referrer", "Views"], summary["top_referrers"], ["referrer_host", "views"])
    recent = render_table(
        ["UTC time", "Path", "Title", "Referrer", "Lang", "Width"],
        summary["recent"],
        ["ts_utc", "path", "title", "referrer_host", "language", "screen_width"],
    )
    daily = render_table(["Date", "Views", "Visitors"], summary["daily"], ["local_date", "views", "visitors"])
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(SITE_NAME)} analytics</title>
  <style>
    :root {{ color-scheme: light; --ink:#172033; --muted:#687085; --line:#d9dee8; --bg:#f7f8fb; --card:#fff; --accent:#1f6feb; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font-family:Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background:var(--bg); color:var(--ink); }}
    main {{ width:min(1120px, calc(100% - 32px)); margin:36px auto 56px; }}
    header {{ display:flex; gap:16px; align-items:flex-end; justify-content:space-between; margin-bottom:24px; }}
    h1 {{ margin:0; font-size:28px; letter-spacing:0; }}
    p {{ color:var(--muted); margin:6px 0 0; }}
    a {{ color:var(--accent); text-decoration:none; }}
    .cards {{ display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:14px; margin-bottom:18px; }}
    .card {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .card span {{ display:block; color:var(--muted); font-size:13px; }}
    .card strong {{ display:block; margin-top:8px; font-size:30px; }}
    section {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:18px; margin-top:14px; overflow-x:auto; }}
    h2 {{ font-size:18px; margin:0 0 12px; }}
    table {{ width:100%; border-collapse:collapse; font-size:14px; }}
    th, td {{ padding:10px 8px; border-top:1px solid var(--line); text-align:left; vertical-align:top; }}
    th {{ color:var(--muted); font-weight:650; }}
    .empty {{ margin:0; padding:10px 0; }}
    .toolbar {{ display:flex; gap:8px; flex-wrap:wrap; }}
    .toolbar a {{ border:1px solid var(--line); border-radius:999px; padding:7px 11px; background:#fff; color:var(--ink); font-size:14px; }}
    @media (max-width: 720px) {{ .cards {{ grid-template-columns:1fr; }} header {{ display:block; }} .toolbar {{ margin-top:14px; }} }}
  </style>
</head>
<body>
  <main>
    <header>
      <div>
        <h1>{html.escape(SITE_NAME)} analytics</h1>
        <p>Generated {html.escape(summary["generated_at"])} UTC, timezone {html.escape(summary["timezone"])}.</p>
      </div>
      <nav class="toolbar"><a href="?days=1">1d</a><a href="?days=7">7d</a><a href="?days=30">30d</a></nav>
    </header>
    <div class="cards">{cards}</div>
    <section><h2>Top pages</h2>{pages}</section>
    <section><h2>Daily trend</h2>{daily}</section>
    <section><h2>Referrers</h2>{referrers}</section>
    <section><h2>Recent visits</h2>{recent}</section>
  </main>
</body>
</html>"""
    return page.encode("utf-8")


class AnalyticsHandler(BaseHTTPRequestHandler):
    server_version = "QinSiteAnalytics/1.0"

    def log_message(self, fmt: str, *args: Any) -> None:
        print("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), fmt % args), flush=True)

    def _origin_allowed(self) -> str:
        origin = self.headers.get("Origin", "").rstrip("/")
        if origin in ALLOWED_ORIGINS:
            return origin
        return ""

    def _send(self, status: int, body: bytes = b"", content_type: str = "application/json") -> None:
        self.send_response(status)
        allowed_origin = self._origin_allowed()
        if allowed_origin:
            self.send_header("Access-Control-Allow-Origin", allowed_origin)
            self.send_header("Vary", "Origin")
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _json(self, status: int, payload: dict[str, Any]) -> None:
        self._send(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def do_OPTIONS(self) -> None:
        self.send_response(HTTPStatus.NO_CONTENT)
        allowed_origin = self._origin_allowed()
        if allowed_origin:
            self.send_header("Access-Control-Allow-Origin", allowed_origin)
            self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "3600")
        self.end_headers()

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        if parsed.path == "/health":
            self._json(HTTPStatus.OK, {"ok": True, "site": SITE_NAME})
            return
        if parsed.path == "/summary":
            if not authorized_summary(self, query):
                self._json(HTTPStatus.UNAUTHORIZED, {"error": "unauthorized"})
                return
            self._json(HTTPStatus.OK, summarize(parse_days(query, default=1)))
            return
        if parsed.path == "/admin":
            if not authorized_admin(self):
                self.send_response(HTTPStatus.UNAUTHORIZED)
                self.send_header("WWW-Authenticate", 'Basic realm="Site analytics"')
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            self._send(HTTPStatus.OK, render_admin(summarize(parse_days(query))), "text/html; charset=utf-8")
            return
        self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/collect":
            self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
            return
        if self.headers.get("DNT") == "1":
            self._send(HTTPStatus.NO_CONTENT)
            return
        try:
            length = min(int(self.headers.get("Content-Length", "0")), MAX_BODY_BYTES)
        except ValueError:
            length = 0
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_json"})
            return
        path = trim(payload.get("path"), 300) or "/"
        if not path.startswith("/"):
            path = "/" + path
        referrer = trim(payload.get("referrer"), 500)
        referrer_host = ""
        if referrer:
            referrer_host = trim(urlparse(referrer).netloc, 120)
        visitor_id = trim(payload.get("visitor_id"), 160)
        now = utc_now()
        with db_connect() as db:
            db.execute(
                """
                INSERT INTO pageviews (
                    ts_utc, local_date, path, title, referrer, referrer_host,
                    visitor_hash, ip_hash, user_agent, language, screen_width, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    now.isoformat(),
                    local_date(now),
                    path,
                    trim(payload.get("title"), 220),
                    referrer,
                    referrer_host,
                    hash_value(visitor_id),
                    hash_value(client_ip(self)),
                    trim(self.headers.get("User-Agent", ""), 500),
                    trim(payload.get("language"), 40),
                    int_or_zero(payload.get("screen_width")),
                    int(time.time()),
                ),
            )
            db.commit()
        self._send(HTTPStatus.NO_CONTENT)


def main() -> None:
    ensure_db()
    bind = env("ANALYTICS_BIND", "127.0.0.1")
    port = int(env("ANALYTICS_PORT", "18080"))
    httpd = ThreadingHTTPServer((bind, port), AnalyticsHandler)
    print(f"qin-site-analytics listening on http://{bind}:{port}", flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
