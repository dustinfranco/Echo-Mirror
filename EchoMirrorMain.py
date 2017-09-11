import cv2
import os
import time
import facedetectection
from BrightnessControl import minToMaxScreenBrightness, maxToMinScreenBrightness
currentPath = os.path.dirname(os.path.realpath(__file__))

#credit to https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Press and release space

def takePicture():
    camera_port = 1
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)
     
    def get_image():
         retval, im = camera.read()
         return im
    for i in xrange(ramp_frames):
         get_image()
    camera_capture = get_image()
    file = "/users/dustinfranco/desktop/new_picture.jpg"
    cv2.imwrite(file, camera_capture)
    return 

while(1):
    maxToMinScreenBrightness(0.01)
    keyboard.press("0")
    keyboard.release("0")
    takePicture()
    time.sleep(3)
    keyboard.press("0")
    keyboard.release("0")
    time.sleep(3)
    minToMaxScreenBrightness(0.01)


