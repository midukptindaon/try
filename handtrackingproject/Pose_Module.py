import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode=False, modelCompxty=1, smoothLms=True,
                 enableSeg=False, smoothSeg=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.modelCompxty = modelCompxty
        self.smoothLms = smoothLms
        self.enableSeg = enableSeg
        self.smoothSeg = smoothSeg
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.modelCompxty,
                                     self.smoothLms, self.enableSeg,
                                     self.smoothSeg, self.detectionCon,
                                     self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                      self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, lm)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 1, (144, 238, 144), cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        #print(lmList[14])
        #cv2.circle(img, (lmList[1][1], lmList[1][2]), 10, (144, 238, 144), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        """putting time text"""
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (144, 238, 144), 3)
        """"Processing the command"""
        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
