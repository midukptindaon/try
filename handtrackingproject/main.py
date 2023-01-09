import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


"""previous time"""
pTime = 0
"""current time"""
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for i in results.multi_hand_landmarks:
            for id, lm in enumerate(i.landmark):
                mpDraw.draw_landmarks(img, i, mpHands.HAND_CONNECTIONS)
                """for getting the index number of hand"""
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                """identifying each id number on hand image dots"""
                if id == 0:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255))
                print(id, cx, cy)


    cTime = time.time()
    """"frame rates"""
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    """fps, scale, value of position, font, scale, color, and thickness"""
    #print(results.multi_hand_landmarks)

    cv2.imshow("image", img)
    cv2.waitKey(1)
