(() => {
  "use strict";
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
    ...document.querySelectorAll("#about, #research, #publications"),
  ];
  const links = [...document.querySelectorAll("nav a")];
  let pending = false;
  function updateNavigation() {
    let active = sections[0].id;
    sections.forEach((section) => {
      if (section.getBoundingClientRect().top <= innerHeight * 0.3)
        active = section.id;
    });
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
