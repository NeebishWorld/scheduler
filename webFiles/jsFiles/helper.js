const screens = {
  home: document.getElementById("screen-home"),
  study: document.getElementById("screen-study"),
  test: document.getElementById("screen-test"),
};

function showScreen(name) {
  Object.values(screens).forEach((el) => el.classList.remove("screen--active"));
  screens[name].classList.add("screen--active");
}

document.addEventListener("click", (e) => {
  const btn = e.target.closest("[data-go]");
  if (!btn) return;

  const target = btn.dataset.go;
  if (!screens[target]) return;

  showScreen(target);
});

// 처음 화면
showScreen("home");
