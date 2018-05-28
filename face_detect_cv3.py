import cv2
import sys
import imutils
from PIL import Image
from showImage import showImage
path = "/Library/emp/"

def createRotatedCopy(fileName = "", fileType = ".png", rotation = 90, downSize = True):
    img = Image.open(fileName + fileType)
    img2 = img.rotate(-90, expand = True)
    img2.save(fileName + "_Rotated" + fileType)
    

def findNumberOfFaces(imageName, imageType, inputScaleFactor = 1.1, rectangle = False, sizeRatio = 1.0, minXFaceSize = 15, minYFaceSize = 15):
    # Get user supplied values
    imagePath = imageName + imageType
    imageRotatedPath = imageName + "_Rotated" + imageType
    createRotatedCopy(imageName, imageType)
    
    #print("RIGHT HERE BABY")
    cascPath = "/users/dustinfranco/desktop/echo-mirror/haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    #print(type(faceCascade))
    
    # Read the image
    image = cv2.imread(imageRotatedPath)
    if(sizeRatio != 1.0):
        #print("downsizing image")
        height, width, channels = image.shape
        #print height, width, channels
        image = changeProportionalSize(image, sizeRatio)
        height, width, channels = image.shape
        #print height, width, channels
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print("TYPE OF GRAY:")
    #print(type(gray))
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(15, 15)
        #flags re= cv2.CV_HAAR_SCALE_IMAGE
    )
    
    # Draw a rectangle around the faces0
    if(rectangle):
        for (x, y, w, h) in faces:
            cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("test", image)
            key=cv2.waitKey(0)
    #else:
    #    for (x, y, w, h) in faces:
    #        print("FACE SIZE: " + str(w-x) + "," + str(h-y))
            
    return len(faces)

def changeProportionalSize(img, ratio = 0.5):
    height, width, channels = img.shape
    newX = int(width * ratio)
    newY = int(height * ratio)
    img = cv2.resize(img, (newX, newY))
    cv2.imwrite("/Library/emp/resized.png", img)
    return img
    
