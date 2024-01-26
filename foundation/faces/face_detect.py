import cv2 as cv

# img = cv.imread('../resources/photos/lady.jpg')
img = cv.imread('../resources/photos/group 2.jpg')
# cv.imshow('person', img)
cv.imshow('group of people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 6)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow('detected faces', img)

cv.waitKey(0)