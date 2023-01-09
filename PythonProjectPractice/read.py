import cv2 as cv2
import numpy as np

i = False

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


# reading videos

captures = cv2.VideoCapture("C:\\Users\\Miduk\\Dropbox\\My PC (DESKTOP-9C1N9SJ)\\"
                            "Pictures\\Camera Roll\\WIN_20210822_23_19_23_Pro.mp4")
while i is True:
    isTrue, frame = captures.read()
    cv2.imshow("video", frame)

    if cv2.waitKey(3000) & 0xFF == ord("s"):  # press s button to break
        break

captures.release()
cv2.destroyAllWindows()

# reading images

if i is True:
    cv2.namedWindow("miduk", cv2.WINDOW_NORMAL)
    img1 = cv2.imread("C:\\Users\\Miduk\\Downloads\\wallpaper2\\IMG-20211113-WA0036.jpg")
    im = cv2.resize(img1, (200, 300))
    cv2.imshow("miduk", im)
    cv2.waitKey(3000)  # waitkey(1) is 1 millisecond
else:
    i = False

# point the image to certain colour

while i is True:
    blank = np.zeros((400, 400, 3), dtype='uint8') # (width, height, number of colour of channel
    blank[:] = 240, 255, 20
    cv2.imshow('colour', blank)

    if cv2.waitKey(3000) & 0xFF == ord("s"):
        break

    blank1 = np.zeros((400, 400, 3), dtype='uint8')
    blank1[150:250, 250:350] = 240, 255, 20
    cv2.imshow("colour", blank1)

    if cv2.waitKey(3000) & 0xFF == ord("s"):
        break

# draw a rectangle

while i is True:
    blank2 = np.zeros((400, 400, 3), dtype='uint8')
    cv2.rectangle(blank2, (125, 125), (250, 250), (0, 255, 0), thickness=2)
    cv2.imshow("rectangle", blank2)

    if cv2.waitKey(3000) & 0xFF == ord("s"):
        break

# greying the image


def resizedframe(greyed_image):
    scale = 50
    fh = int(greyed_image.shape[0] * scale / 100)  # shape 0 is height
    fw = int(greyed_image.shape[1] * scale / 100)   # shape 1 is width
    dimension1 = (fh, fw)
    return cv2.resize(greyed_image, dimension1, interpolation=cv2.INTER_AREA)

while i is True:
    grayresized = cv2.cvtColor(resizedframe(cv2.imread("C:\\Users\\Miduk\\"
    "Downloads\\wallpaper2\\IMG-20211113-WA0036.jpg")),
    cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayresized, (7, 7), cv2.BORDER_DEFAULT)
    canny = cv2.Canny(grayresized, 125, 175)
    cv2.imshow("canny", canny)
    if cv2.waitKey(3000) & 0xFF == ord("s"):
        break

while i is False:
    img3 = rescaleFrame(cv2.imread("C:\\Users\\Miduk\\"
        "Downloads\\wallpaper2\\IMG-20211113-WA0036.jpg"))
    def translate(img, x, y):
        transMat = np.float32([[1, 0, x], [0, 1, y]])
        dimensions = (img.shape[1], img.shape[0])
        return cv2.warpAffine(img, transMat, dimensions)
    translated = translate(img3, 50, 50)
    cv2.imshow("translated", translated)

    if cv2.waitKey(3000) & 0xFF == ord("s"):
        break




