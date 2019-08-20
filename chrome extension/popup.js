function processImage() {
    // Replace <Subscription Key> with your valid subscription key.
    var subscriptionKey = "b8ea8ee7334149cebd7ed530acdf84d7";

    // NOTE: You must use the same region in your REST call as you used to
    // obtain your subscription keys. For example, if you obtained your
    // subscription keys from westus, replace "westcentralus" in the URL
    // below with "westus".
    //
    // Free trial subscription keys are generated in the "westus" region.
    // If you use a free trial subscription key, you shouldn't need to change 
    // this region.
    var uriBase =
        "https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect";

    // Request parameters.
    var params = {
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes":
            "age,gender,smile,facialHair,glasses,emotion,hair,makeup"
    };

    // Display the image.
    var sourceImageUrl = document.getElementById("inputImage").value;
    // document.querySelector("#sourceImage").src = sourceImageUrl;

    // Perform the REST API call.
    $.ajax({
        url: uriBase + "?" + $.param(params),

        // Request headers.
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
        },

        type: "POST",

        // Request body.
        data: '{"url": ' + '"' + sourceImageUrl + '"}',
    })
    .done(function(data) {
        // Show formatted JSON on webpage.
        var i;
        json = "";
        for (i = 0; i < data.length; i++) {
            json += data[i]["faceAttributes"];
        }
        $("#responseTextArea").val(JSON.stringify(json, null, 2));
    })
    
    .fail(function(jqXHR, textStatus, errorThrown) {
        // Display error message.
        var errorString = (errorThrown === "") ?
            "Error. " : errorThrown + " (" + jqXHR.status + "): ";
        errorString += (jqXHR.responseText === "") ?
            "" : (jQuery.parseJSON(jqXHR.responseText).message) ?
                jQuery.parseJSON(jqXHR.responseText).message :
                    jQuery.parseJSON(jqXHR.responseText).error.message;
        alert(errorString);
    });
};

document.addEventListener('DOMContentLoaded', function() {
    var analyse = document.getElementById('analyse_button');
    analyse.addEventListener('click', function() {
        processImage();
    });
<<<<<<< HEAD
=======
=======
function processImage() {
    // Replace <Subscription Key> with your valid subscription key.
    var subscriptionKey = "b8ea8ee7334149cebd7ed530acdf84d7";

    // NOTE: You must use the same region in your REST call as you used to
    // obtain your subscription keys. For example, if you obtained your
    // subscription keys from westus, replace "westcentralus" in the URL
    // below with "westus".
    //
    // Free trial subscription keys are generated in the "westus" region.
    // If you use a free trial subscription key, you shouldn't need to change 
    // this region.
    var uriBase =
        "https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect";

    // Request parameters.
    var params = {
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes":
            "age,gender,smile,facialHair,glasses,emotion,hair,makeup"
    };

    // Display the image.
    var sourceImageUrl = document.getElementById("inputImage").value;
    // document.querySelector("#sourceImage").src = sourceImageUrl;

    // Perform the REST API call.
    $.ajax({
        url: uriBase + "?" + $.param(params),

        // Request headers.
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
        },

        type: "POST",

        // Request body.
        data: '{"url": ' + '"' + sourceImageUrl + '"}',
    })
    .done(function(data) {
        // Show formatted JSON on webpage.
        $("#responseTextArea").val(JSON.stringify(data, null, 2));
    })

    .fail(function(jqXHR, textStatus, errorThrown) {
        // Display error message.
        var errorString = (errorThrown === "") ?
            "Error. " : errorThrown + " (" + jqXHR.status + "): ";
        errorString += (jqXHR.responseText === "") ?
            "" : (jQuery.parseJSON(jqXHR.responseText).message) ?
                jQuery.parseJSON(jqXHR.responseText).message :
                    jQuery.parseJSON(jqXHR.responseText).error.message;
        alert(errorString);
    });
};

document.addEventListener('DOMContentLoaded', function() {
    var analyse = document.getElementById('analyse_button');
    analyse.addEventListener('click', function() {
        processImage();
    });
>>>>>>> 030d9be53a567cb35abdd268beea81e1793bb95d
>>>>>>> 5bb79606953cd0b89a3dacedf1ae6ab54bef007d
});