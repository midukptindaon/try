import mediapipe as mp
import cv2
import time


class face_mesh_detector():
    def __init__(self, static_mode=False,maxFaces=2,refine_landmarks=False,
        minDetectionCon=0.5,
        minTrackCon=0.5):
        self.static_mode = static_mode
        self.maxFaces = maxFaces
        self.refine_landmarks = refine_landmarks
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = mp.solutions.face_mesh.FaceMesh(self.static_mode,
                                                        self.maxFaces,
                                                        self.refine_landmarks,
                                                        self.minDetectionCon,
                                                        self.minTrackCon)


    def findFacesMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        self.drawSpec = self.mpDraw.DrawingSpec()
        if self.results.multi_face_landmarks:
            faces = [] #"faces list for number of faces through face loop value"
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms,
                                               self.mpFaceMesh.FACEMESH_CONTOURS,
                                          self.drawSpec)

                face = [] #"appending face list"
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    #print(id, x, y)
                    face.append([x, y])
                    "enumerate every landmarks"
                    # cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.5,
                    #             (0, 255, 0), 1)
                faces.append(face)

        return img, faces


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = face_mesh_detector()
    while True:
        success, img = cap.read()
        img, face = detector.findFacesMesh(img)
        if len(face) != 0:
            print(len(face))
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FrPS:{int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
