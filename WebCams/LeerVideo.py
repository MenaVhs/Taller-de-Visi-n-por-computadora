import cv2 as cv

#Conect video
capture = cv.VideoCapture('WebCam.avi')

# Lecture 
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video WebCam', frame)

    if (cv.waitKey(30) & 0xFF == ord('s')):
        break

capture.realise()
cv.destroyAllWindows