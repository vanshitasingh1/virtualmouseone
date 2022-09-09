import cv2
import numpy as np
import autopy
import handrecognition as htm
import time
import mediapipe as mp

cTime = 0
pTime = 0
cap = cv2.VideoCapture(0)
detector= htm.handDetector(maxHands=1)
while (True):
    #1
    ret, img = cap.read()
    image = detector.findHands(img)
    lmlisy, bbox = detector.findPosition(img)
    #2
    #3
    #4
    #5
    #6
    #7
    #8
    #9
    #10
    #11
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    #12
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

