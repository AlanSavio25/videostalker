chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
    //    localStorage["anger"] = request.anger;
    //    localStorage["contempt"] = request.contempt;
    //    localStorage["disgust"] = request.disgust;
    //    localStorage["link"] = request.link;
    localStorage["jsondata"] = request.jsondata;
    }
);






