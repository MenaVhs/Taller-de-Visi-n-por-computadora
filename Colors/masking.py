import cv2 as cv
import numpy as np

img = cv.imread('img/1.jpg')
cv.imshow('Img', img)

# Focus on faces
blank = np.zeros(img.shape[:2], dtype ='uint8')
# cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2 -25, img.shape[0]//2 - 15 ), 100, 255, -1)
#2
# mask = cv.rectangle(blank, (img.shape[1]//2 -25, img.shape[0]//2 - 15 ),(img.shape[1]//2 + 100, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

#3
####################
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (370, 370), 255, -1)
quarter_circle = cv.bitwise_and(circle, rectangle)
# cv.imshow('Half', quarter_circle)
#####################

masked = cv.bitwise_and(img, img, mask = quarter_circle) #3 mask = quarter_circle
# cv.imshow('masked', masked)

cv.waitKey(0)