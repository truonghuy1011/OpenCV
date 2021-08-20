from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('nhuc.jpg',1)
min_mau=np.array([5,130,133])
max_mau=np.array([7,165,169])
mask=cv2.inRange(img1,max_mau,min_mau)
img2=cv2.imshow('anh',mask)
cv2.waitKey(0)