import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cv2.imshow('frame', frame)
       
    
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
