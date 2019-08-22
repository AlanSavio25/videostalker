from flask import Flask, redirect, request
import main
import VideoIndexerAPI
import videoframes

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
  finalJson = main.frameAverage(jsonContainingEveryFrameJson)

@app.route("/video-indexer")
def s():
  return "Hello, Salvador"

@app.route("/frameSplit")
def frameSplit():
  videoframes.frameCapture("https://www.youtube.com/watch?v=NrJEFrth27Q")

if __name__ == "__main__":
    app.run(debug=True)