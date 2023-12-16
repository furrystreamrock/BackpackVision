import cv2 as cv
import matplotlib.pyplot as plt
from util import *

img1 = cv.imread('5s10.png') # queryImage
img2 = cv.imread('s10ui.png') # trainImage
garen1 = cv.imread('garen1.png', cv.IMREAD_UNCHANGED)
garen1_base = garen1[:,:,0:3]
garen1_alpha = garen1[:,:,3]
garen1_alpha = cv.merge([garen1_alpha, garen1_alpha, garen1_alpha])

