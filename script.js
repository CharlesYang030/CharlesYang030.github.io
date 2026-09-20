(() => {
  "use strict";
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const root = document.documentElement;
  const motionToggle = document.querySelector(".motion-toggle");
  let paused = reducedMotion.matches;
  function setMotion() {
    root.classList.toggle("motion-paused", paused);
    root.classList.toggle("motion-ready", !paused);
    motionToggle.setAttribute("aria-pressed", String(paused));
    motionToggle.setAttribute(
      "aria-label",
      paused ? "Resume animations" : "Pause animations",
    );
    motionToggle.firstElementChild.textContent = paused ? "▷" : "Ⅱ";
  }
  motionToggle.hidden = false;
  setMotion();
  motionToggle.addEventListener("click", () => {
    paused = !paused;
    setMotion();
  });
  reducedMotion.addEventListener("change", (event) => {
    paused = event.matches;
    setMotion();
  });

  const progress = document.querySelector(".reading-progress");
  const sections = [...document.querySelectorAll("main > section")];
  const navLinks = [...document.querySelectorAll("nav a")];
  let ticking = false;
  function updateProgress() {
    const scrollable =
      document.documentElement.scrollHeight - window.innerHeight;
    const fraction =
      scrollable > 0
        ? Math.min(1, Math.max(0, window.scrollY / scrollable))
        : 0;
    progress.style.transform = `scaleX(${fraction})`;
    let current = sections[0].id;
    sections.forEach((section) => {
      if (section.getBoundingClientRect().top <= window.innerHeight * 0.35)
        current = section.id;
    });
    navLinks.forEach((link) => {
      if (link.hash === `#${current}`)
        link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
    ticking = false;
  }
  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        requestAnimationFrame(updateProgress);
        ticking = true;
      }
    },
    { passive: true },
  );
  window.addEventListener("resize", updateProgress);
  updateProgress();
  if ("IntersectionObserver" in window && !reducedMotion.matches) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.05 },
    );
    document
      .querySelectorAll(
        ".research-topics article, .paper, .contact .section-body",
      )
      .forEach((item) => {
        if (item.getBoundingClientRect().top > window.innerHeight) {
          item.classList.add("reveal-ready");
          observer.observe(item);
        }
      });
  }
})();
