import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[111, 219], [320, 200], [154, 482], [352, 440]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output Image", imgOut)
cv2.imshow("Image", img)
cv2.waitKey(0)