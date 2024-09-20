let currentOverlay = null;
// Function to extract transcript from YouTube
async function extractTranscript() {
  const transcriptSelector = "ytd-transcript-segment-renderer";
  const transcriptElements = document.querySelectorAll(transcriptSelector);

  if (transcriptElements.length > 0) {
    const transcriptLines = Array.from(transcriptElements).map((segment) => {
      const timestampElement = segment.querySelector("div.segment-timestamp");
      const textElement = segment.querySelector(
        "yt-formatted-string.segment-text"
      );

      const timestamp = timestampElement
        ? timestampElement.textContent.trim()
        : "";
      const text = textElement ? textElement.textContent.trim() : "";

      return timestamp + " " + text;
    });
    const transcript = transcriptLines.join("\n");
    return transcript;
  }

  return `⚠ Transcript not found. Make sure the transcript is visible on the page.`;
}
extractTranscript();


function createOverlay() {
  const videoPlayer = document.querySelector('.html5-video-player');
  if (!videoPlayer) {
    console.error('Video player not found');
    return;
  }

  // Remove existing overlay if present
  if (currentOverlay) {
    currentOverlay.remove();
  }

  const overlay = document.createElement('div');
  overlay.style.cssText = `
    position: absolute;
    bottom: 60px;
    right: 20px;
    width: 320px;
    height: 180px;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 2147483647;
    border: 2px solid white;
  `;

  const video = document.createElement('video');
  video.style.cssText = `
    width: 100%;
    height: 100%;
    object-fit: cover;
  `;
  video.autoplay = true;
  video.src = 'https://www.w3schools.com/html/mov_bbb.mp4'; // Replace with the actual URL of your sign language video

  overlay.appendChild(video);
  videoPlayer.appendChild(overlay);
  currentOverlay = overlay; // Track the current overlay

  // Add a close button
  const closeButton = document.createElement('button');
  closeButton.textContent = 'X';
  closeButton.style.cssText = `
    position: absolute;
    top: 5px;
    right: 5px;
    background: red;
    color: white;
    border: none;
    cursor: pointer;
    z-index: 2147483648;
  `;
  closeButton.onclick = () => {
    overlay.remove();
    currentOverlay = null; // Clear reference
  };
  overlay.appendChild(closeButton);

  const youtubeVideo = document.querySelector('video.html5-main-video');
  if (youtubeVideo) {
    youtubeVideo.currentTime = 0; // Reset YouTube video to 0:00
    youtubeVideo.play(); // Play YouTube video

    // Play overlay video
    video.currentTime = 0; // Reset overlay video to 0:00
    video.play(); // Play overlay video
  }

  // Synchronize play/pause functionality
  video.addEventListener('play', () => {
    if (youtubeVideo.paused) {
      youtubeVideo.play();
    }
  });

  video.addEventListener('pause', () => {
    if (!youtubeVideo.paused) {
      youtubeVideo.pause();
    }
  });

  youtubeVideo.addEventListener('play', () => {
    video.play();
  });

  youtubeVideo.addEventListener('pause', () => {
    video.pause();
  });

  // Close overlay when YouTube video ends
  youtubeVideo.addEventListener('ended', () => {
    overlay.remove();
    currentOverlay = null; // Clear reference
  });

  // Listen for changes in the YouTube player
  const observer = new MutationObserver(() => {
    const newVideo = document.querySelector('video.html5-main-video');
    if (newVideo && currentOverlay) {
      const newVideoSrc = newVideo.getAttribute('src');
      const oldVideoSrc = youtubeVideo.getAttribute('src');
      if (newVideoSrc !== oldVideoSrc) {
        // Stop overlay video and remove the overlay
        video.pause(); // Stop overlay video
        overlay.remove(); // Remove the overlay
        currentOverlay = null; // Clear reference
        observer.disconnect(); // Stop observing
      }
    }
  });

  // Observe changes to the video player
  observer.observe(videoPlayer, { attributes: true, childList: true, subtree: true });
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "extractTranscript") {
    extractTranscript().then(transcript => sendResponse({transcript: transcript}));
    return true; // Indicates that the response is sent asynchronously
  } else if (request.action === "showOverlay") {
    createOverlay();
    sendResponse({status: "Overlay created"});
  }
});

// This line is not needed here as we're using message passing now
// extractTranscript();