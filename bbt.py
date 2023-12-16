import cv2 as cv
import matplotlib.pyplot as plt
from util import *
import os 
import time

# choose between SIFT/ORB

# for file in os.listdir(".//screenshots"): 
    # print(str(file))
    # img1 = cv.imread(".//screenshots//" + str(file), cv.IMREAD_UNCHANGED)
    # img2 = cv.imread('shop_ui.png') # target
    # sift = cv.SIFT_create(nfeatures=70000)
    # sift5 = cv.SIFT_create(nfeatures=500)
    # find_subimage_hard(img1, img2, sift, sift5, file)
    


    # # img3 = cv.drawMatches(img1,kp1,img2,kp2,matches,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    # # plt.imshow(img3)
    # # plt.show()
np.set_printoptions(threshold=sys.maxsize)
img1 = cv.imread("test0.png")
img2 = cv.imread('ui_0.png') # target
sift = cv.SIFT_create(nfeatures=70000)
sift5 = cv.SIFT_create(nfeatures=500)
foundim = find_subimage_hard(img1, img2, sift, sift5)

packCord0 = []
packCord1 = []
for i in range(7):
    packCord0.append([])
    packCord1.append([])
    for j in range(9):
        packCord0[i].append(None)
        packCord1[i].append(None)

foundim = foundim[35:545,5:-25,:]
cv.imwrite("foundim.png", foundim)


found = []
start = time.time()
fig, ax = plt.subplots()
method = eval('cv.TM_SQDIFF')#max method
toggle = True
ax.imshow(foundim)
for file in os.listdir(".//target_images"):
    t1 = time.time()
    template = cv.imread(".//target_images//" + str(file), cv.IMREAD_UNCHANGED)                              
    base = template[:,:,0:3]
    alpha = template[:,:,3]
    alpha = cv.merge([alpha, alpha, alpha])
    res = cv.matchTemplate(foundim,base,method,mask=alpha)
    templateWidth, templateHeight = template.shape[:2]
    
    print(res)
    
    res = np.array(res)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            pt = (i, j)
            if res[pt] > .7:
                t0 = time.time()
                targ = array_bfs_max(res, pt)[1]
                targ = (targ[1], targ[0])
                box = plt.Rectangle(targ, templateHeight, templateWidth, fill=False, color='white')
                ax.add_patch(box)
                ax.text(targ[1], targ[0], str(file))
                if(toggle):
                    toggle = False
                if(targ[0] > 490): #Right pack
                    if packCord1[int((targ[1]-5)/66)][int((targ[0]-555)/42)] is None:
                        packCord1[int((targ[1]-5)/66)][int((targ[0]-555)/42)] = str(file)
                else:#:Left pack
                    if packCord0[int((targ[1]-5)/66)][int(targ[0]/42)] is None:
                        packCord0[int((targ[1]-5)/66)][int(targ[0]/42)] = str(file)
                
                   # print("small " + str(time.time() - t0))
   # print("run " + str(time.time() - t1))
    
print("-------------")
print(time.time() - start)

print(packCord0)
print(packCord1)
        
plt.show()

    
    


    #print(target_matched_points)