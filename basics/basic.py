import cv2 as cv

img = cv.imread('../resources/photos/cat.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) 
# the second parameter denotes the kernel size and it must be an odd number
cv.imshow('blur', blur)


# edge cascade(used to detect edges)
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# dilating the image using a specific structural element
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('dilated', dilated)

# eroding dilated image to get back the structural element
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow('eroded', eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# interpolation=cv.INTER_AREA generally used while downscaling
# INTER_LINEAR or INTER_CUBIC(slowest but highest quality) typically used for upscaling
cv.imshow('resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)