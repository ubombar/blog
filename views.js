// Fill every [data-path] element with its GoatCounter view count.
document.querySelectorAll(".views[data-path]").forEach(async (el) => {
  try {
    const r = await fetch(`https://${window.GC}.goatcounter.com/counter/${encodeURIComponent(el.dataset.path)}.json`);
    const count = r.ok ? (await r.json()).count : "0";  // 404 = no views yet
    el.textContent = ` · ${count} view${count === "1" ? "" : "s"}`;
  } catch {}
});
