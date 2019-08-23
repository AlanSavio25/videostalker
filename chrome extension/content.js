alert("You're on a Youtube page link!")
// var firstHref = $("a[href^='http']").eq(0).attr("href");
// var secondhref = $("a[href^='http']").eq(1).attr("href");
// console.log(firstHref);
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
    alert("content "+ url)
});
