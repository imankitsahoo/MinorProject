// Background script

let extensionEnabled = false;

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "enableExtension") {
    extensionEnabled = true;
    // Optionally, perform any necessary initialization when enabling the extension
  }
});
