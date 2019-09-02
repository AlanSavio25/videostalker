var youtubelink = window.location.toString()
console.log(youtubelink)

var data = {}
$.ajax({
  url: "http://127.0.0.1:5000/videoframe" + "?link=" + youtubelink,
  data : youtubelink,
  type: "POST",  
  success: function(res) {
    console.log(res);
    data = JSON.stringify(res)
  },
  async:false
})


// Send data to popup.js

chrome.runtime.sendMessage({

    jsondata : data
    
  });



