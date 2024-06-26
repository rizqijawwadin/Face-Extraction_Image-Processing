import cv2
import numpy as np

image = cv2.imread('C:/Users/Yeeeee/Desktop/Aberdeen/paul14.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Hsv", hsv_image)

lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)
skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
cv2.imshow("Thesh", skin_mask)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skin_mask = cv2.erode(skin_mask, kernel, iterations=2)
cv2.imshow("Erode", skin_mask)

skin_mask = cv2.dilate(skin_mask, kernel, iterations=2)
cv2.imshow("Dilate", skin_mask)

skin_mask = cv2.GaussianBlur(skin_mask, (5, 5), 0)
cv2.imshow("Blur", skin_mask)

skin = cv2.bitwise_and(image, image, mask=skin_mask)
cv2.imshow("mask", skin_mask)
cv2.imshow("Skin", skin)
cv2.waitKey(0)
