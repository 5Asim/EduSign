document.getElementById("extract").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      files: ["content.js"],
    },
    ([result]) => {
      document.getElementById("transcript").value = result.result;
    }
  );
});

document.getElementById("copy-all").addEventListener("click", async () => {
  const transcriptTextarea = document.getElementById("transcript");
  transcriptTextarea.select();

  try {
    await navigator.clipboard.writeText(transcriptTextarea.value);
  } catch (err) {
    console.error("Failed to copy the transcript: ", err);
  }
});

async function sendTranscriptToServer(transcript) {
  try {
    const response = await fetch("localhost:5100/postTranscibedData", {
      method: "POST", // Specify the method as POST
      headers: {
        "Content-Type": "application/json", // Specify the content type as JSON
      },
      body: JSON.stringify({ transcript: transcript }), // Send the transcript data as JSON
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const responseData = await response.json();
    console.log("Successfully sent transcript to server:", responseData);
  } catch (error) {
    console.error("Failed to send transcript to server:", error);
  }
}
