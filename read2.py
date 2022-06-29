import cv2 as cv
import numpy as np

blank = np.ones((500, 500, 3), dtype='uint8')

cv.imshow('blank', blank)
img = cv.imread("Photos/cats.jpg")
cv.imshow("Cat", img)

#1. Paint the image a certain colour
blank[200:300, 300:400] = 0,0, 255
print(blank)
# cv.imshow("Green", blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow("Circle",blank)
cv.waitKey(0)








