import cv2, pafy  


def frameCapture(url): 
    # Path to video file 
    # url = 'https://youtu.be/W1yKqFZ34y4'
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="webm")
    vidObj = cv2.VideoCapture(play.url) 


    count = 0
    success = 1
  
    while success: 
    
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read()   

        if count%30==0:
            cv2.imwrite("Videoframes/frame%d.jpg" % count, image)
            
        count += 1
  
# if __name__ == '__main__':
#     frameCapture("https://www.youtube.com/watch?v=W1yKqFZ34y4&feature=youtu.be")


