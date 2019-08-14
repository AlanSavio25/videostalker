import json
import requests
import azure
import azure.cognitiveservices
from msrest.authentication import CognitiveServicesCredentials
import requests
from io import BytesIO
from PIL import Image, ImageDraw
from pprint import pprint
import json
import statistics as st

url = "https://i0.wp.com/sitn.hms.harvard.edu/wp-content/uploads/2018/11/Fig2.jpg?resize=768%2C512"
#################################################################################################################
subscription_key = 'your key'
assert subscription_key

face_api_url = 'https://faceapi-alan.cognitiveservices.azure.com/face/v1.0/detect'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,hair,makeup',
}

img_url1 = 'https://images.performgroup.com/di/library/omnisport/a4/1b/lionelmessi-cropped_1gkj19cowm6ee1rntkhz44784v.jpg?t=1579297980&quality=60&w=640&h=360'
img_url2 = 'https://pmcdeadline2.files.wordpress.com/2019/08/barack-obama.jpg?w=681&h=383&crop=1'

response  = requests.post(face_api_url,params=params, headers=headers,  json={"url": img_url2})

faces = response.json()

# Download the image from the url
response = requests.get(img_url2)
img = Image.open(BytesIO(response.content))

headers = {'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key}

img = open('C:/Users/alans/Desktop/29664935_1826046541029897_4816426771371512794_o.jpg', 'rb')

response  = requests.post(face_api_url,params=params, headers=headers,  data=img)
faces = response.json()

# for i in range(len(faces)):
#     face_att = faces[i]['faceAttributes']
#     pprint(face_att)

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

pprint(jsonData)

with open('data.json', 'w') as outfile:
    json.dump(jsonData, outfile)
# link = 'https://www.youtube.com/watch?v=t67_zAg5vvI'
# page = urllib2.urlopen(link)

# soup = BeautifulSoup(page)

# print(soup.prettify())