import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Img/fullHD.jpg')
# cv.imshow('FullHD', img)


# un sistema que representa un arreglo de colores de pixel
# BGR to Grayscale (1 chanel)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
# print(gray.shape)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

########## Aquí la imagen se muestra en RGB
plt.imshow(img)
plt.show()
##########

# BGR a RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# sólo se puede convertir hacia BGR, no se puede hacer directo 

cv.waitKey(0)