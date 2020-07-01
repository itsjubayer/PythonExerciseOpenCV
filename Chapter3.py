import cv2

img = cv2.imread("Resources/car.jpg")
print(img.shape)

imResize = cv2.resize(img,(1000, 500)) #width, height
print(imResize.shape)

imgCropped = img[0:200, 200:500] #hight, width

cv2.imshow("Original Image", img)
#cv2.imshow("Resized Image", imResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
