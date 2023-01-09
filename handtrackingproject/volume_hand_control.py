import math
import cv2
import time
import mediapipe as mp
import hand_tracking_dummy_code as htdc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400
volPercentage = 0

########################
wCam, hCam = 640, 480
########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htdc.handDetector()

pTime = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

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

        length = math.hypot(x2-x1, y2-y1)
        #print(length)

        # hand range -63.5 - -28.5
        # volume range -65 - 0

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPercentage = np.interp(length, [50, 300], [0, 100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255,0 , 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f':{int(volPercentage)}%', (40,450), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FrPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
