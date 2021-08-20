from cv2 import cv2

image=cv2.imread('Coco.jpg')
image_resize=cv2.resize(image,dsize=(1000,1000))
cv2.imshow('anh goc',image_resize)



gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_resize2=cv2.resize(gray_image,dsize=(1000,1000))
ret,thresh_gray=cv2.threshold(image_resize2,30,255,cv2.THRESH_BINARY)
th3 = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
# edit_image=cv2.resize(th3,dsize=(800,800))
cv2.imshow('anh nhi phan',th3 )
cv2.waitKey()
cv2.destroyAllWindows()