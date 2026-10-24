// Retired: the root-scope Shinylive service worker was only used by the old embedded apps on /teaching/.
// Browsers that still have it registered pick up this version, which unregisters itself and reloads open
// pages, so the per-course Econ Lab service workers (e.g. /econlab/stats-course/) work normally again.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil(
    self.registration.unregister()
      .then(() => self.clients.matchAll({ type: "window" }))
      .then((clients) => clients.forEach((c) => c.navigate(c.url)))
  );
});
