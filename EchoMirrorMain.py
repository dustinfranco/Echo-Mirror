import cv2
import os
import time
from shutil import copy
from face_detect_cv3 import findNumberOfFaces
from BrightnessControl import minToMaxScreenBrightness, maxToMinScreenBrightness
currentPath = os.path.dirname(os.path.realpath(__file__))
from showImage import showImage
#credit to https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/
from pynput.keyboard import Key, Controller
import imutils
import numpy as np
from subprocess import Popen, PIPE
from clickOnCorner import clickOnCorner
path = "/Library/emp/"
keyboard = Controller()
cv2.importlib 
# Press and release space

def takePicture(inputFileName = "", flip = True):
    camera_port = 1
    ramp_frames = 0
    camera = cv2.VideoCapture(camera_port)
    counter = 1;
    camera_capture = None
    def get_image():
        retval, im = camera.read()
        return im
    for i in xrange(ramp_frames):
         get_image()
    while(type(camera_capture) == type(None)):
        if(counter > 20):
            time.sleep(counter)
        if(counter < 120):
            counter += 1
        camera_capture = get_image()
        file = inputFileName
        #print("camera capture is type")
        if(flip):
            camera_capture = cv2.flip( camera_capture, 1 )
        #print("writing piture")
        cv2.imwrite(file, camera_capture)
    return 

def echoMirrorCycle():
            maxToMinScreenBrightness(0.003)
            clickOnCorner()
            numberOfFaces = 1;
            #debounce faces
            keyboard.press("0")
            keyboard.release("0")
            while(numberOfFaces > 0):
                takePicture(path + "temp_picture.png")
                numberOfFaces = findNumberOfFaces(path + "temp_picture",".png", 1.1, False,  0.5, 10, 10)
                #print("LEN FACES DEBOUNCE " + str(numberOfFaces))
            
            
            
            #print("C")
            copy(path + "new_picture.png",path + "old_picture.png")
            copy(path + "new_picture_Rotated.png",path + "old_picture_Rotated.png")
            
            #look for a face
            while(numberOfFaces == 0 or numberOfFaces > 1):
                #print("D")
                takePicture(path + "new_picture.png")
                #print("e")
                numberOfFaces = findNumberOfFaces(path + "new_picture",".png", 1.1, False, 0.5, 10, 10)
                #print("LEN FACES SHOW " + str(numberOfFaces))
            #show picture and fade in last face
            
            keyboard.press("0")
            keyboard.release("0")
            minToMaxScreenBrightness(0.003)
            time.sleep(2)
def echoMirrorMain():
    minToMaxScreenBrightness(0.01)
    print("10 seconds until it starts")
    #time.sleep(10)
    #p = Popen(['python ImageDisplay.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    clickOnCorner()
    while(1):
            x = echoMirrorCycle()
            del x

def echoMirrorTest():
    while(1):
            #print("take pitcture debounce")
            takePicture(path + "new_picture.png")
            #print("find faces debounce")
            numberOfFaces = findNumberOfFaces(path + "new_picture",".png", 1.1, True)
            #print("LEN FACES DEBOUNCE " + str(numberOfFaces))
         
echoMirrorMain()