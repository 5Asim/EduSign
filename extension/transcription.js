import { YoutubeTranscript } from 'youtube-transcript';
let url;

chrome.tabs.query({ active: true, lastFocusedWindow: true }, function (tabs) {
  url = tabs[0].url;
});

function transcribe() {
  console.log('click');
  if (url) {
    YoutubeTranscript.fetchTranscript(url)
      .then((value) => {
        console.log(value);
        exportToFile(value);
      })
      .catch((error) => console.error('Error fetching transcript:', error));
  } else {
    console.error('URL is not available');
  }
}

function exportToFile(transcription) {
  const blob = new Blob([JSON.stringify(transcription, null, 2)], {
    type: 'text/plain',
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'transcription.txt';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
