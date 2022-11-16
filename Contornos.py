import cv2 as cv
img = cv.imread('img/rata3.jpg')

#cv.imshow('Original', img)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#Canny 
canny = cv.Canny(gray, 100, 150)
cv.imshow('canny', canny)

contours, hierarcies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found')

cv.waitKey(0)