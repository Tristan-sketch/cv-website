// Small extras for the device: clock, typing effect and menu navigation.
// The page works without this file; it only adds the interactive parts.

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Clock in the status bar
const clock = document.getElementById("clock");
function updateClock() {
  clock.textContent = new Date().toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" });
}
updateClock();
setInterval(updateClock, 30_000);

// Type the role letter by letter
const typed = document.getElementById("typed");
if (!reduceMotion) {
  const text = typed.dataset.text;
  typed.textContent = "";
  [...text].forEach((letter, i) => {
    setTimeout(() => (typed.textContent += letter), 600 + i * 70);
  });
}

// Show the speech bubble once after the page loaded
const bubble = document.querySelector(".bubble");
setTimeout(() => bubble.classList.add("is-visible"), 1200);
setTimeout(() => bubble.classList.remove("is-visible"), 3600);

// Menu navigation with the d-pad and the keyboard
const device = document.querySelector(".device");
const items = [...document.querySelectorAll(".menu-item")];
let selected = 0;

function select(index) {
  selected = (index + items.length) % items.length;
  items.forEach((item, i) => item.classList.toggle("is-selected", i === selected));
}

function run(action) {
  if (action === "up") select(selected - 1);
  if (action === "down") select(selected + 1);
  if (action === "ok") items[selected].click();
  if (action === "back") window.scrollTo({ top: 0 });
}

document.querySelectorAll("[data-action]").forEach((button) => {
  button.addEventListener("click", () => run(button.dataset.action));
});

items.forEach((item, i) => item.addEventListener("mouseenter", () => select(i)));

// Arrow keys only control the menu while the device is visible,
// so they still scroll the page normally further down.
let deviceVisible = true;
new IntersectionObserver(([entry]) => (deviceVisible = entry.isIntersecting), { threshold: 0.5 }).observe(device);

document.addEventListener("keydown", (event) => {
  if (!deviceVisible || event.altKey || event.ctrlKey || event.metaKey) return;
  const onControl = event.target instanceof Element && event.target.closest("a, button, input, textarea");
  const keys = { ArrowUp: "up", ArrowLeft: "up", ArrowDown: "down", ArrowRight: "down" };

  if (keys[event.key]) {
    event.preventDefault();
    run(keys[event.key]);
  } else if (event.key === "Enter" && !onControl) {
    run("ok");
  }
});

// Keep the menu selection in sync with the section on screen
const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const index = items.findIndex((item) => item.hash === `#${entry.target.id}`);
      if (index >= 0) select(index);
    });
  },
  { rootMargin: "-40% 0px -55% 0px" },
);
document.querySelectorAll(".section").forEach((section) => sectionObserver.observe(section));
