(() => {
  "use strict";
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
