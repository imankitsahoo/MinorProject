

//for the popup
document.addEventListener("DOMContentLoaded", function () {
  // Get references to the permission request popup and buttons
  const permissionPopup = document.getElementById("permissionPopup");
  const allowBtn = document.getElementById("allowBtn");
  const denyBtn = document.getElementById("denyBtn");

  // Hide the permission request popup initially
  permissionPopup.style.display = "none";

  // Function to show the permission request popup
  function showPermissionPopup() {
    permissionPopup.style.display = "block";
  }

  // Function to hide the permission request popup
  function hidePermissionPopup() {
    permissionPopup.style.display = "none";
  }


  // Event listener for the "Allow" button
  allowBtn.addEventListener("click", function () {
    // Perform action when user allows tracking
    // For example, send request to Python backend to track emotions
    // You can use fetch API or XMLHttpRequest to send request
    alert("Thank you for allowing us to track your emotions.");
    // Hide the permission request popup
    hidePermissionPopup();
  });

  // Event listener for the "Deny" button
  denyBtn.addEventListener("click", function () {
    // Perform action when user denies tracking
    alert("You denied permission to track your emotions.");
    // Hide the permission request popup
    hidePermissionPopup();
    window.close();
  });

  // Show the permission request popup
  showPermissionPopup();
});




