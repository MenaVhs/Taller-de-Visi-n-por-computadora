import cv2 as cv
import  numpy as np

#img = cv.imread('img\python.png')
img = cv.imread('Img/python.png', -1)

# cv.imshow('Python', img)

def translate(img, x, y):
    height = img.shape[0]
    width = img.shape[1]

    transMat = np.float32([[1, 0, x], [0, 1, y]])
    channels = img.shape[2]
    dimensions = (width, height) 
    shifted = cv.warpAffine(img, transMat, dimensions)

    print("Image dimension:  ", dimensions)
    print("Image Height:   ", height)
    print("Image width", width)
    print("Number of channels:   ", channels)

    return shifted

translate = translate(img, -50, 50)
cv.imshow('Translated', translate)

# -x --> Left
# x --> Right
# -y --> Upwards
# y --> Downwards

# Rotation
def rotate(img, angle, rotPoint = None):
    print("entro")
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale = 1.0)
    dimensions = (height, width)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
rotated2 = rotate(rotated, 35)

cv.imshow('Rotation',rotated)
cv.imshow('Rotation2',rotated2)
cv.waitKey(0)