import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('park', img)

b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

# showing each channel in its original color rather than grayscale
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue channel', blue)
cv.imshow('green channel', green)
cv.imshow('red channel', red)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# output represents intensity of that color in pixel concentrations
# lighter graysacle pixel indicates more pixel concentration
# darker grayscale pixel indicates less pixel concentration of that color

merged = cv.merge([b, g, r])
cv.imshow('merged image', merged)

cv.waitKey(0)