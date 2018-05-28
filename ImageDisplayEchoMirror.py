from BrightnessControl import minToMaxScreenBrightness, maxToMinScreenBrightness
from showImage import showImage
import cv2
path = "/Library/emp/"

while(1):
    showImage(path + "old_picture.png")
    showImage(path + "black.jpg")