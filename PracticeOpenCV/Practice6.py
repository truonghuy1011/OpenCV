from cv2 import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('5851071030.jpg',0)
face=face_cascade.detectMultiScale(img,1.1,4)
cv2.imshow('face',face)
cv2.waitKey()
cv2.destroyAllWindows()