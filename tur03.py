import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

start = (0, 0)
end = (img.shape[1], img.shape[0])
color = (0, 0, 255)
thicness = 2
cv2.line(img, start, end, color, thicness)
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), 2)
cv2.circle(img, (300, 400), 60, (255, 0, 0), 2)
cv2.putText(img, "hello", (100, 500), cv2.FONT_HERSHEY_COMPLEX, 2, (50, 50, 50), 1)

cv2.imshow('img', img)
cv2.waitKey(0)
