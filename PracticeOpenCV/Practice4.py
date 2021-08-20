from cv2 import cv2
import imutils
image=cv2.imread('Coco.jpg')
imgresize=cv2.resize(image,dsize=(1000,1000))
#img_rotate=imutils.rotate(imgresize,90)
cv2.imshow('anh',img_rotate)
cv2.waitKey()
cv2.destroyAllWindows()
image2=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
imgresize2=cv2.resize(image2,dsize=(600,400))
#img_rotate2=imutils.rotate(imgresize2,90)
cv2.imshow('anh2',img_rotate2)
cv2.waitKey()
cv2.destroyAllWindows()