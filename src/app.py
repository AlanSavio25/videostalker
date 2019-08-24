from flask import Flask, redirect, request
import main
import videoframes
import time
from time import sleep

app = Flask(__name__)

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
    if (len(faces)>0):
      data.append(faces)
    print("%f percentage done \n" % (100*count/len(filenames)))
    time.sleep(3)
    count+=1
  
  for i in data:
    picdata = main.frameAverage(i)
    totalData.append(picdata)
  finalJson = main.overallAverage(totalData)
  return str(finalJson)

@app.route("/videoframe", methods = ['GET', 'POST'])
def videoframe():
  if request.method == 'GET':
    videoframes.frameCapture("https://www.youtube.com/watch?v=wjIes1eGAw4")
    return redirect('/average')
  if request.method == 'POST'
    print("Your POST request is: " + request)

if __name__ == "__main__":
    app.run(debug=True)