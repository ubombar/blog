# blog.bombar.dev

Write posts in `posts/<slug>.md`:

```markdown
---
title: My post
date: 2026-10-06
---

Markdown here.
```

Push to `main` and GitHub Actions builds and deploys it. Add `draft: true` to hide a post.

Local (Nix): `make preview` builds, serves on :8000 and opens the browser. `nix develop` for a shell, `nix build` for the site in `./result`.

Standalone apps live in `apps/<name>/` and are copied unchanged into the site.
The Hello World PWA is at `/apps/hello/` (after deployment:
`https://blog.bombar.dev/apps/hello/`). Open it in Chrome on Android or Safari on
iPhone and add it to the Home Screen. It caches its files for offline use.

Use relative URLs for each app's assets, manifest, and service worker so its
offline scope stays inside its own directory. The Hello app does not load the
blog's analytics. For local testing, use `http://localhost:8000/apps/hello/`;
installation from a phone over Wi-Fi requires a trusted HTTPS origin.
