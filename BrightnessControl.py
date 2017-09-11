import subprocess
import os
import time

currentPath = os.path.dirname(os.path.realpath(__file__))

def setBrightness(inputBrightness = 1.0):
    subprocess.call([currentPath + "/brightness control/dbrightness", str(inputBrightness)])

def minToMaxScreenBrightness(speed = 0.01):
    for m in range(0,1):
        for x in range (0,101):
            	setBrightness(x/100.0)
            	time.sleep(speed)
                
def maxToMinScreenBrightness(speed = 0.01):
    for x in range (0,101):
        	setBrightness((100.0 - x)/100.0)
        	time.sleep(speed)
            