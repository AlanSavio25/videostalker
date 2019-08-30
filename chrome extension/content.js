var youtubelink = window.location.toString()
console.log(youtubelink)

var anger = ""
var contempt = ""
var disgust =""
// var fear = ""
// var happiness = ""
// var neutral = ""
// var sadness = ""
// var surprise = ""
var data = {}
$.ajax({
  url: "http://127.0.0.1:5000/videoframe" + "?link=" + youtubelink,
  data : youtubelink,
  type: "POST",  
  success: function(res) {
    console.log(res);
    data = JSON.stringify(res)
    anger = String(res["emotion"]["anger"]);
    contempt = String(res["emotion"]["contempt"]);
    disgust  = String(res["emotion"]["disgust"]);
  },
  async:false
})


console.log(typeof (data))

// Send youtube link variable to popup.js

// chrome.runtime.sendMessage({
//     link: youtubelink 
//   });

// Send emotion values to popup.js

chrome.runtime.sendMessage({
    // anger: anger,
    // contempt: contempt ,
    // disgust: disgust
    jsondata : data
  });



