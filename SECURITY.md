# Security policy

## Reporting a vulnerability

Email ryaneditraj@gmail.com with the subject line "Personality Analyzer security". Please include:

- The page or endpoint
- What you sent
- What you expected to happen
- What happened instead

Do not open a public GitHub issue for a vulnerability, and do not include exploit payloads in a pull request description.

## Supported versions

Security fixes land on `main`. There are no older release branches.

## What this app stores

The quiz does not have accounts, cookies for login, or a database. Answers exist only for the request that scores them. Result pages are sent with `Cache-Control: no-store`.

## Configuration

| Variable | Purpose |
| --- | --- |
| `FLASK_DEBUG` | Leave unset or `0`. `1` turns on the Werkzeug debugger, which is unsafe on a public server. |
| `FLASK_HOST` | Defaults to `127.0.0.1`. Bind `0.0.0.0` only when you intend to share the process. |
| `FLASK_PORT` | Defaults to `5001`. |
| `SITE_URL` | Optional public origin for canonical, Open Graph, sitemap, and robots links. |

Copy `.env.example` to `.env` for local values. `.env` is gitignored.

## Hardened behavior

- Itinerary HTML escapes the destination and the generated sentences. Unknown personalities and non-numeric day counts are rejected.
- Names used in the page and in share links are trimmed, limited to 80 characters, and URL-encoded.
- External result links use `rel="noopener noreferrer"`.
- Responses send `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, and a Content-Security-Policy.
- Chart.js 4.4.1 is loaded from cdnjs with a Subresource Integrity hash.
- Form bodies are limited to 64 KB.
- Flask is pinned to 3.1.3, which includes the fix for CVE-2026-27205. This app does not use sessions, so that issue does not apply here, but the pin stays on the patched release.
- Jinja2 is pinned to 3.1.6, which includes the fix for CVE-2025-27516. The quiz templates are part of this repository, not user input, so the sandbox breakout does not apply. The pin stays on the patched release.
- Werkzeug is pinned to 3.1.9, which includes the fix for GHSA-g6x2-hccm-hh4m (Windows device names in `safe_join`).

## Remaining risk

- Chart.js still comes from a third-party CDN. The integrity hash pins the file we reviewed. If that CDN is unreachable, the charts do not draw and the rest of the result page still works.
- Budget math uses fixed currency rates. That is a product limit, not a credential.
- Deploy behind HTTPS. The app itself does not terminate TLS.
- A history search of this repository found no committed API keys, passwords, tokens, or private keys. Nothing in git history needs to be rotated because of a leaked credential.
