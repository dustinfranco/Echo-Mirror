from BrightnessControl import minToMaxScreenBrightness, maxToMinScreenBrightness
from showImage import showImage
import sys
import cv2
path = "/Library/emp/"
showImage(path + "old_picture_Rotated_safe.png", rotated = True)
    
while(1):
    showImage(path + "black_Rotated.png", rotated = True)
    try:
        showImage(path + "old_picture_Rotated.png", rotated = True)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        showImage(path + "old_picture_Rotated_safe.png", rotated = True)

     