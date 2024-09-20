document.getElementById("extract").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Execute content.js to set up the page
  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      files: ["content.js"],
    },
    async () => {
      // Request the transcript after executing content.js
      chrome.tabs.sendMessage(tab.id, { action: "extractTranscript" }, async (transcriptResponse) => {
        if (transcriptResponse && transcriptResponse.transcript) {
          const success = await sendTranscriptToServer(transcriptResponse.transcript); // Send transcript to the server

          // Create the overlay only if sending the transcript was successful
          if (success) {
            chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
          }
        } else {
          console.error("Failed to extract transcript:", transcriptResponse.transcript);
        }
      });
    }
  );
});

async function sendTranscriptToServer(transcript) {
  try {
    console.log("Sending transcript to server:", transcript); // Log the transcript data

    const response = await fetch("http://localhost:5000/api/transcript", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ transcript: transcript }), // Send the transcript data as JSON
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const responseData = await response.json();
    console.log("Successfully sent transcript to server:", responseData);
    return true; // Indicate success
  } catch (error) {
    console.error("Failed to send transcript to server:", error);
    return false; // Indicate failure
  }
}

let video;
let model;
let canvas;
let ctx;

document.addEventListener('DOMContentLoaded', function() {
  const startButton = document.getElementById('startCamersa');
  video = document.getElementById('video');
  const cameraContainer = document.getElementById('cameraContainer');
  const resultDiv = document.getElementById('result');
  canvas = document.getElementById('canvas');
  ctx = canvas.getContext('2d');

  startButton.addEventListener('click', startCamera);

  async function startCamera() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;
      cameraContainer.classList.remove('hidden');
      startButton.classList.add('hidden');
      await loadModel();
      processVideoFrames();
    } catch (err) {
      console.error("Error accessing the camera: ", err);
      resultDiv.textContent = "Error accessing the camera. Please make sure you've granted camera permissions.";
    }
  }

  async function loadModel() {
    try {
      // Replace 'model_url' with the actual URL or path to your converted TensorFlow.js model
      model = await tf.loadLayersModel('model_url');
      console.log('Model loaded successfully');
    } catch (err) {
      console.error('Failed to load model:', err);
    }
  }

  function preprocessFrame(videoFrame) {
    return tf.tidy(() => {
      const tfImg = tf.browser.fromPixels(videoFrame).resizeBilinear([224, 224]);
      const normalizedImg = tfImg.div(tf.scalar(255));
      return normalizedImg.expandDims(0);
    });
  }

  async function predict() {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const tfImg = preprocessFrame(canvas);
    const prediction = await model.predict(tfImg);
    const classIndex = prediction.argMax(1).dataSync()[0];
    // Replace this with your actual class mapping
    const classNames = ['Class 0', 'Class 1', 'Class 2']; // Add all your classes
    resultDiv.textContent = `Detected Sign: ${classNames[classIndex]}`;
    tfImg.dispose();
    prediction.dispose();
  }

  function processVideoFrames() {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
      predict();
    }
    requestAnimationFrame(processVideoFrames);
  }
});