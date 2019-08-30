from flask import Flask, redirect, request
import main
import videoframes
import time
from time import sleep
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/average", methods = ['GET', 'POST'])
def average():
  print("Video frames ready")
  print("Starting averaging...")
  filenames = main.loopdir("C:/Users/alans/Desktop/MicrosoftAzure/videostalker/src/frames")
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
  print(finalJson)
  return str(finalJson)

@app.route("/videoframe", methods = ['GET', 'POST'])
def videoframe():
  if request.method == 'GET':
    videoframes.frameCapture("https://www.youtube.com/watch?v=wjIes1eGAw4")
    return redirect('/average')
  if request.method == 'POST':
    s = ("Your POST request is: " + str(request.data))
    url = request.args['link']
    print("URL is: " + url)
    videoframes.frameCapture(url)
    print("Successfully created video frames, starting averaging..")
    return redirect('/average')

if __name__ == "__main__":
    app.run(debug=True)