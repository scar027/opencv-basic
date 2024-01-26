import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('park', img)

# plt.imshow(img)
# plt.show()


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# graysacle image cant be convverted to hsv directly
# if we want to convert graysacale to hsv then we must first convert 
# grayscale to bgr and then bgr to hsv

# HSV to BGR 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv --> bgr', hsv_bgr)

# L*A*B to BGR 
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab --> bgr', lab_bgr)


cv.waitKey(0)