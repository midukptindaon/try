import math
import cv2
import time
import hand_tracking_dummy_code as htdc
import numpy as np

"""grimacing face print("\U0001F62C")"""

########################
wCam, hCam = 640, 480
########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

minVol = 0
maxVol = 0
volBar = 0
volPercentage = 0

detector = htdc.handDetector()

pTime = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2] # thumb finger's value
        x2, y2 = lmList[8][1], lmList[8][2] # index finger's value
        cx, cy = (x1+x2)//2, (y1+y2)//2 # middle dot value
        "/ is normal division produces float value e.g 5/2=2.5"
        "// is floor division produces int value e.g 5/2=2"
        cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
        "making a line in between"
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

        length = int(math.hypot(x2-x1, y2-y1))
        print(length)

        if length <= 90:
            cv2.putText(img, f'Itok yang cantik', (200, 200), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 0, 250), 8)
        if 90 <= length <= 180:
            cv2.putText(img, f'I LOVE YOU', (200, 200), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 0, 250), 8)
        if 180 <= length <= 270:
            cv2.putText(img, f'Will You Love Me Too', (100, 200), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 0, 250), 8)
        if 270 <= length <= 400:
            cv2.putText(img, f'\U0001F62C', (200, 200), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 0, 250), 8)


        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPercentage = np.interp(length, [50, 300], [0, 100])


    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f':{int(volPercentage)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 2)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FrPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
