# Resaltar color rojo con fondo gris
import cv2 as cv
import numpy as np
import imutils

# espacio de color en HSV (h=color, s=saturacion, v=iluminación)
rojoBajo1 = np.array([0, 50, 60], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 90], np.uint8)

img = cv.imread('Colors\girl.jpg')

# redimencionar img
img = imutils.resize(img, width=640)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#######
img_gray = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
#######
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# detectar rojo de la imgen (binearias)
maskRojo1 = cv.inRange(img_HSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv.inRange(img_HSV, rojoBajo2, rojoAlto2)

#unir imágenes
mask = cv.add(maskRojo1, maskRojo2)

# Mejorar contornos
mask = cv.medianBlur(mask, 7)

# Mezclar color rojo de original en mask
redDetected = cv.bitwise_and(img, img, mask=mask)

# fondo en escala de grises
invMask = cv.bitwise_not(mask)
bgGray = cv.bitwise_and(img_gray, img_gray, mask=invMask)

# Suma del fondo
#gray un canal y redDectected 3 canales
finalImg = cv.add(bgGray, redDetected)

# cv.imshow('Red orig', img)  
# cv.imshow('Mask', mask)
# cv.imshow('Red Detected', redDetected) 
# cv.imshow('invMask', invMask) 
# cv.imshow('bgGray', bgGray) 
cv.imshow('finalImg', finalImg) 
 
cv.waitKey(0)
cv.destroyAllWindows()