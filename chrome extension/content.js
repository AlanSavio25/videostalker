var youtubelink = window.location.toString()

$.ajax({
  url: "http://127.0.0.1:5000/videoframe" + "?link=" + youtubelink,
  data : youtubelink,
  type: "POST",  
  success: function(res) {
    console.log(res)
  }
})
