import cv2, pafy  
import os
import shutil

def frameCapture(url): 
    # Path to video file 
    # url = 'https://youtu.be/W1yKqFZ34y4'
    # vPafy = pafy.new(url)
    # play = vPafy.getbest(preftype="webm")
    # vidObj = cv2.VideoCapture(play.url) 
    dir = "C:/Users/alans/Desktop/MicrosoftAzure/videostalker/frames/"
    if os.path.exists(dir):
        print("File does exist!")
        shutil.rmtree(dir)
        print("Update: File exists- " + str(os.path.exists(dir)))
    os.makedirs(dir)

        
        


    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    capture = cv2.VideoCapture()
    capture.open(best.url)

    count = 0
    success = 1
  
    while success: 
        # vidObj object calls read 
        # function extract frames 
        success, image = capture.read()   

        if count%100==0:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30)) 
            # print("Found {0} Faces!".format(len(faces)))
            if len(faces)>0:
                status = cv2.imwrite("frames/frame%d.jpg" % count, image)
                if(not status):
                    print("Failed to write Image: frames/frame%d.jpg" % count)
        count += 1

# frameCapture("https://www.youtube.com/watch?v=cT1Kzk7akjQ")
