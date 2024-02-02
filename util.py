import numpy as np
import math
import cv2 as cv
import os
import sys
import matplotlib.pyplot as plt

def getHp(img, hps):
    # fig, ax = plt.subplots()
    # plt.imshow(img)
    img = img[945:975, 74:89]
    # box = plt.Rectangle((74,945),15 , 30, fill=False, color='white')
    # ax.add_patch(box)
    # plt.show()
    # cv.imwrite("fig1.png", img)
    min_score = np.inf
    SIndex = -1
    for i in range(5):
        hp =  hps[i]
        res = cv.matchTemplate(img, hp, cv.TM_SQDIFF)
        if res[0,0] < min_score:
            min_score = res[0,0]
            SIndex = i+1
    return SIndex
        
def bin_find_board(buffer, target):
    #binary search the first instance of a target. (Defined as either when the previous frame fails, or is the first)
    #presupposes that there is a frame containing a board   
    right = find_subimage_hard(buffer[int(len(buffer)/2)], target)    
    if len(buffer) == 1:
        return right[0]
    if right[1] == False:
        return bin_find_board(buffer[int(len(buffer)/2):], target)
    else:
        left = find_subimage_hard(buffer[int(len(buffer)/2)-1], target) 
        if left[1]:
            return bin_find_board(buffer[0:int(len(buffer)/2)], target)
        else:
            return right[0]
            
            
def is_invertible(a):
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]

def magnitude(vector): 
    return math.sqrt(sum(pow(element, 2) for element in vector))
    
def vect_dist(p1, p2):
    return magnitude((p1[0] - p2[0], p1[1] - p2[1]))
    
def majorityGroup(points, rad):
    #given a list of points, return only the points that are part of the majority group.
    #a group is defined as all points within a radius of a single point. Naive implementation n^3
    max_count = 0
    max_set = []
    for p1 in points:
        for p2 in points:
            if magnitude(((p1[0] - p2[0]),(p1[1] - p2[1]))):
               mid = ((p1[0] + p2[0])/2,  (p1[1] + p2[1])/2) 
               dist = magnitude((p1[0] - p2[0], p1[1] - p2[1]))  /2
               if dist < rad:
                    mag = math.sqrt(pow(rad, 2) - pow(dist, 2))
                    adj = (p1[0] - mid[0], p1[1] - mid[1])
                    dir1 = (adj[1], -adj[0])
                    dir2 = (-adj[1], adj[0])
                    dir1 = (dir1[0]/magnitude(dir1)*mag, dir1[1] / magnitude(dir1) * mag)
                    dir2 = (dir2[0]/magnitude(dir2)*mag, dir2[1] / magnitude(dir2) * mag)
                    r1 = (mid[0] + dir1[0], mid[1] + dir1[1])
                    r2 = (mid[0] + dir2[0], mid[1] + dir2[1])
                    
                    r1set = []
                    for p3 in points:
                        if magnitude((r1[0] - p3[0], r1[1] - p3[1])) <= rad:
                            r1set.append(p3)
                    if len(r1set) > max_count:
                           max_count = len(r1set)
                           max_set = r1set
                    r2set = []
                    for p3  in points:
                        if magnitude((r2[0] - p3[0], r2[1] - p3[1])) <= rad:
                            r2set.append(p3)
                    if len(r2set) > max_count:
                           max_count = len(r2set)
                           max_set = r2set
    if len(max_set) == 0:
        return [points[0]]
    return max_set


def array_bfs_max(arr, pt):
    #bfs's from a given point on condition:
    #arr must be numpy array
    
    if(pt[0] < 0 or pt[0] >= arr.shape[0] or pt[1] < 0 or pt[1] >= arr.shape[1]):
        return (-100, (0,0))
    if(arr[pt] < .7):
        return (-100, (0,0))
    #print("curr " + str(pt) + " val " + str(arr[pt]))
    vals = [(arr[pt], pt)]
    arr[pt] = 0
    vals.extend([array_bfs_max(arr, (pt[0]+1, pt[1])), array_bfs_max(arr, (pt[0]-1, pt[1])), array_bfs_max(arr, (pt[0], pt[1]+1)), array_bfs_max(arr, (pt[0], pt[1]-1))])
    return sorted(vals, key=lambda x: x[1],reverse=True)[0]
    
    
def find_subimage_hard(img1, img2):#uses expensive feature matching and fitting to find subimages that are scale invariant. 
    queryHeight, queryWidth = img1.shape[:2]
    trainHeight, trainWidth = img2.shape[:2]

    # #increase size and blur, manufacture more keypoints and rely on clusters for accuracy.
    # img1 = cv.resize(img1, (0,0), fx=2, fy=2)
    # img2 = cv.resize(img2, (0,0), fx=5, fy=5)

    # img1 = cv.GaussianBlur(img1, (3,3), sigmaX=.5, sigmaY=.5)
    # img2 = cv.GaussianBlur(img2, (3,3), sigmaX=.5, sigmaY=.5)

    sift = cv.SIFT_create(nfeatures=70000)
    sift5 = cv.SIFT_create(nfeatures=500)

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None) #the BIG BOI
    kp2, des2 = sift5.detectAndCompute(img2,None)
    bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    #only keep top quarter of matches
    matches = matches[0:int(len(matches)/4)]
    target_matched_points = [kp1[   x.queryIdx].pt for x in matches]

    topleft, bottomright = None, None

    #find the "true" points
    found = False
    for mt1 in matches:
        for mt2 in matches:
            q1 = kp1[mt1.queryIdx].pt
            q2 = kp1[mt2.queryIdx].pt
            t1 = kp2[mt1.trainIdx].pt
            t2 = kp2[mt2.trainIdx].pt
            if abs(q1[0] - q2[0]) > 100 and abs(q1[1] -q2[1]) > 100:
                thirdpoint = [x for x in matches if x is not mt1 and x is not mt2]
                #calculate topleft and bottomright points in query
                LRmat = np.array([  [1, t1[0]], [1, t2[0]]  ])
                if not is_invertible(LRmat):
                    break
                xtargets = np.array([q1[0], q2[0]])
                left, xScale = np.linalg.solve(LRmat, xtargets)
                right = left + xScale* trainWidth
                    
                UDmat = np.array([ [1, t1[1]],[1, t2[1]] ])
                if not is_invertible(UDmat):
                    break
                ytargets = np.array([q1[1], q2[1]])  
                top, yScale = np.linalg.solve(UDmat, ytargets)
                bottom = top + yScale * trainHeight
                topleft = (left, top)
                bottomright = (right, bottom)
                for mt3 in thirdpoint:  
                    #check if we have a near perfect match on third point. 
                    q3 = kp1[mt3.queryIdx].pt
                    t3 = kp2[mt3.trainIdx].pt
                    expected = (t3[0]*xScale + left, t3[1]*yScale + top)#the point we expect the matching to be if all three points are 'true'            
                    if vect_dist(expected, q3) <= .5:
                        fourthpoint = [x for x in matches if x is not mt1 and x is not mt2 and x is not mt3]    
                        for mt4 in fourthpoint:
                            q4 = kp1[mt4.queryIdx].pt
                            t4 = kp2[mt4.trainIdx].pt
                            expected4 = (t4[0]*xScale + left, t4[1]*yScale + top)
                            
                            if vect_dist(expected4, q4) <= .5:
                            
                            
                                                        
                                fifthpoint = [x for x in matches if x is not mt1 and x is not mt2 and x is not mt3 and x is not mt4]
                                for mt5 in fifthpoint:
                                    q5 = kp1[mt5.queryIdx].pt
                                    t5 = kp2[mt5.trainIdx].pt
                                    expected5 = (t5[0]*xScale + left, t5[1]*yScale + top)                                    
                                    if vect_dist(expected5, q5) <= .5:
                                
                                
                                
                                        if topleft[0] < 0 or topleft[1] < 0 or bottomright[0] > queryWidth or bottomright[1] > queryHeight or bottomright[1] < topleft[1] or bottomright[0] < topleft[0]:
                                            break
                                        # print(topleft)
                                        # print(bottomright)
                                        # print("Found im contained in dimensions: " + str(bottomright[1]-topleft[1]) + "," + str(bottomright[0] - topleft[0]) )
                                        foundim = img1[int(topleft[1]):int(bottomright[1]), int(topleft[0]) : int(bottomright[0])]
                                        foundim = cv.resize(foundim, (int(1000), int( 1000)), cv.INTER_NEAREST)
                                        return (foundim, True)
    return (None, False)
#pts = [(-1, -1), (0.5, 0.5), (0,0),(0,1),(1,0),(1,1),(3,3),( 2, 4),(4, 4)]

#print(majorityGroup(pts, 1))
#print(magnitude((1,1)))