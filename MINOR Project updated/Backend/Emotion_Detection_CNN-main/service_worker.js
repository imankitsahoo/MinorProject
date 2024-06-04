// service_worker.js

// service_worker.js

let isEnabled = false;

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "toggle") {
    isEnabled = !isEnabled;
    if (isEnabled) {
      // Inject the popup.js script into the chat.html page
      chrome.tabs.executeScript({ file: "popup.js" });
    } else {
      // Remove the injected script
      chrome.tabs.executeScript({
        code: 'document.querySelector("#permissionPopup").remove();',
      });
    }
  }
});
