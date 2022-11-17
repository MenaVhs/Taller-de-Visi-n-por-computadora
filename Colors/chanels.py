import cv2 as cv
import numpy as np

img = cv.imread('Img/fullHD.jpg')
cv.imshow('FullHD', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b, g, r = cv.split(img)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)


print(img.shape, b.shape, g.shape, r.shape)

merged = cv.merge([b, g, r])
# cv.imshow('Merge', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('blue', blue) # representa una alta distribución de azul
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)