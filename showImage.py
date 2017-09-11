import cv2

def showImage(inputFileName):
        print 'loading images...'
        img = cv2.imread(inputFileName)
        # Note: 900x1440 is the resolution with my MBP
        img = cv2.resize(img, (2560, 1440), interpolation=cv2.INTER_CUBIC)
        cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("test", img)
        key=cv2.waitKey(0)
        