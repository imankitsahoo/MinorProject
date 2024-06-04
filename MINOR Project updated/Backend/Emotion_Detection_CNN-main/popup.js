document.addEventListener("DOMContentLoaded", function () {
  // Check if the extension is enabled and update the button text accordingly
  chrome.storage.local.get("enabled", function (data) {
    const enableExtensionBtn = document.getElementById("enableExtensionBtn");
    if (data.enabled) {
      enableExtensionBtn.textContent = "Enable Extension";
    } else {
      enableExtensionBtn.textContent = "Disable Extension";
    }
  });

  // Handle click event on the "Enable Extension" button
  document
    .getElementById("enableExtensionBtn")
    .addEventListener("click", function () {
      chrome.storage.local.get("enabled", function (data) {
        const isEnabled = data.enabled;
        // Toggle the enabled state
        chrome.storage.local.set({ enabled: !isEnabled }, function () {
          // Update button text based on the new state
          const enableExtensionBtn =
            document.getElementById("enableExtensionBtn");
          if (!isEnabled) {
            enableExtensionBtn.textContent = "Disable Extension";
          } else {
            enableExtensionBtn.textContent = "Enable Extension";
          }
        });
      });
    });
});

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("enableExtensionBtn")
    .addEventListener("click", function () {
      chrome.runtime.sendMessage({ action: "toggle" });
    });
});

