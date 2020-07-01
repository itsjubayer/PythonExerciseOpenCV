import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#print(img)
#img[:]=0,255,0

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0,0), (250, 250), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (450, 50), 30, (255, 255, 0), 5)
cv2.putText(img, "PYTHON OPENCV", (200, 350), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 124, 50), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)