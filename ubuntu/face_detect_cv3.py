import cv2
import sys
import imutils
import os
import time

path = "/Library/emp/"

def findNumberOfFaces(imageName, imageType, inputScaleFactor = 1.1, rectangle = False, sizeRatio = 1.0, minXFaceSize = 15, minYFaceSize = 15):
    m = int(round(time.time() * 1000))
    print (m)
    image = cv2.imread("./pics/out.png")

    cascPath = "./haarcascade_frontalface_default.xml"
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    faces = faceCascade.detectMultiScale(
        #gray,
        image,
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
    m = int(round(time.time() * 1000)) - m
    print ("it took " + str(m) + "ms to find faces")
    return len(faces)

def changeProportionalSize(img, ratio = 0.5):
    height, width, channels = img.shape
    newX = int(width * ratio)
    newY = int(height * ratio)
    img = cv2.resize(img, (newX, newY))
    cv2.imwrite("/Library/emp/resized.png", img)
    return img
    
