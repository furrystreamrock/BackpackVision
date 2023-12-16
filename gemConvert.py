import cv2 as cv
from util import *
import os

for file in os.listdir(".//raysPNGS//gems"):
    gemImg = cv.imread(".//raysPNGS//gems//" + str(file), cv.IMREAD_UNCHANGED)
    img1 = cv.rotate(gemImg, cv.ROTATE_90_CLOCKWISE)
    img2 = cv.rotate(gemImg, cv.ROTATE_180)
    img3 = cv.rotate(gemImg, cv.ROTATE_90_COUNTERCLOCKWISE)
    xScale = 1000/1713
    yScale = 1000/964
    gemImg = cv.resize(gemImg, (int(gemImg.shape[1]*xScale/2.17), int(gemImg.shape[0]*yScale/2.17)), interpolation= cv.INTER_AREA)
    img1 = cv.resize(img1, (int(img1.shape[1]*xScale/2.17), int(img1.shape[0]*yScale/2.17)), interpolation= cv.INTER_AREA)
    img2 = cv.resize(img2, (int(img2.shape[1]*xScale/2.17), int(img2.shape[0]*yScale/2.17)), interpolation= cv.INTER_AREA)
    img3 = cv.resize(img3, (int(img3.shape[1]*xScale/2.17), int(img3.shape[0]*yScale/2.17)), interpolation= cv.INTER_AREA)
    cv.imwrite(".//gems// " + str(file[0:-4]) + "0.png", gemImg)
    cv.imwrite(".//gems// " + str(file[0:-4]) + "1.png", img1)
    cv.imwrite(".//gems// " + str(file[0:-4]) + "2.png", img2)
    cv.imwrite(".//gems// " + str(file[0:-4]) + "3.png", img3)