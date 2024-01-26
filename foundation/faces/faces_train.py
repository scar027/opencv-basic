import os
import cv2 as cv
import numpy as np

dir = r'../resources/faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []
for i in os.listdir(dir):
    people.append(i)

features = []
labels = []

def create_train():
    # changing directory to the directory of the person
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)
        
        # looping through the images in the persons directory
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            # converting to grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
            
            # cropping to only the face of the person from the image
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y: y + h, x:x + w] # roi: region of interest
                # appending the features of the person from that image to the features list
                features.append(faces_roi)
                labels.append(label) 
            
create_train()
print('training done------------------')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

# print(f'length of the features = {len(features)}')
# print(f'length of the features = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create() # instantiating the face recognizer

# training the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)