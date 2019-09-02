function myfunc() {
  var viddata = JSON.parse(localStorage["jsondata"])
  document.getElementById("outputdiv").innerHTML = `anger:${viddata["emotion"]["anger"]}` + "<br>" + `contempt:${viddata["emotion"]["contempt"]}` + "<br>" + `disgust:${viddata["emotion"]["disgust"]}` + "<br>";
  // document.getElementById("outputdiv").innerHTML = "total data:" + localStorage["youtubeoverall"]
  console.log(localStorage["youtubeoverall"])
  // document.getElementById("outputdiv").innerHTML = localStorage["jsondata"] + JSON.parse(localStorage["jsondata"])["emotion"]["anger"]
}

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById("mybutton").addEventListener('click', myfunc);
});


