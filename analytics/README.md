# Self-hosted site analytics

This folder contains a tiny private analytics backend for `tianqin.netlify.app`.
It is intended to run on the Hermes server behind nginx.

## Endpoints

- `POST /collect`: anonymous pageview collection.
- `GET /admin?days=7`: basic-auth dashboard.
- `GET /summary?days=1`: JSON summary for Hermes, protected by bearer token or `token` query parameter.
- `GET /health`: health check.

The service stores hashed visitor IDs and hashed IPs only. Raw IP addresses are not written to SQLite.

## Server environment

Create `/etc/qin-site-analytics.env` on the server:

```bash
ANALYTICS_BIND=127.0.0.1
ANALYTICS_PORT=18080
ANALYTICS_DB=/var/lib/qin-site-analytics/analytics.sqlite3
ANALYTICS_SITE=tianqin.netlify.app
ANALYTICS_TIMEZONE=Asia/Shanghai
ANALYTICS_ALLOWED_ORIGINS=https://tianqin.netlify.app,http://127.0.0.1:1313,http://localhost:1313
ANALYTICS_SALT=<long-random-secret>
ANALYTICS_API_TOKEN=<long-random-token>
ANALYTICS_ADMIN_USER=<admin-user>
ANALYTICS_ADMIN_PASSWORD=<long-random-password>
```

Install `server.py` in `/opt/qin-site-analytics/server.py`, install the systemd unit in
`/etc/systemd/system/qin-site-analytics.service`, and add the nginx location block to the
server block that listens on port 80.

The Netlify site proxies:

- `/api/analytics/*` to the Hermes backend for collection.
- `/site-analytics/*` to the same backend for the dashboard.
