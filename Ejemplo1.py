import cv2 as cv 
import numpy as np 

# print("Versión OpenCV: ", cv.__version__)
# Readinf images
img = cv.imread('img/1.jpg')

# cv.imshow('Imagen 1', img) # mostrat la imagen
# cv.waitKey(0) # cerrar imagen con cualquier tecla

video = cv.VideoCapture('video\Loro.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Cuando haya terminado el video
video.realise()
cv.destroyAllWindows