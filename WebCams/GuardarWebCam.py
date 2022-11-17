import cv2 as cv 

# Connecting to a webcam

capture = cv.VideoCapture(0)

salida = cv.VideoWriter('Rata.avi', cv.VideoWriter_fourcc(*'XVID'), 15, (640, 480))

# Lectura de frames
while (capture.isOpened()):
    ret, frame = capture.read()
    salida.write(frame)
    cv.imshow('WebCam', frame)

    if(cv.waitKey(1) == ord('s')):
        break

salida.release()
capture.release()
cv.destroyAllWindows
