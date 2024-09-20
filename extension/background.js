// chrome.runtime.onInstalled.addListener(() => {
// 	chrome.contextMenus.create({
// 	  id: "textSelector",
// 	  title: "Run EduSign",
// 	  contexts: ["selection"]
// 	});
//       });
      
//       chrome.contextMenus.onClicked.addListener((info, tab) => {
// 	if (info.menuItemId === "textSelector" && info.selectionText && !tab.url.startsWith('chrome://')) {
// 	  chrome.scripting.executeScript({
// 	    target: {tabId: tab.id},
// 	    func: selectedTextHandler,
// 	    args: [info.selectionText]
// 	  });
// 	}
//       });
      
//       function selectedTextHandler(selectedText) {
// 	alert("Running....... Selected Text: " + selectedText);
// 	// Add your custom functionality here
//       }
       