import cv2
import mediapipe as mp
import time


class faceDetector():
    def __init__(self, minDetectionCon=0):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetect = self.mpFaceDetection.FaceDetection(minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetect.process(imgRGB)

        if self.results.detections:
            bboxes = []
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                "imageheight, imagewidth, imagechannel"
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin*iw), int(bboxC.ymin*ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxes.append([id, bbox, detection.score])
                if draw:
                    img = self.fancyDraw(img, bbox)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                (bbox[0], bbox[1]-10),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        return img, bboxes

    def fancyDraw(self, img, bbox, l=15, t=2):
        "l = length, t = thickness"
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (0, 255, 0), 1)
        "top-left corner line"
        cv2.line(img, (x, y), (x+l, y), (0, 255, 0), t)
        cv2.line(img, (x, y), (x, y+l), (0, 255, 0), t)
        "top-right corner line"
        cv2.line(img, (x1, y), (x1 - l, y), (0, 255, 0), t)
        cv2.line(img, (x1, y), (x1, y + l), (0, 255, 0), t)
        "bottom-left corner line"
        cv2.line(img, (x, y1), (x + l, y1), (0, 255, 0), t)
        cv2.line(img, (x, y1), (x, y1 - l), (0, 255, 0), t)
        "bottom-right corner line"
        cv2.line(img, (x1, y1), (x1 - l, y1), (0, 255, 0), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (0, 255, 0), t)

        return img



def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = faceDetector()

    while True:
        success, img = cap.read()
        img, bboxes = detector.findFaces(img, draw=True)
        print(bboxes)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FrPS: {int(fps)}', (20, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()