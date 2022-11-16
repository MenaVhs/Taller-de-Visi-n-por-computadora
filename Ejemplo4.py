import cv2 as cv
import numpy as np

# Imagen en vacío
blank = np.zeros((500, 500, 3), dtype= 'uint8')
# cv.imshow('Blank', blank)

# 1. Pintar toda imagen 
# orden de los colores es en BGR
blank[:] = 226, 43, 138
#cv.imshow('Color', blank)

# 2. Dibujar un rectángulo
# rectangle = cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,0,234), thickness= cv.FILLED)
cv.rectangle(blank, (500,500), (300,300),(0,0,234), thickness= cv.FILLED)

# 3. Círculo
cv.circle(blank, (55,250), 50, (255,0,0), thickness = 10) 

# 4. Línea
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,244,234), thickness=40)

# 5. Escribir un texto en la imagen
cv.putText(blank, "Hola a todos",  (230,200), cv.FONT_ITALIC, 2.0, (0,0,0), thickness= 2)
cv.imshow('Middle Rectangle', blank)

cv.waitKey(0)