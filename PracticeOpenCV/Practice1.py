from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
def click_event(event,x,y):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        st=str(x)+','+str(y)
        
        cv2.putText(img,st,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.imshow('img',img)
        

img=np.zeros((600,600,3),np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()