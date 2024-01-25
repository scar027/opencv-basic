import cv2 as cv

img = cv.imread('../resources/photos/cat.jpg')
cv.imshow('cat', img)

cv.waitKey(0)

'''
capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    istrue, frame = capture.read()
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

'''
