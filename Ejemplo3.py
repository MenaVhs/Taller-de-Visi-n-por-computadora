import cv2 as cv
from ctypes import resize 

img = cv.imread('img\python.png')

cv.imshow('Orginal', img)

# Convertir a escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (0,0), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)