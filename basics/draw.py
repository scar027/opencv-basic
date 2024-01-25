import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8') #uint8 denotes the data type of an image
cv.imshow('blank', blank)

#painting a range of pixels of an image in a certain color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('green', blank)

#drawing a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = 2)
#use thickness=cv.filled to fill the rectangle completely with color
#or alternatively use thickness = -1 to achieve the same result.
cv.imshow("rectangle", blank)

#drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 80, (0, 0, 255), thickness = 3)
cv.imshow('circle', blank)

#drawing a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 3)
cv.imshow('line', blank)

#writing text
cv.putText(blank, 'Hello', (225,425), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)