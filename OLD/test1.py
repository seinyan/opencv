import cv2 as cv

import numpy as np
from PIL import Image


face_cascade = cv.CascadeClassifier ( 'haarcascade_smile.xml' )
img = cv.imread ( '1.jpg' )
gray = cv.cvtColor (img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 2)

    font = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (x,y)
    fontScale = 1
    fontColor = (123, 0, 0)
    lineType = 2

    cv.putText(img, 'EYE',
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()


# void cv::putText	(	InputOutputArray 	img,
# const String & 	text,
# Point 	org,
# int 	fontFace,
# double 	fontScale,
# Scalar 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# bool 	bottomLeftOrigin = false
# )


# cv.putText(img, "qq", x, y, (0, 255, 0), 2)

# void cv::rectangle	(	InputOutputArray 	img,
# Point 	pt1,
# Point 	pt2,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0
# )

# image = cv.imread("1.jpg")
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# gray = cv.GaussianBlur(gray, (3, 3), 0)
# cv.imwrite("gray.jpg", gray)
#
# edged = cv2.Canny(gray, 10, 250)
# cv.imwrite("edged.jpg", edged)
#
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
# closed = cv.morphologyEx(edged, cv.MORPH_CLOSE, kernel)
# cv.imwrite("closed.jpg", closed)

