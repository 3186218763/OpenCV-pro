import cv2
import numpy as np
import random

img = cv2.imread("./image/colorcolor.jpg")
print(img.shape)
newimg = img[0:150, 0:200]

cv2.imshow('img', img)
cv2.imshow("newimg", newimg)
cv2.waitKey(0)
