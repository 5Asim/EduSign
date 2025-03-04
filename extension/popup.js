document.getElementById("extract").addEventListener("click", async () => {
  const loadingScreen = document.getElementById("loading-screen");
  loadingScreen.style.display = "block"; // Show loading screen
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Execute content.js to set up the page
  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      files: ["content.js"],
    },
    async () => {
      // Request the transcript after executing content.js
      chrome.tabs.sendMessage(
        tab.id,
        { action: "extractTranscript" },
        async (transcriptResponse) => {
          if (transcriptResponse && transcriptResponse.transcript) {
            const success = await sendTranscriptToServer(
              transcriptResponse.transcript
            ); // Send transcript to the server

            // Create the overlay only if sending the transcript was successful
            chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
            // if (success) {
            //   chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
            // }
          } else {
            console.error(
              "Failed to extract transcript:",
              transcriptResponse.transcript
            );
          }
        }
      );
      chrome.tabs.sendMessage(
        tab.id,
        { action: "extractTranscript" },
        async (transcriptResponse) => {
          if (transcriptResponse && transcriptResponse.transcript) {
            const success = await sendTranscriptToServer(
              transcriptResponse.transcript
            ); // Send transcript to the server

            // Create the overlay only if sending the transcript was successful
            setTimeout(() => {
              chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
            }, 8000);
          }
          if (success) {
            chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
          } else {
            console.error(
              "Failed to extract transcript:",
              transcriptResponse.transcript
            );
          }
        }
      );
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
    print(response);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const responseData = await response.json();
    console.log("Successfully sent transcript to server:", responseData);

    await listenToSSE();
    return true; // Indicate success
  } catch (error) {
    console.error("Failed to send transcript to server:", error);
    return false; // Indicate failure
  }
}

async function listenToSSE() {
  console.log("sse");
  // Create an EventSource to listen to the server updates
  const eventSource = new EventSource(`http://localhost:5000/api/sse`);

  eventSource.onmessage = async function (event) {
    console.log("SSE message received:", event.data);

    // Check if the server indicates the video is ready
    if (event.data.includes(".mp4")) {
      console.log("Video is ready:", event.data);

      const response = await fetch("http://localhost:5000/api/download_video", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      print(response);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // To download the video using the src
      // Read the file as a blob
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);

      // Create a link element to download the file
      const a = document.createElement("a");
      a.style.display = "none";
      a.href = url;
      a.download = `video_${clientId}.mp4`;

      // Append the link to the body and trigger a click event
      document.body.appendChild(a);
      a.click();

      // Clean up: Remove the link and revoke the object URL
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
      // Close the SSE connection once the video is ready and downloaded
      eventSource.close();
    } else {
      // Log the processing status
      console.log("Processing update:", event.data);
    }
  };

  document.addEventListener("DOMContentLoaded", async () => {
    const videoFeed = document.getElementById("video-feed");
    const videoContainer = document.getElementById("videoContainer");
    const askQuestionButton = document.getElementById("askQuestionButton");
    const clearButton = document.getElementById("clear-btn");
    const recognizedWordElement = document.getElementById(
      "extension-recognized-word"
    );
    const narrateButton = document.getElementById("narrate-btn");

    // Access the webcam when the "Ask Question" button is clicked
    askQuestionButton.addEventListener("click", () => {
      videoFeed.src = "http://localhost:5000/video_feed"; // Adjust based on your Flask server
      videoContainer.style.display = "block"; // Show video container
    });

    // Fetch the recognized word from the backend
    async function fetchRecognizedWord() {
      const response = await fetch("http://localhost:5000/get_word");
      const data = await response.json();
      recognizedWordElement.innerText =
        data.predicted_word || "No word recognized";
    }

    // Update recognized word every second
    setInterval(fetchRecognizedWord, 1000); // Adjust interval as needed

    // Clear the predicted word
    clearButton.addEventListener("click", async () => {
      const response = await fetch("http://localhost:5000/clear_word", {
        method: "POST",
      });
      const data = await response.json();
      console.log(data.status);
      recognizedWordElement.innerText = "No word recognized"; // Clear displayed word
    });

    // Copy recognized word to clipboard
    document
      .getElementById("extension-copy-btn")
      .addEventListener("click", () => {
        const textToCopy = recognizedWordElement.innerText;

        if (textToCopy && textToCopy !== "No word recognized") {
          navigator.clipboard
            .writeText(textToCopy)
            .then(() => {
              alert("Text copied to clipboard!");
            })
            .catch((err) => {
              console.error("Error copying text: ", err);
            });
        } else {
          alert("No text to copy!");
        }
      });

    // Add the event listener for the narrate button
    narrateButton.addEventListener("click", async () => {
      const recognizedWord = recognizedWordElement.innerText;
      if (recognizedWord && recognizedWord !== "No word recognized") {
        try {
          const response = await fetch(
            "http://localhost:5000/api/transcript/audio",
            {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({ transcript: recognizedWord }),
            }
          );

          if (response.ok) {
            const audioBlob = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioUrl);
            audio.play(); // Play the audio
          } else {
            console.error("Failed to generate audio:", response.statusText);
          }
        } catch (error) {
          console.error(
            "Error while sending recognized word to the server:",
            error
          );
        }
      } else {
        alert("No recognized word to narrate!");
      }
    });
  });

  // popup.js
  document
    .getElementById("askQuestionButton")
    .addEventListener("click", function () {
      document.querySelector(".popup").style.display = "none"; // Hide popup
      document.querySelector(".camera").style.display = "block"; // Show camera
    });
}
