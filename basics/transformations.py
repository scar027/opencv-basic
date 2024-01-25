import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/cat.jpg')
cv.imshow('boston', img)

# translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# rotation
def rotate(img, angle, rotPoint = None ):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)  # returns rotated image

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('rotated_rotated', rotated_rotated)

# resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flipping
flip = cv.flip(img, 0)
# flip code 0 : vertical flip
# flip code 1 : horizontal flip
# flip code -1: both vertical and horizontal flip
cv.imshow('flip', flip)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)