import cv2 as cv
import matplotlib.pyplot as plt
from util import *
import os 
import time

#load in all point_images:
point_images = {}
# for file in os.listdir(".//ContrastPoints//Raw"):
    # point_images[file[0:-4]] = cv.imread(".//ContrastPoints//Raw//" + str(file), cv.IMREAD_UNCHANGED)
    
alpha_count = {"BookOfLight_0.png": 4159,"BookOfLight_1.png": 4126,"BookOfLight_2.png": 4165,"BookOfLight_3.png": 4121,"PiercingArrow_0.png": 1542,"PiercingArrow_1.png": 1522,"PiercingArrow_2.png": 1543,"PiercingArrow_3.png": 1499}
img1 = cv.imread("test9.png")
img2 = cv.imread('ui_0.png') # target
sift = cv.SIFT_create(nfeatures=70000)
sift5 = cv.SIFT_create(nfeatures=500)
foundim = find_subimage_hard(img1, img2, sift, sift5)

cv.imwrite("foundim.png", foundim)
boardWidth, boardHeight = foundim.shape[:2]
plt.imshow(foundim)
plt.show()


file = "BookOfLight_1.png"
template = cv.imread(".//target_images//FilledRaw//" + file , cv.IMREAD_UNCHANGED)  
base = template[:,:,0:3]
alpha = template[:,:,3]
alpha = cv.merge([alpha, alpha, alpha])
res = cv.matchTemplate(foundim,base,method=cv.TM_SQDIFF,mask=alpha)
templateWidth, templateHeight = template.shape[:2]
res = np.array(res)
res /= alpha_count[file]
b,c = np.where(res < 4000)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
print(min_val)
top_left = min_loc
bottom_right = (top_left[0] + templateHeight, top_left[1] + templateWidth)
cv.rectangle(foundim,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(foundim,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()