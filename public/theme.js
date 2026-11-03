// PRISM theme bootstrap: dark by default (spec section 8). Runs before first paint; adds a header toggle.
(function () {
  var root = document.documentElement, key = 'metriport-workspace-theme', saved = 'light';
  try { saved = localStorage.getItem(key) || localStorage.getItem('prism-theme') || 'light'; } catch (e) {}
  root.setAttribute('data-theme', 'prism');
  root.setAttribute('data-color-scheme', saved === 'light' ? 'light' : 'dark');
  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.querySelector('header nav');
    if (!nav) return;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'secondary'; b.id = 'themeToggle';
    var label = function () { b.setAttribute('aria-label',root.getAttribute('data-color-scheme') === 'light' ? 'Switch to dark mode' : 'Switch to light mode'); b.textContent = root.getAttribute('data-color-scheme') === 'light' ? 'Dark mode' : 'Light mode'; };
    b.onclick = function () {
      var next = root.getAttribute('data-color-scheme') === 'light' ? 'dark' : 'light';
      root.setAttribute('data-color-scheme', next);
      try { localStorage.setItem(key, next); } catch (e) {}
      label();
    };
    label(); nav.appendChild(b);
  });
})();
