import cv2 as cv

import numpy as np
from PIL import Image


face_cascade = cv.CascadeClassifier ( 'haarcascade_smile.xml' )
img = cv.imread('1.jpg', cv.IMREAD_UNCHANGED)

cv.imwrite('2.jpg' , img)


# show result
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()