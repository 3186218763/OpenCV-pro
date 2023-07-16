import cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)
re_kernel = np.ones((10, 10), np.uint8)

img = cv2.imread("./image/colorcolor.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #把RGB图片转为灰阶图片
blur = cv2.GaussianBlur(img, (3,3), 0) #把图片高斯模糊化，可以有效去除噪点
canny = cv2.Canny(img, 200, 250) #对边缘进行检测，可以得到轮廓图
dilate = cv2.dilate(canny, kernel, iterations=1) #膨胀：把线条变粗，可用于处理轮廓图
erode = cv2.erode(canny, re_kernel, iterations=1) #侵蚀：把线条变细


cv2.imshow('img', img)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("canny", canny)
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)
cv2.waitKey(0)