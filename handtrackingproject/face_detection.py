import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetect = mpFaceDetection.FaceDetection(0.75)

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetect.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            #mpDraw.draw_detection(img, detection)
            #print(id, detection)
            # print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            "BoundingBoxClass"
            bboxC = detection.location_data.relative_bounding_box
            "imageheight, imagewidth, imagechannel"
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin*iw), int(bboxC.ymin*ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(img, bbox, (0, 255, 0), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                        (bbox[0], bbox[1]-10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    #print(bboxC)




    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # print(bbox[0], bbox[1])
    cv2.putText(img, f'FrPS: {int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
