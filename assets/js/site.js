(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const isDark = () => root.dataset.theme === 'dark';
  const updateLabel = () => { toggle.setAttribute('aria-label', `Switch to ${isDark() ? 'light' : 'dark'} mode`); };
  toggle.hidden = false;
  updateLabel();
  toggle.addEventListener('click', () => {
    root.dataset.theme = isDark() ? 'light' : 'dark';
    updateLabel();
  });
})();
