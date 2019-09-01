import os
import json
import requests
import azure
import azure.cognitiveservices
from msrest.authentication import CognitiveServicesCredentials
from io import BytesIO
from pprint import pprint
import statistics as st
import time
from time import sleep

rootdir = "pics"

def loopdir(rootdir):
    filenames = []
    for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            filenames.append(filepath)


def connectToFaceAPI(subscription_key):
    assert subscription_key
    print("Hello")
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,hair,makeup',
    }
    return [headers, params]


def getFaceResponse(face_api_url, image, headers, params):
    img = open(image, 'rb')
    response = requests.post(face_api_url, params=params,
                             headers=headers,  data=img)
    faces = response.json()
    return faces


vals = connectToFaceAPI('b8ea8ee7334149cebd7ed530acdf84d7')

data = []
totalData = []
for file in filenames:
    faces = getFaceResponse(
        'https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect', file, vals[0], vals[1])
    data.append(faces)
    time.sleep(3)
for i in data:
    picdata = frameAverage(i)
    totalData.append(picdata)

# print(data)


def frameAverage(faces):
    jsonData = {}
    jsonData['emotion'] = {
        'anger': 0.0,
        'contempt': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'happiness': 0.0,
        'neutral': 0.0,
        'sadness': 0.0,
        'surprise': 0.0
    }
    jsonData['facialHair'] = {'beard': 0.0, 'moustache': 0.0, 'sideburns': 0.0}
    jsonData['hair'] = {'bald': 0.0, 'hairColor': ''}

    age = 0
    smile = 0
    # pprint(faces)

    for face in faces:
        fa = face['faceAttributes']
        age += fa['age']
        for em in fa['emotion']:
            jsonData['emotion'][em] += fa['emotion'][em]
        for hair in fa['facialHair']:
            jsonData['facialHair'][hair] += fa['facialHair'][hair]
        jsonData['hair']['bald'] += fa['hair']['bald']
        smile += fa['smile']

    # average age of all faces in a single frame
    jsonData['age'] = age/len(faces)
    for em in jsonData['emotion']:
        jsonData['emotion'][em] = jsonData['emotion'][em]/len(faces)
    for hair in fa['facialHair']:
        jsonData['facialHair'][hair] = jsonData['facialHair'][hair]/len(faces)
    jsonData['hair']['bald'] /= len(faces)
    jsonData['smile'] = smile/len(faces)
    return jsonData
    for face in faces:
        fa = face['faceAttributes']
        age += fa['age']
        for em in fa['emotion']:
            jsonData['emotion'][em] += fa['emotion'][em]
        for hair in fa['facialHair']:
            jsonData['facialHair'][hair] += fa['facialHair'][hair]
        jsonData['hair']['bald'] += fa['hair']['bald']
        smile += fa['smile']

    # average age of all faces in a single frame
    jsonData['age'] = age/len(faces)
    for em in jsonData['emotion']:
        jsonData['emotion'][em] = jsonData['emotion'][em]/len(faces)
    for hair in fa['facialHair']:
        jsonData['facialHair'][hair] = jsonData['facialHair'][hair]/len(faces)
    jsonData['hair']['bald'] /= len(faces)
    jsonData['smile'] = smile/len(faces)
    return jsonData


def writeJsonDatatoFile(jsonData):
    with open('data.json', 'w') as outfile:
        json.dump(jsonData, outfile)




# print(totalData)
def overallAverage(faces):
    jsonData = {}
    jsonData['emotion'] = {
        'anger': 0.0,
        'contempt': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'happiness': 0.0,
        'neutral': 0.0,
        'sadness': 0.0,
        'surprise': 0.0
    }
    jsonData['facialHair'] = {'beard': 0.0, 'moustache': 0.0, 'sideburns': 0.0}
    jsonData['hair'] = {'bald': 0.0, 'hairColor': ''}

    age = 0
    smile = 0
    # pprint(faces)

    for face in faces:
        fa = face
        age += fa['age']
        for em in fa['emotion']:
            jsonData['emotion'][em] += fa['emotion'][em]
        for hair in fa['facialHair']:
            jsonData['facialHair'][hair] += fa['facialHair'][hair]
        jsonData['hair']['bald'] += fa['hair']['bald']
        smile += fa['smile']

    # average age of all faces in a single frame
    jsonData['age'] = age/len(faces)
    for em in jsonData['emotion']:
        jsonData['emotion'][em] = jsonData['emotion'][em]/len(faces)
    for hair in fa['facialHair']:
        jsonData['facialHair'][hair] = jsonData['facialHair'][hair]/len(faces)
    jsonData['hair']['bald'] /= len(faces)
    jsonData['smile'] = smile/len(faces)
    return jsonData
    for face in faces:
        fa = face
        age += fa['age']
        for em in fa['emotion']:
            jsonData['emotion'][em] += fa['emotion'][em]
        for hair in fa['facialHair']:
            jsonData['facialHair'][hair] += fa['facialHair'][hair]
        jsonData['hair']['bald'] += fa['hair']['bald']
        smile += fa['smile']

    # average age of all faces in a single frame
    jsonData['age'] = age/len(faces)
    for em in jsonData['emotion']:
        jsonData['emotion'][em] = jsonData['emotion'][em]/len(faces)
    for hair in fa['facialHair']:
        jsonData['facialHair'][hair] = jsonData['facialHair'][hair]/len(faces)
    jsonData['hair']['bald'] /= len(faces)
    jsonData['smile'] = smile/len(faces)
    return jsonData


# j = overallAverage(totalData)

# print(j)


