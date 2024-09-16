import { YoutubeTranscript } from 'youtube-transcript';
chrome.tabs.query({ active: true, lastFocusedWindow: true }, function (tabs) {
  var url = tabs[0].url;
});
YoutubeTranscript.fetchTranscript(url).then(console.log);
