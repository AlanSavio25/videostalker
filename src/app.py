from flask import Flask, redirect, request
import main
app = Flask(__name__)

@app.route("/face-api")
def home():
  vals = main.connectToFaceAPI('b8ea8ee7334149cebd7ed530acdf84d7')
  faces = main.getFaceResponse('https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect', 'C:/Users/alans/Desktop/29664935_1826046541029897_4816426771371512794_o.jpg', vals[0], vals[1])
  jsonData = main.frameAverage(faces)
  # pprint(jsonData)
  return str(jsonData)

@app.route("/video-indexer")
def salvador():
  return "Hello, Salvador"


if __name__ == "__main__":
    app.run(debug=True)