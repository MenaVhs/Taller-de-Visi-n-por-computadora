from configparser import Interpolation
from re import I
from turtle import window_width
import cv2 as cv

img = cv.imread('img/fullHD.jpg')
cv.imshow('HD',img)

def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1] * scale)
    hight = int(frame.shape[0] * scale)
    dimensions = (width, hight)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

rescale_img = rescaleFrame(img)

capture = cv.VideoCapture('video/Loro.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video Loro', frame_resized)

    # Para video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Cuando se haya terminado el video
capture.realise()
cv.destroyAllWindows

# cv.imshow('rescale',rescale_img)
# cv.waitKey(0)