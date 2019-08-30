function myfunc(){
    // console.log(localStorage["link"])
    // document.getElementById("outputdiv").innerHTML = `anger:${localStorage["anger"]}`+ "<br>"+ `contempt:${localStorage["contempt"]}`+ "<br>" + `disgust:${localStorage["disgust"]}`;
    document.getElementById("outputdiv").innerHTML = localStorage["jsondata"] + JSON.parse(localStorage["jsondata"])["emotion"]["anger"]
    
    // console.log(JSON.stringify(localStorage["jsondata"]))
    // document.getElementById("outputdiv").innerHTML =  "anger:" + localStorage["anger"];
    // document.getElementById("outputdiv").innerHTML = localStorage["disgust"];
    // console.log(localStorage["anger"])
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').addEventListener('click', myfunc);
  });

// document.getElementById("outputdiv").innerHTML = localStorage["link"];

// var outputdiv = document.getElementById("outputdiv")
// outputdiv.innerHTML = localStorage["anger"];
