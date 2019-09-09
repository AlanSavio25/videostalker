from flask import Flask, redirect, request
import main
import videoframes
import time
import json
from time import sleep
from flask_cors import CORS
global listOfVideos
listOfVideos = []
listofEvery10 = []
app = Flask(__name__)
CORS(app)
# @app.route("/average", methods = ['GET', 'POST'])
def average(listOfVideos):
  print("Video frames ready")
  print("Starting averaging...")
  filenames = main.loopdir("C:/Users/alans/Desktop/MicrosoftAzure/videostalker/src/frames")
  vals = main.connectToFaceAPI('16d17acb6e14429db19bdc89ff8291e7')

  data = []
  totalData = []
  count = 0
  for file in filenames:
    faces = main.getFaceResponse('https://face-ugrade.cognitiveservices.azure.com/face/v1.0/detect', file, vals[0], vals[1])
    if (len(faces)>0):
      data.append(faces)
    print("%f percentage done \n" % (100*count/len(filenames)))
    time.sleep(3)
    count+=1
  
  for i in data:
    picdata = main.frameAverage(i)
    totalData.append(picdata)
  finalJson = main.overallAverage(totalData)
  listOfVideos.append(finalJson)


@app.route("/videoframe", methods = ['GET', 'POST'])
def videoframe():
  if request.method == 'GET':
    videoframes.frameCapture("https://www.youtube.com/watch?v=wjIes1eGAw4")
    average(listOfVideos)
    if len(listOfVideos)%2==0:
      # average(listofEvery10)
      resultof10 = main.overallAverage(listOfVideos[-10:])
      return (json.dumps(resultof10, indent=4, sort_keys=True))
    return "Finished one"
  if request.method == 'POST':
    
    url = request.args['link']
    print("URL is: " + url)
    videoframes.frameCapture(url)
    average(listOfVideos)
    # if len(listOfVideos)%2==0:
      # average(listofEvery10)
    resultof10 = main.overallAverage(listOfVideos[-10:])
    return str(resultof10)
    #print(json.dumps(listOfVideos, indent=4, sort_keys=True))
    # return "Finished one"


if __name__ == "__main__":
    app.run(debug=True)