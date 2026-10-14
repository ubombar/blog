const status = document.querySelector('#status');
const install = document.querySelector('#install');
let installPrompt;

if (!window.isSecureContext) {
  status.textContent = 'Open the HTTPS version to install and use offline.';
} else if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js', { scope: './' })
    .then(() => navigator.serviceWorker.ready)
    .then(() => {
      const standalone = window.matchMedia('(display-mode: standalone)').matches || navigator.standalone;
      status.textContent = standalone
        ? 'Ready for offline use.'
        : 'Ready for offline use. Add to your Home Screen.';
    })
    .catch(() => { status.textContent = 'Offline setup failed. Please reload while connected.'; });
} else {
  status.textContent = 'This browser does not support offline setup.';
}

window.addEventListener('beforeinstallprompt', event => {
  event.preventDefault();
  installPrompt = event;
  install.hidden = false;
});
install.addEventListener('click', async () => {
  if (!installPrompt) return;
  await installPrompt.prompt();
  await installPrompt.userChoice;
  installPrompt = null;
  install.hidden = true;
});
window.addEventListener('appinstalled', () => {
  install.hidden = true;
  status.textContent = 'Installed. Hello from your new app.';
});
