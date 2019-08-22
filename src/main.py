import json
import requests
import azure
import azure.cognitiveservices
from msrest.authentication import CognitiveServicesCredentials
import requests
from io import BytesIO
from pprint import pprint
import json
import statistics as st
import videoframes


def connectToFaceAPI(subscription_key):
	assert subscription_key
	print("Hello")
	headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}
	params = {
		'returnFaceId': 'true',
		'returnFaceLandmarks': 'false',
		'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,hair,makeup',
	}
	return [headers, params]

def getFaceResponse(face_api_url, image, headers, params):
	img = open(image, 'rb')
	response  = requests.post(face_api_url,params=params, headers=headers,  data=img)
	faces = response.json()
	return faces

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
	jsonData['hair'] = {'bald': 0.0, 'hairColor': '' }

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

	jsonData['age'] = age/len(faces)  #average age of all faces in a single frame
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


# if __name__ == '__main__':
	# vals = connectToFaceAPI('b8ea8ee7334149cebd7ed530acdf84d7')
	# faces = getFaceResponse('https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect', 'C:/Users/alans/Desktop/29664935_1826046541029897_4816426771371512794_o.jpg', vals[0], vals[1])
	# jsonData = frameAverage(faces)
	# pprint(jsonData)
	# writeJsonDatatoFile(jsonData)
	# videoframes.frameCapture("https://www.youtube.com/watch?v=W1yKqFZ34y4&feature=youtu.be")



	# for i in range(len(faces)):
	# 	face_att = faces[i]['faceAttributes']
	# 	pprint(face_att)
