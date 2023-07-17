import cv2

#人脸识别

img = cv2.imread("./image/lenna.jpg")

#人脸识别不需要RGB，要灰阶图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#加载模型
faceCascade = cv2.CascadeClassifier("frontalface.xml")

#辨识人脸
#返回的是矩形的框
faceRect = faceCascade.detectMultiScale(gray, 1.1, 3) #第2个参数指图片缩放因子，第3个参数最小邻近数：越大越严谨,但是也不能太大

#打印出检测的数量
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)