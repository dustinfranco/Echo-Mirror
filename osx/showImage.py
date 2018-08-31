import cv2
import time
import imutils

def showImage(inputFileName, rotated = True):
        #print 'loading images...'
        img = cv2.imread(inputFileName)
        # Note: 900x1440 is the resolution with my MBP
        if(rotated):
            img = cv2.resize(img, (1440, 2560), interpolation=cv2.INTER_CUBIC)
        else:
            img = cv2.resize(img, (2560, 1440), interpolation=cv2.INTER_CUBIC)
        
        cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("test", img)
        key=cv2.waitKey(0)

def AddTextToImage(fileNameIn, fileNameOut, textToAdd, x = 2, y = 255, color = (255,255,255), scale = 2):
        #print 'loading images...'
        img = cv2.imread(fileNameIn)
        # Note: 900x1440 is the resolution with my MBP
        img = cv2.resize(img, (2560, 1440), interpolation=cv2.INTER_CUBIC)
        cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        img = imutils.rotate_bound(img, 90)
        cv2.putText(img, textToAdd, (x,y), cv2.FONT_HERSHEY_SIMPLEX, scale, color)
        img = imutils.rotate_bound(img, -90)
        return img
    
def addTextToBlackImage(textToAdd, x = 2, y = 255, color = (255,255,255), scale = 2):
    img = AddTextToImage("/users/dustinfranco/desktop/blackness.jpg", "", textToAdd)
    return img