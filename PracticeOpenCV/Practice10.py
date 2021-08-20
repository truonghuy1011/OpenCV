from cv2 import cv2
import datetime
cap=cv2.VideoCapture(0)

# cap.set(3,3000)
# cap.set(4,3000)
# print(cap.get(3))
# print(cap.get(4))
# fourcc=cv2.VideoWriter_fourcc(*'FUCK')
# out=cv2.VideoWriter('truonghuy.mp4',fourcc,20.0,(640,480))
# print(cap.isOpened())
while (True):
     ret,frame=cap.read()
     if (ret==True):
      #  out.write(frame)
      #  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #  print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #  print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
       dateti=str(datetime.datetime.now())
       frame=cv2.putText(frame,dateti,(10,40),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),2)
       
       cv2.imshow('camera',frame)
       if cv2.waitKey(1) & 0xFF==ord('q'):
         break
     else:
         break
cap.release()
# out.release()
cv2.destroyAllWindows()