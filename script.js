document.getElementById('uploadForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  var formData = new FormData();
  formData.append('file', document.getElementById('fileInput').files[0]);
  
  fetch('/predict', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('message').innerText = 'Prediction: ' + data.prediction;
    document.getElementById('testButton').style.display = 'block';
  })
  .catch(error => console.error('Error:', error));
});

document.getElementById("testButton").addEventListener("click", function() {
  fetch("/predict/", {
    method: "POST",
    body: new FormData(document.getElementById('uploadForm'))  // Include form data
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("result").textContent = "Prediction: " + data.prediction;
  })
  .catch(error => {
    console.error("Error making prediction:", error);
    document.getElementById("result").textContent = "Error making prediction.";
  });
});
