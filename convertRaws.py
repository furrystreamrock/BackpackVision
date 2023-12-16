import cv2 as cv
from util import *
import os

for file in os.listdir(".//RRaw"):
    img0 = cv.imread(".//RRaw//" + str(file), cv.IMREAD_UNCHANGED)
    img1 = cv.rotate(img0, cv.ROTATE_90_CLOCKWISE)
    img2 = cv.rotate(img0, cv.ROTATE_180)
    img3 = cv.rotate(img0, cv.ROTATE_90_COUNTERCLOCKWISE)
    xScale = 1000/1624 
    yScale = 1000/914 
    img0 = cv.resize(img0, (int(img0.shape[1]*xScale), int(img0.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img1 = cv.resize(img1, (int(img1.shape[1]*xScale), int(img1.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img2 = cv.resize(img2, (int(img2.shape[1]*xScale), int(img2.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img3 = cv.resize(img3, (int(img3.shape[1]*xScale), int(img3.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "0.png", img0)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "1.png", img1)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "2.png", img2)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "3.png", img3)
    
    
for file in os.listdir(".//RRaw2"):
    img0 = cv.imread(".//RRaw2//" + str(file), cv.IMREAD_UNCHANGED)
    img1 = cv.rotate(img0, cv.ROTATE_90_CLOCKWISE)
    img2 = cv.rotate(img0, cv.ROTATE_180)
    img3 = cv.rotate(img0, cv.ROTATE_90_COUNTERCLOCKWISE)
    xScale = 1000/1808  
    yScale = 1000/1017 
    img0 = cv.resize(img0, (int(img0.shape[1]*xScale), int(img0.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img1 = cv.resize(img1, (int(img1.shape[1]*xScale), int(img1.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img2 = cv.resize(img2, (int(img2.shape[1]*xScale), int(img2.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    img3 = cv.resize(img3, (int(img3.shape[1]*xScale), int(img3.shape[0]*yScale)), interpolation= cv.INTER_AREA)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "0.png", img0)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "1.png", img1)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "2.png", img2)
    cv.imwrite(".//target_images// " + str(file[0:-4]) + "3.png", img3)