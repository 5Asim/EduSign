// document.getElementById("extract").addEventListener("click", async () => {
//   const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

//   // Execute content.js to set up the page
//   chrome.scripting.executeScript(
//     {
//       target: { tabId: tab.id },
//       files: ["content.js"],
//     },
//     async () => {
//       // Request the transcript after executing content.js
//       chrome.tabs.sendMessage(tab.id, { action: "extractTranscript" }, async (transcriptResponse) => {
//         if (transcriptResponse && transcriptResponse.transcript) {
//           const success = await sendTranscriptToServer(transcriptResponse.transcript); // Send transcript to the server

//           // Create the overlay only if sending the transcript was successful
//           if (success) {
//             chrome.tabs.sendMessage(tab.id, { action: "showOverlay" });
//           }
//         } else {
//           console.error("Failed to extract transcript:", transcriptResponse.transcript);
//         }
//       });
//     }
//   );
// });

// async function sendTranscriptToServer(transcript) {
//   try {
//     console.log("Sending transcript to server:", transcript); // Log the transcript data

//     const response = await fetch("http://localhost:5000/api/transcript", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ transcript: transcript }), // Send the transcript data as JSON
//     });

//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }

//     const responseData = await response.json();
//     console.log("Successfully sent transcript to server:", responseData);
//     return true; // Indicate success
//   } catch (error) {
//     console.error("Failed to send transcript to server:", error);
//     return false; // Indicate failure
//   }
// }

document.addEventListener('DOMContentLoaded', function () {
  const videoFeed = document.getElementById('video-feed');
  const videoContainer = document.getElementById('videoContainer');
  const askQuestionButton = document.getElementById('askQuestionButton');
  const clearButton = document.getElementById('clear-btn');

  // Access the webcam when the "Ask Question" button is clicked
  askQuestionButton.addEventListener('click', () => {
      // Set the source of the image to the video feed from Flask
      videoFeed.src = 'http://localhost:5000/video_feed'; // Adjust this URL based on your Flask server address
      videoContainer.style.display = 'block'; // Show video container
  });

  // Clear the predicted word
  clearButton.addEventListener('click', async () => {
      const response = await fetch('http://localhost:5000/clear_word', { method: 'POST' });
      const data = await response.json();
      console.log(data.status);
  });
});