var chart;
var charts = [];
var width;
var height;
var js = JSON.parse(localStorage["jsondata"])
em = js.emotion
emotionSum = 0.00
for (var key in em) {
    emotionSum += em[key]
}

var classNumber = 0
document.getElementById("number1").style.display = "none";
document.getElementById("number2").style.display = "none";
// document.getElementById("number3").style.display = "none";
// document.getElementById("number4").style.display = "none";
var fav = "beard";
if(js.facialHair.sideburns>js.facialHair.moustache && js.facialHair.sideburns>js.facialHair.beard){ fav = "sideburns" }
else if(js.facialHair.moustache>js.facialHair.sideburns && js.facialHair.moustache>js.facialHair.beard){ fav = "moustache" }

document.getElementById("number1").innerHTML += "<b>" + fav + "</b>" + "!!";
document.getElementById("number2").innerHTML += parseInt(js.age) + "!!";



$('.carousel-control.left').click(function() {
  document.getElementById("number"+classNumber).style.display = "none";
  classNumber += -1
  if(classNumber==-1){
    classNumber = 2
  }
  console.log(classNumber)
  document.getElementById("number"+classNumber).style.display = "block";  
});

$('.carousel-control.right').click(function() {
  document.getElementById("number"+classNumber).style.display = "none";
  classNumber += 1
  if(classNumber==3){
    classNumber = 0
  }
  console.log(classNumber)
  document.getElementById("number"+classNumber).style.display = "block";  
});

width = $('#carousel-example-generic').width();
height = $('#carousel-example-generic').height();
$('.carousel').carousel({
  interval: false,
});
chart = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	title: {
		text: "Emotions"
	},
	data: [{
		type: "pie",
		startAngle: 240,
		yValueFormatString: "##0.00\"%\"",
		indexLabel: "{label} {y}",
		dataPoints: [
			{y: parseFloat(em.anger/emotionSum), label: "Anger"},
			{y: parseFloat(em.contempt/emotionSum), label: "Contempt"},
			{y: parseFloat(em.disgust/emotionSum), label: "Disgust"},
			{y: parseFloat(em.fear/emotionSum), label: "Fear"},
      {y: parseFloat(em.sadness/emotionSum), label: "Sadness"},
      {y: parseFloat(em.surprise/emotionSum), label: "Surprise"},
      {y: parseFloat(em.happiness/emotionSum), label: "Happiness"},
      {y: parseFloat(em.neutral/emotionSum), label: "Neutral"}
		]
	}]
});
chart.render();
charts.push(chart);

chart = new CanvasJS.Chart("chartContainer2", {
  title: {
    text: "Most Appearing Facial Hair in the Videos You watch"
  },
  width: width,
  height: height,
  data: [{
    type: "column",
    dataPoints: [{ y: js.facialHair.beard*100, label: "Beard" },
    { y: js.facialHair.moustache*100,  label: "Moustache" },
    { y: js.facialHair.sideburns*100,  label: "Sideburns" }]
  }]
});
chart.render();
charts.push(chart);

chart = new CanvasJS.Chart("chartContainer3", {
  title: {
    text: "Like to know how old the people you view most often are?"
  },
  width: width,
  height: height,
  data: [{
    type: "bar",
    color: "#014D65",
		axisYType: "secondary",
    dataPoints: [
      { y: js.age, label: "Age" }
      ]
  }]
});
chart.render();
charts.push(chart);

$(window).resize(function() {
  for (var i = 0; i < charts.length; i++) {
    charts[i].options.width = $('.carousel').width();
    charts[i].options.height = $('.carousel').height();
    charts[i].render();
  }
});
