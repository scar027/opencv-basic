import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

dir = r'../resources/faces/train'
test = r'../resources/faces/val/ben_afflek/5.jpg'

people = []
for i in os.listdir(dir):
    people.append(i)

features = np.load('features.npy', allow_pickle = True)
labels = np.load('labels.npy', allow_pickle = True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(test)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y + h, x:x + h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (50, 50), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness = 2)
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), thickness = 2)

cv.imshow('Detected Face', img)

cv.waitKey(0)