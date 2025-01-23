const $cru = (e) => document.querySelector(e);
const $crus = (e) => document.querySelectorAll(e);
const $cruConfig = {
    prefix_url: "",
    headers: { "Content-Type": "application/json" },
    callbacks: {}
};

const $C = (e = !1) => {
    if (e) for (let t of Object.keys(e)) $cruConfig[t] = e[t];
    $cruLoadEvents();
};

const $cruLoadEvents = () => {
    $cruLoadRequests();
    $cruLoadFormIntercept();
    $cruLoadAllContainers();
};

const $cruLoadContainer = async (e) => {
    e.classList.add("loaded");
    const t = e.closest("[c-container]") || e;
    const r = t.getAttribute("c-container");
    const c = t.getAttribute("c-target") || !1;
    const a = t.getAttribute("c-type") || "html";
    const n = t.getAttribute("c-callback") || !1;
    const o = await fetch($cruConfig.prefix_url + r, { method: "GET", headers: $cruConfig.headers });
    const s = await $cruTypeResponse(a, o);
    const i = c ? $cru(c) : t;

    if (c || "off" != c) {
        if (c) i.innerHTML = s;
        else if ("html" == a) i.innerHTML = s;
    }

    if (n) $cruConfig.callbacks[n](s, i);
    $cruLoadEvents();
};

const $cruLoadAllContainers = async () => {
    $crus("[c-container]:not(.loaded)").forEach(async (e) => {
        e.classList.add("loaded");
        $cruLoadContainer(e);
    });

    $crus("[c-reload]:not(.loaded)").forEach(async (e) => {
        e.classList.add("loaded");
        e.addEventListener("click", (t) => $cruLoadContainer(e));
    });
};

const cruRequest = async (e, t) => {
    const r = e.getAttribute(`c-${t}`);
    const c = e.getAttribute("c-type") || "html";
    const a = e.getAttribute("c-reload-container") || !1;
    const n = e.getAttribute("c-remove-closest") || !1;
    const o = e.getAttribute("c-self-remove") || !1;
    const s = e.getAttribute("c-redirect") || !1;
    const i = e.getAttribute("c-swap") || !1;
    const d = e.getAttribute("c-append") || !1;
    const u = e.getAttribute("c-prepend") || !1;
    const l = e.getAttribute("c-callback") || !1;
    const $ = e.getAttribute("c-target") || !1;
    const g = await fetch($cruConfig.prefix_url + r, { method: t, headers: $cruConfig.headers });
    const L = await $cruTypeResponse(c, g);
    const f = !!$ && $cru($);

    if (n) e.closest(n).remove();
    if (o) e.remove();
    if (i) $cru(i).outerHTML = L;
    if (d) $cru(d).insertAdjacentHTML("beforeend", L);
    if (u) $cru(u).insertAdjacentHTML("afterbegin", L);
    if (a) $cruLoadContainer(e);
    if (f) {
        if (f) f.innerHTML = L;
        else if ("html" == c) e.innerHTML = L;
    }
    if (l) $cruConfig.callbacks[l](L, f);
    $cruLoadEvents();
    if (s) window.location.href = s;
};

const $cruLoadRequests = () => {
    $crus("[c-delete]:not(.loaded)").forEach((e) => {
        e.classList.add("loaded");
        e.addEventListener("click", async (t) => {
            cruRequest(e, "delete");
        });
    });

    $crus("[c-put]:not(.loaded)").forEach((e) => {
        e.classList.add("loaded");
        e.addEventListener("click", async (t) => {
            cruRequest(e, "put");
        });
    });

    $crus("[c-get]:not(.loaded)").forEach((e) => {
        e.classList.add("loaded");
        e.addEventListener("click", async (t) => {
            cruRequest(e, "get");
        });
    });

    $crus("[c-post]:not(.loaded)").forEach((e) => {
        e.classList.add("loaded");
        e.addEventListener("click", async (t) => {
            cruRequest(e, "post");
        });
    });
};

const $cruLoadFormIntercept = () => {
    $crus(".c-form:not(.loaded)").forEach((e) => {
        e.classList.add("loaded");
        e.addEventListener("submit", async (t) => {
            t.preventDefault();
            const r = e.getAttribute("action");
            const c = e.getAttribute("method").toUpperCase() || "POST";
            const a = e.getAttribute("c-type") || "html";
            const n = e.getAttribute("c-append") || !1;
            const o = e.getAttribute("c-prepend") || !1;
            const s = e.getAttribute("c-redirect") || !1;
            const i = e.getAttribute("c-reset") || !1;
            const d = e.getAttribute("c-swap") || !1;
            const u = e.getAttribute("c-target") || !1;
            const l = e.getAttribute("c-reload-container") || !1;
            const $ = e.getAttribute("c-callback") || !1;
            const g = $cruIsRead(c);
            const L = Object.fromEntries(new FormData(t.target).entries());
            const f = cruFormatURL(r, g, L);
            const b = await fetch(f, {
                method: c,
                headers: $cruConfig.headers,
                body: g ? null : JSON.stringify(L)
            });
            const p = await $cruTypeResponse(a, b);

            if (d) $cru(d).outerHTML = p;
            if (n) $cru(n).insertAdjacentHTML("beforeend", p);
            if (o) $cru(o).insertAdjacentHTML("afterbegin", p);
            if (u) $cru(u).innerHTML = p;
            if (i) e.reset();
            if (l) $cruLoadContainer(e);
            if ($) $cruConfig.callbacks[$]({ status: b.status, data: p }, e);
            $cruLoadEvents();
            if (s) window.location.href = s;
        });
    });
};

const cruFormatURL = (e, t, r) => {
    let c = $cruConfig.prefix_url + e;
    if (t) {
        try {
            c = new URL(e);
        } catch (t) {
            try {
                c = new URL(window.location.origin + e);
            } catch (t) {
                throw e;
            }
        } finally {
            c.search = new URLSearchParams(r).toString();
            c = c.href;
        }
    }
    return c;
};

const $cruCallback = (e, t) => {
    $cruConfig.callbacks[e] = t;
};

const $cruIsRead = (e) => ["GET", "HEAD"].includes(e);

const $cruTypeResponse = async (e, t) => {
    return "html" == e ? await t.text() : await t.json();
};

$C();















