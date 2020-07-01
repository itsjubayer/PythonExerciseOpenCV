import cv2
import numpy np

img = cv2.imread("Resources/lena.jpg")
kernel = np.Ones((5,5), np.uint8)

#Convert to GRAY
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Convert to Blur
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
#Canny Edge Detector
imgCanny = cv2.Canny(img, 150, 200)
#image Dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)



cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.waitKey(0)