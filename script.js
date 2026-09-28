(() => {
  "use strict";
  const visitorCounter = document.querySelector("#visitor-counter");
  if (visitorCounter && location.hostname === "charlesyang030.github.io") {
    visitorCounter.addEventListener("load", () => {
      visitorCounter.hidden = false;
      document.querySelector("#visitor-counter-fallback").hidden = true;
    });
    visitorCounter.src = visitorCounter.dataset.src;
  }
  const visitorPins = document.querySelector(".visitors-pins");
  if (visitorPins) {
    const ns = "http://www.w3.org/2000/svg";
    const renderVisitors = (data) => {
      if (!Array.isArray(data.countries)) throw new Error("Invalid visitor data");
      visitorPins.replaceChildren();
      data.countries.forEach((country) => {
        if (!Array.isArray(country.position) || country.position.length !== 2 ||
            !country.position.every(Number.isFinite)) return;
        const [x, y] = country.position;
        if (x < 0 || x > 720 || y < 0 || y > 300) return;
        const pin = document.createElementNS(ns, "circle");
        pin.setAttribute("cx", x);
        pin.setAttribute("cy", y);
        pin.setAttribute("r", "4.5");
        pin.setAttribute("class", "visitor-pin");
        pin.setAttribute("tabindex", "0");
        pin.setAttribute("role", "img");
        const label = `${country.name} · ${Number(country.visitors).toLocaleString()} recorded ${country.visitors === 1 ? "visit" : "visits"}`;
        pin.setAttribute("aria-label", label);
        const title = document.createElementNS(ns, "title");
        title.textContent = label;
        pin.append(title);
        visitorPins.append(pin);
      });
      const updated = new Date(data.updatedAt);
      if (!Number.isNaN(updated.getTime()))
        document.querySelector(".visitors-legend").title = `Locations last changed ${updated.toLocaleString()}`;
    };
    const loadVisitors = async () => {
      // The bundled snapshot keeps the atlas useful if the statistics host is blocked.
      for (const url of [
        "https://raw.githubusercontent.com/CharlesYang030/CharlesYang030.github.io/visitor-data/visitors.json",
        "site-assets/visitors.json",
      ]) {
        try {
          const response = await fetch(url, { signal: AbortSignal.timeout(8000) });
          if (!response.ok) throw new Error("Visitor statistics unavailable");
          const data = await response.json();
          renderVisitors(data);
          if (url.startsWith("site-assets/")) {
            document.querySelector("#visitor-map-status").textContent =
              `Saved map · ${new Date(data.updatedAt).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" })}`;
          }
          return;
        } catch {
          // Retain the map and the direct statistics link when either host is unavailable.
        }
      }
    };
    loadVisitors();
  }
  const portraitSwitch = document.querySelector(".portrait-switch");
  const portraitPhotos = [...document.querySelectorAll(".portrait-photo")];
  if (portraitSwitch && portraitPhotos.length === 2) {
    let activePhoto = 0;
    portraitSwitch.hidden = false;
    portraitSwitch.addEventListener("click", async () => {
      if (portraitSwitch.disabled) return;
      portraitSwitch.disabled = true;
      const nextPhoto = 1 - activePhoto;
      try {
        await portraitPhotos[nextPhoto].decode();
        portraitPhotos.forEach((photo, index) => {
          photo.classList.toggle("is-active", index === nextPhoto);
          photo.setAttribute("aria-hidden", String(index !== nextPhoto));
        });
        activePhoto = nextPhoto;
        portraitSwitch.setAttribute(
          "aria-label",
          activePhoto === 0
            ? "Show the Universal globe photo"
            : "Show the mountain photo",
        );
      } catch {
        // Keep the current photo available if the alternative cannot load.
      } finally {
        portraitSwitch.disabled = false;
      }
    });
  }
  const affiliations = document.querySelector(".affiliations");
  if (affiliations) {
    const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
    const track = affiliations.querySelector(".affiliation-track");
    const copy = track.firstElementChild.cloneNode(true);
    copy.setAttribute("aria-hidden", "true");
    copy.removeAttribute("aria-label");
    copy.inert = true;
    track.append(copy);
    const updateMotion = () => {
      affiliations.classList.toggle("is-moving", !reducedMotion.matches);
    };
    reducedMotion.addEventListener("change", updateMotion);
    updateMotion();
  }
  const dialog = document.querySelector("#news");
  const triggers = [...document.querySelectorAll("[data-news-open]")];
  if (typeof dialog.showModal === "function") {
    triggers.forEach((button) => {
      button.hidden = false;
      button.setAttribute("aria-expanded", "false");
      button.addEventListener("click", () => {
        dialog.showModal();
        triggers.forEach((item) => item.setAttribute("aria-expanded", "true"));
      });
    });
    dialog
      .querySelector(".news-close")
      .addEventListener("click", () => dialog.close());
    dialog.addEventListener("click", (event) => {
      const bounds = dialog.getBoundingClientRect();
      if (
        event.target === dialog &&
        (event.clientX < bounds.left ||
          event.clientX > bounds.right ||
          event.clientY < bounds.top ||
          event.clientY > bounds.bottom)
      )
        dialog.close();
    });
    dialog.addEventListener("close", () =>
      triggers.forEach((button) =>
        button.setAttribute("aria-expanded", "false"),
      ),
    );
  }
  const sections = [
    ...document.querySelectorAll("#about, #research, #publications, #projects"),
  ];
  const links = [...document.querySelectorAll("nav a")];
  let pending = false;
  function updateNavigation() {
    let active = sections[0].id;
    sections.forEach((section) => {
      if (section.getBoundingClientRect().top <= innerHeight * 0.3)
        active = section.id;
    });
    if (scrollY + innerHeight >= document.documentElement.scrollHeight - 2)
      active = sections[sections.length - 1].id;
    links.forEach((link) => {
      if (link.hash === "#" + active)
        link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
    pending = false;
  }
  addEventListener(
    "scroll",
    () => {
      if (!pending) {
        pending = true;
        requestAnimationFrame(updateNavigation);
      }
    },
    { passive: true },
  );
  addEventListener("resize", updateNavigation);
  updateNavigation();
})();
