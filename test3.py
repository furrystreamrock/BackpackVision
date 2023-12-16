import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('ixt.png',cv.IMREAD_GRAYSCALE) #target

sift5 = cv.SIFT_create(nfeatures=10)
kp, des = sift5.detectAndCompute(img,None)

img2 =cv.drawKeypoints(img,kp,img)
plt.imshow(img2)
plt.show()