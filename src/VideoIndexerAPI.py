from pprint import pprint
from video_indexer import VideoIndexer

CONFIG = {
    "SUBSCRIPTION_KEY": "77893956f6d0401abb40291b4afec19c",
    "LOCATION": "trial",
    "ACCOUNT_ID": "8457154a-07a0-4874-bb51-2c0aa361db22",
}

vi = VideoIndexer(
    vi_subscription_key=CONFIG["SUBSCRIPTION_KEY"],
    vi_location=CONFIG["LOCATION"],
    vi_account_id=CONFIG["ACCOUNT_ID"],
)
#Upload video to indexer

video_id = vi.upload_to_video_indexer(
    input_filename="https://www.youtube.com/watch?v=oPpzJAzdpTU",
    video_name="video1",
    video_language="English",
)

#Get video info from indexer

info = vi.get_video_info(video_id, video_language="English")

pprint(info)

#Get Brands

brands = info['summarizedInsights']['brands']
pprint(brands)

#Get topics 

topics = info['videos'][0]['insights']['topics']

print('TOPICS:')
for i in range(len(info['videos'][0]['insights']['topics'])):
    topic = info['videos'][0]['insights']['topics'][i]['name']
    pprint(topic)

#Get named people

named_people=info['videos'][0]['insights']['namedPeople']

print('NAMED_PEOPLE:')
for i in range(len(info['videos'][0]['insights']['namedPeople'])):
    person = info['videos'][0]['insights']['namedPeople'][i]['name']
    pprint(person)

#Get Transcript

transcript = ''
for i in range(len(info['videos'][0]['insights']['transcript'])):
    text = info['videos'][0]['insights']['transcript'][i]['text']  
    #print(text)
    transcript +=text

pprint(transcript)
   