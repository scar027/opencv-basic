import cv2 as cv

img = cv.imread('../resources/photos/cats.jpg')
cv.imshow('cats', img)

# averaging 
average = cv.blur(img, (3,3))
cv.imshow('average blur', average)

# gaussian blur(weighted average)
gauss = cv.GaussianBlur(img, (3,3), 0) # last parameter denotes the standard deviation in the x direction
cv.imshow('gaussian', gauss)

# median blur(more effective in removing noise)
median = cv.medianBlur(img, 3)
cv.imshow('median', median)
# median blur is generally not suitable for high kernel sizes like 5,7..

# bilateral blurring(retains edges in the image)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)