import numpy as np
from cv2 import cv2
img=cv2.imread('do.jpg',1)
# print(img.shape)
print(img[:,:,])
# cv2.line(img,(0,0),(400,300),(0,255,0),5)
# cv2.rectangle(img,(300,300),(500,300),(0,255,0),10)
# cv2.circle(img,(450,150),20,(255,9,0))
# cv2.putText(img,'Mona Lisa',(20,500),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),10,lineType=cv2.LINE_AA)
cv2.imshow('dep',img)
cv2.waitKey()
cv2.destroyAllWindows()