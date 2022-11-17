import cv2 as cv

img = cv.imread('Img/fullHD.jpg')
cv.imshow('FullHD', img)

# Averaging, promedio de los pixeles que estén al rededor
average = cv.blur(img, (3,3))
# cv.imshow('Avarage Blur', average)

# Gaussian Blur, less blur but more nature the average
gauss = cv.GaussianBlur(img, (3,3), 0)
# cv.imshow('Gauss Blur', gauss)

# Median Blur, no se hace por promedio, sino por la media
median = cv.medianBlur(img, 3)
# cv.imshow('Median', median)

# Bilateral, most efective. Cómo lo hace es retiene los bordes de la imagen
bilateral = cv.bilateralFilter(img, d=15, sigmaColor=35, sigmaSpace=25)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)