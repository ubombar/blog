"""Build the site: posts/*.md -> _site/posts/*.html, plus index.html."""
import html, pathlib, shutil
import markdown

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "_site"
BASE = (ROOT / "templates/base.html").read_text()


def page(title, body):
    return BASE.replace("{title}", html.escape(title)).replace("{body}", body)


def parse(path):
    text = path.read_text()
    meta = {}
    if text.startswith("---"):
        _, front, text = text.split("---", 2)
        for line in front.strip().splitlines():
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta.setdefault("title", path.stem)
    meta.setdefault("date", "")
    return meta, markdown.markdown(text, extensions=["fenced_code", "tables"])


shutil.rmtree(OUT, ignore_errors=True)
(OUT / "posts").mkdir(parents=True)
for f in ["style.css", "CNAME"]:
    shutil.copy(ROOT / f, OUT / f)

posts = []
for md in (ROOT / "posts").glob("*.md"):
    meta, body = parse(md)
    if meta.get("draft") == "true":
        continue
    article = (f'<article><p class="meta">{meta["date"]}</p>'
               f'<h1>{html.escape(meta["title"])}</h1>{body}</article>')
    (OUT / "posts" / f"{md.stem}.html").write_text(
        page(f'{meta["title"]} — Ufuk Bombar', article))
    posts.append((meta["date"], meta["title"], md.stem))

items = "\n".join(
    f'<li><time class="meta" datetime="{d}">{d}</time>'
    f'<a href="/posts/{slug}.html">{html.escape(t)}</a></li>'
    for d, t, slug in sorted(posts, reverse=True))
index = ('<p class="intro">Notes from a PhD candidate in Internet measurements at LIP6, '
         'Sorbonne University. Packets, paths, and the software that chases them.</p>'
         f'<ul class="posts">\n{items}\n</ul>')
(OUT / "index.html").write_text(page("Ufuk Bombar — blog", index))
print(f"built {len(posts)} post(s) into {OUT}")
