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

Local preview: `pip install markdown && python build.py && python -m http.server -d _site`
