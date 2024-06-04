// popup.js
document.getElementById('download').addEventListener('click', function() {
  // Code to download the extension
});

document.getElementById('gotoWebsite').addEventListener('click', function() {
  // Code to redirect to the website
});

// Code to ask for camera and audio permissions
navigator.mediaDevices.getUserMedia({ audio: true, video: true })
.then(function(stream) {
  // Code to handle the stream
})
.catch(function(err) {
  // Code to handle the error
});

// Code to show the robot at certain intervals
setInterval(function() {
  document.getElementById('robot').style.display = 'block';
  // Code for mood and facial recognition
}, 10000); // Change this to set the time limit

