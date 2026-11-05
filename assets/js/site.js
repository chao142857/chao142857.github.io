(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : system.matches;
  const updateLabel = () => { toggle.setAttribute('aria-label', `Switch to ${isDark() ? 'light' : 'dark'} mode`); };
  toggle.hidden = false;
  updateLabel();
  system.addEventListener('change', updateLabel);
  toggle.addEventListener('click', () => {
    root.dataset.theme = isDark() ? 'light' : 'dark';
    try { localStorage.setItem('chao-theme', root.dataset.theme); } catch (e) {}
    updateLabel();
  });
})();
