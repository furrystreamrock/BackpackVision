import cv2 as cv
from util import *
import os

for file in os.listdir(".//target_images//youtube//"):
    img0 = cv.imread(".//target_images//youtube//" + str(file), cv.IMREAD_UNCHANGED)
    img1 = cv.rotate(img0, cv.ROTATE_90_CLOCKWISE)
    img2 = cv.rotate(img0, cv.ROTATE_180)
    img3 = cv.rotate(img0, cv.ROTATE_90_COUNTERCLOCKWISE)
    xScale = (1000/1896.33) #*1.04
    yScale = (1000/1069) #*1.05
    img0 = cv.resize(img0, (int(img0.shape[1]*xScale), int(img0.shape[0]*yScale)), interpolation= cv.INTER_NEAREST )
    img1 = cv.resize(img1, (int(img1.shape[1]*xScale), int(img1.shape[0]*yScale)), interpolation= cv.INTER_NEAREST )
    img2 = cv.resize(img2, (int(img2.shape[1]*xScale), int(img2.shape[0]*yScale)), interpolation= cv.INTER_NEAREST )
    img3 = cv.resize(img3, (int(img3.shape[1]*xScale), int(img3.shape[0]*yScale)), interpolation= cv.INTER_NEAREST )
    a = [img0, img1, img2, img3]
    # for geh in a:
        # geh = cv.GaussianBlur(geh, (9,9), 6)
        # geh2 = geh.copy()
        # geh[:,:,0:3] = cv.bilateralFilter(geh2[:,:,0:3], 5, 175,7)
        # for y in range(geh.shape[0]):
            # for x in range(geh.shape[1]):
                # geh[y,x,0] = int(0.9*geh[y,x,0])
                # geh[y,x,1] = int(0.8*geh[y,x,1])
                # geh[y,x,2] = int(0.8*geh[y,x,2])
        
    cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "_0.png", img0)
    cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "_1.png", img1)
    cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "_2.png", img2)
    cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "_3.png", img3)
    
    
# for file in os.listdir(".//target_images//TrimFillRaw2//"):
    # img0 = cv.imread(".//target_images//TrimFillRaw2//" + str(file), cv.IMREAD_UNCHANGED)
    # img1 = cv.rotate(img0, cv.ROTATE_90_CLOCKWISE)
    # img2 = cv.rotate(img0, cv.ROTATE_180)
    # img3 = cv.rotate(img0, cv.ROTATE_90_COUNTERCLOCKWISE)
    # xScale = (1000/1896.33) #*1.04
    # yScale = (1000/1069) #*1.05
    # img0 = cv.resize(img0, (int(img0.shape[1]*xScale), int(img0.shape[0]*yScale)), interpolation= cv.INTER_LANCZOS4)
    # img1 = cv.resize(img1, (int(img1.shape[1]*xScale), int(img1.shape[0]*yScale)), interpolation= cv.INTER_LANCZOS4 )
    # img2 = cv.resize(img2, (int(img2.shape[1]*xScale), int(img2.shape[0]*yScale)), interpolation= cv.INTER_LANCZOS4 )
    # img3 = cv.resize(img3, (int(img3.shape[1]*xScale), int(img3.shape[0]*yScale)), interpolation= cv.INTER_LANCZOS4 )
    # a = [img0, img1, img2, img3]
    # # for geh in a:
        # # geh = cv.GaussianBlur(geh, (9,9), 6)
        # # geh2 = geh.copy()
        # # geh[:,:,0:3] = cv.bilateralFilter(geh2[:,:,0:3], 5, 175,7)
        # # for y in range(geh.shape[0]):
            # # for x in range(geh.shape[1]):
                # # geh[y,x,0] = int(0.9*geh[y,x,0])
                # # geh[y,x,1] = int(0.8*geh[y,x,1])
                # # geh[y,x,2] = int(0.8*geh[y,x,2])
    # cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "0.png", img0)
    # cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "1.png", img1)
    # cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "2.png", img2)
    # cv.imwrite(".//target_images//FilledRaw//" + str(file[0:-4]) + "3.png", img3)