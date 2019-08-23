console.log(window.location.href)

chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
    alert("background "+ url)
});
