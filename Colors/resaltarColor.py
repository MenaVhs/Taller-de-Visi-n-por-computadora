import cv2 as cv
import numpy as np
import imutils 

# HSV: h =  color, s = saturación, v = iluminación
rojoBajo1 = np.array([0, 60, 40], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 90], np.uint8)

img = cv.imread('girl.jpg')

# Redimencionar imagen
img = imutils.resize(img, width=640)

# Escala de grises
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Detectar rojo de la imagen 
maskRojo1 = cv.inRange(img_hsv, rojoBajo1, rojoAlto1)
maskRojo2 = cv.inRange(img_hsv, rojoBajo2, rojoAlto2)

# unir imagenes
mask = cv.add(maskRojo1, maskRojo2)
mask = cv.medianBlur(mask, 7)

# Mezclar color rojo de original en mask
redDetected = cv.bitwise_and(img, img, mask=mask)

# Fondo en escala de grises
invMask =cv.bitwise_not(mask)
bgGray = cv.bitwise_and(img_gray, img_gray, mask=invMask)

# Suma del fondo
# gray con el redDectected

finalImg = cv.add(bgGray, redDetected)

# cv.imshow('Img original', img)
# cv.imshow('Img Mask', mask)
# cv.imshow('Red Detected', redDetected)
# cv.imshow('InvMask', invMask)
# cv.imshow('Background', bgGray)
cv.imshow('Final', finalImg)
cv.waitKey(0)
cv.destroyAllWindows()