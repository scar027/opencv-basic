import cv2 as cv
import numpy as np

# its the process of binarisation of an image

img = cv.imread('../resources/photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded image', thresh)

# inverse thresholded image
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('inverse thresholded image', thresh_inv)

# adaptive thresholding(automatically generate optimal threshold value)
# the third argument tells which automatic method to use
# the second last argument denotes the kernel size
# the last argument is the C value which we subtract from the mean to fine tune our threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive thresholding', adaptive_thresh)

cv.waitKey(0)