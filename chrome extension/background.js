chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
    localStorage["jsondata"] = request.jsondata;
    
    }
);