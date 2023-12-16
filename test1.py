import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

### TESTING TEMPLATE BASED MATCHES
img = cv.imread('full0.png', cv.IMREAD_GRAYSCALE)
img2 = img.copy()
img1 = img.copy()
template = cv.imread('levelNRoll.png', cv.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]


w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
#, 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED' 'cv.TM_CCOEFF'
#[cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]: the 
methods = ['cv.TM_CCOEFF_NORMED']
maxval = -1
overall_max_loc = None
iteration = -1
for meth in methods:
    method = eval(meth)
    for i in range(50):
        blur = cv.GaussianBlur(img1, (3,3), 0)
        template_blur = cv.GaussianBlur(template, (3,3), 0)

        
        res = cv.matchTemplate(blur ,template_blur,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)     
        
        if max_val > maxval:
            overall_max_loc = max_loc
            maxval = max_val            
            iteration = i
        
        img1 = cv.resize(img1, (0,0), fx=0.99, fy=0.99, interpolation = cv.INTER_NEAREST) 
        
        
    print(iteration)
    top_left = overall_max_loc
    print(iteration)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    plt.subplot(121), plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    
    img3 = cv.resize(img, (0,0), fx = (0.99)**(iteration), fy = (0.99)**(iteration), interpolation = cv.INTER_NEAREST) 
    cv.rectangle(img3,top_left, bottom_right, 255, 2)
    plt.subplot(122), plt.imshow(img3,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()