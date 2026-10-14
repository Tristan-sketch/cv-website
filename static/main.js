// Small extras for the device: clock, battery, typing effect, screen readouts and
// menu navigation. The page is fully readable without this file.

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Clock in the status bar
const clock = document.getElementById("clock");
function updateClock() {
  clock.textContent = new Date().toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" });
}
updateClock();
setInterval(updateClock, 30_000);

// Battery = progress of the study programme. Recalculated here so a static
// build stays correct after the day it was built.
const battery = document.getElementById("battery");
const start = new Date(battery.dataset.start);
const end = new Date(battery.dataset.end);
const share = Math.min(Math.max((Date.now() - start) / (end - start), 0), 1);
const percent = Math.round(share * 100);
battery.querySelector("i").style.width = `${percent}%`;
battery.title = `Studium ${percent} % geladen`;
battery.setAttribute("aria-label", `Fortschritt des Studiums: ${percent} Prozent`);

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

// Screen views: the intro at the top, a short readout for each section below
const views = new Map([...document.querySelectorAll(".screen-view")].map((view) => [view.dataset.view, view]));
function showView(name) {
  const target = views.get(name) ?? views.get("intro");
  views.forEach((view) => view.classList.toggle("is-active", view === target));
}

// Menu navigation with the d-pad and the keyboard. The menu is a grid of two columns.
const device = document.querySelector(".device");
const items = [...document.querySelectorAll(".menu-item")];
const columns = 2;
let selected = 0;

function select(index) {
  if (index < 0 || index >= items.length) return;
  selected = index;
  items.forEach((item, i) => item.classList.toggle("is-selected", i === selected));
}

function run(action) {
  if (action === "up") select(selected - columns);
  if (action === "down") select(selected + columns);
  if (action === "left") select(selected - 1);
  if (action === "right") select(selected + 1);
  if (action === "ok") items[selected].click();
  if (action === "back") window.scrollTo({ top: 0 });
  if (action === "print") window.print();
}

document.querySelectorAll("[data-action]").forEach((button) => {
  button.addEventListener("click", () => {
    if (device.contains(button) && button.dataset.action !== "print") device.focus({ preventScroll: true });
    run(button.dataset.action);
  });
});

items.forEach((item, i) => item.addEventListener("mouseenter", () => select(i)));

// Clicking anywhere on the device gives it focus, so the arrow keys steer the menu.
// Elsewhere on the page the arrow keys scroll as usual.
device.addEventListener("mousedown", (event) => {
  if (!event.target.closest("a, button")) device.focus({ preventScroll: true });
});

device.addEventListener("keydown", (event) => {
  if (event.altKey || event.ctrlKey || event.metaKey) return;
  const keys = { ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right" };

  if (keys[event.key]) {
    event.preventDefault();
    run(keys[event.key]);
    items[selected].focus({ preventScroll: true });
  } else if (event.key === "Enter" && event.target === device) {
    run("ok");
  }
});

// Follow the reader: highlight the matching menu entry and switch the screen view.
const sections = [...document.querySelectorAll(".section")];
const hero = document.querySelector(".hero");
let lastSection = null;

function followReader() {
  const line = window.innerHeight * 0.45;
  const heroVisible = hero.getBoundingClientRect().bottom > window.innerHeight * 0.3;
  // The last section whose top has passed the reading line, so gaps between sections count too.
  // At the very bottom the last section never reaches the line, so it counts as current there.
  const atBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
  const passed = sections.filter((section) => section.getBoundingClientRect().top < line);
  const current = heroVisible ? null : atBottom ? sections.at(-1) : passed.at(-1);
  const id = current?.id ?? null;
  if (id === lastSection) return;
  lastSection = id;

  showView(id ?? "intro");
  const index = items.findIndex((item) => item.hash === `#${id}`);
  if (index >= 0) select(index);
}

let ticking = false;
window.addEventListener("scroll", () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    followReader();
    ticking = false;
  });
}, { passive: true });
followReader();
