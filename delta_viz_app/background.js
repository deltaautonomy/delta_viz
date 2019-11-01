chrome.app.runtime.onLaunched.addListener(function() {
  chrome.app.window.create('app.html', {
    id: 'main',
    bounds: { width: 1280, height: 720 }
  });
});
