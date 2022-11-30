import cv2 as cv
import numpy as np

img = cv.imread('img/1.jpg')
cv.imshow('Img', img)

# Focus
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank img', blank)

# enmascaramiento
# mask = cv.circle(blank,(img.shape[1]//2 -25, img.shape[0]//2-15), 100, 255, -1)
# cv.imshow('Mask', mask)

######

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 +15), 100, 255, -1)
# circle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (370, 370), 255, -1)
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (370, 370), 255, -1)

new_mask = cv.bitwise_and(circle, rectangle)
cv.imshow('New mask', new_mask)

masked = cv.bitwise_and(img, img, mask=new_mask)
cv.imshow('Masked', masked)


cv.waitKey(0)