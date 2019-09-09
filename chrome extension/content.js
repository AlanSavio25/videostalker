var youtubelink = window.location.toString()
var data;
$.ajax({
  url: "http://127.0.0.1:5000/videoframe" + "?link=" + youtubelink,
  data : youtubelink,
  type: "POST",  
  success: function(res) {
    console.log(res.replace(/'/g, '"'))
    
  }
}).done(function(data) {
  alert("Attempting to store to Local Storage..")
  chrome.runtime.sendMessage({
    jsondata : data.replace(/'/g, '"')
  });
  window.localStorage.setItem('jsonstring', data);
 })


