import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
    #works for images, videos and live videos
    height = int (frame.shape[0] * scale)
    width = int (frame.shape[1] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    #works only for live video
    capture.set(3, width)
    capture.set(4, height)
    
img = cv.imread('../resources/photos/cats.jpg')
cv.imshow('cat', img)

resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)



capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    istrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()