from flask import Flask, redirect, request
import main
import videoframes
import time
from time import sleep

app = Flask(__name__)

@app.route("/face-api")
def face():
  vals = main.connectToFaceAPI('b8ea8ee7334149cebd7ed530acdf84d7')
  faces = main.getFaceResponse('https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect', 'C:/Users/alans/Desktop/29664935_1826046541029897_4816426771371512794_o.jpg', vals[0], vals[1])
  jsonData = main.frameAverage(faces)
  # pprint(jsonData)
  return str(jsonData)


@app.route("/average")
def average():
  print("Video frames ready")
  print("Starting averaging...")
  filenames = main.loopdir("C:/Users/alans/Desktop/MicrosoftAzure/videostalker/src")
  vals = main.connectToFaceAPI('b8ea8ee7334149cebd7ed530acdf84d7')

  data = []
  totalData = []
  count = 0
  for file in filenames:
    faces = main.getFaceResponse('https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect', file, vals[0], vals[1])
    data.append(faces)
    print("%f percentage done \n" % (100*count/len(filenames)))
    time.sleep(3)
    count+=1
  
  for i in data:
    picdata = main.frameAverage(i)
    totalData.append(picdata)
  finalJson = main.overallAverage(totalData)
  return str(finalJson)

@app.route("/videoframe")
def videoframe():
  videoframes.frameCapture("https://www.youtube.com/watch?v=cT1Kzk7akjQ")
  return redirect('/average')

@app.route("/frameSplit")
def frameSplit():
  videoframes.frameCapture("https://www.youtube.com/watch?v=NrJEFrth27Q")

if __name__ == "__main__":
    app.run(debug=True)