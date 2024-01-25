import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

'''
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)
'''

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # thresholdin tries to binarize an image
cv.imshow('thresh', thresh)
# if intensity of a pixel is less than 125 in the above case then
# it is set ot 0 and if it is above 255 then it is set to 1.

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_TREE is used to specify the mode in which the contours are to be found
# cv.RETR_TREE for all hierarchical contours
# cv.RETR_EXTERNAL for only external contours
# cv.RETR_LIST for all contours
# cv.CHAIN_APPROX_NONE is the argument used for the approximation method parameter
# cv.CHAIN_APPROX_NONE returns all of the contours
# cv.CHAIN_APPROX_SIMPLE returns all of the contours that are returned and 
# compresses them into simple ones that make more sense
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('contours drawn', blank)

cv.waitKey(0)