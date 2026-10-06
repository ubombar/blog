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
