import cv2
import numpy as np

#轮廓检测
img = cv2.imread("./image/shape.jpg")
imgContour = img.copy()

#轮廓检测不需要RGB图片，转化为灰阶图片
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#边缘检测
canny = cv2.Canny(img, 150, 200)

#轮廓侦测
#轮廓点    阶乘                                需要侦测的轮廓类型  压不压缩
Contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in Contours:
    #用轮廓点画出轮廓
    #                               -1代表把所以轮廓点画出来 4代表轮廓粗度
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
    #取得不同轮廓的面积  可以用面积来过滤噪点
    area = cv2.contourArea(cnt)
    if area > 500:
        pass
    else:
        ##
        pass
    #取得不同轮廓的表总长度
    peri = cv2.arcLength(cnt, True) #如果是闭合的些True ，反之False
    #利用多边形近似轮廓来判断轮廓的形状
    vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
    #取得顶点数量
    corners = len(vertices)
    #用一个矩形把所有轮廓框起来
    x, y, w, h = cv2.boundingRect(vertices)
    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 4)
    if corners == 3:
        cv2.putText(imgContour, 'triangle', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 0, 255), 2)
    elif corners == 4:
        cv2.putText(imgContour, 'rectangle', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 0, 255), 2)
    elif corners == 5:
        cv2.putText(imgContour, 'pentagon', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 0, 255), 2)
    elif corners >= 6:
        cv2.putText(imgContour, 'circle', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1 , (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("canny", canny)
cv2.imshow("imgContour", imgContour)
cv2.waitKey(0)