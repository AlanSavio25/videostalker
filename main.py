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

url = "https://i0.wp.com/sitn.hms.harvard.edu/wp-content/uploads/2018/11/Fig2.jpg?resize=768%2C512"
#################################################################################################################
subscription_key = 'b8ea8ee7334149cebd7ed530acdf84d7'
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

for i in range(len(faces)):
    face_att = faces[i]['faceAttributes']
    pprint(face_att)