import cv2
import time

characterGuess = ''
questionNum = 0
points = 0

def gameStart():
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
        else:
                rval = False

        while rval:
                cv2.imshow("preview", frame)
                rval, frame = vc.read()
                key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                        break

        vc.release()
        cv2.destroyWindow("preview")

def gameLoop():
        print("game loop")
        return False

def waitTime():
        return False

def questionMode():
        return False

#cv2.namedWindow("preview")
#cam = cv2.VideoCapture(0)


    
        #ret, frame = cam.read()
        #if not ret:
        #    print("failed")
        #    break
        #cv2.imshow('camera', frame)

        #k = cv2.waitKey(1)
        #if k % 256 == 27:
        #    print("closing app...")

#cam.release()
#cam.destroyAllWindows()
#cv2.waitKey(1) 