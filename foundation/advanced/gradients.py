import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian(computes the gradient of the grayscale image)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sabel(gradient in x and y directions)
sabelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sabely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sabel = cv.bitwise_or(sabelx, sabely)

cv.imshow('sabel x', sabelx)
cv.imshow('sabel y', sabely)
cv.imshow('combined sabel', combined_sabel)

# canny is a multi-stage process which uses sabel in one of its stages
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)