import cv2

def take_snapshot():
    #initialize the cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite( to save an image to the storage)
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False

    #release the cam
    videoCaptureObject.release()
    #close all the windows opened 
    cv2.destroyAllWindows()

take_snapshot()    
