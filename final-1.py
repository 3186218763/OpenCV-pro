import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #加载模型
        faceCascade = cv2.CascadeClassifier("frontalface.xml")

        #辨识人脸
        #返回的是矩形的框
        faceRect = faceCascade.detectMultiScale(gray, 1.15, 12) #第2个参数指图片缩放因子，第3个参数最小邻近数：越大越严谨,但是也不能太大

        #打印出检测的数量
        print(len(faceRect))

        for (x, y, w, h) in faceRect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        frame = cv2.resize(frame, (0, 0), fx=2, fy=2)
        cv2.imshow('video', frame)
    
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
