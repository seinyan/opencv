import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


cv2.imshow('img',ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
