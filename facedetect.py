# import the opencv library
import cv2

#Load the Cascade Classifier File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

img = cv2.imread('boy.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 ,255), 2)
    roi_color = img[y:y+h, x:x+w]
    cv2.imwrite('face.jpg', roi_color)

cv2.imshow('img', img)

cv2.waitKey(0)