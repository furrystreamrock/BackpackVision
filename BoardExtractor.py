import cv2 as cv
import matplotlib.pyplot as plt
from util import *
import os 
import time
import mss
import sys

methods = ['screenshot', 'mp4']
method = methods[1]
sessionID = time.time() #use to mark a batch of pictures by date
hp1,hp2,hp3,hp4,hp5 = cv.imread("1hp.png"),cv.imread("2hp.png"),cv.imread("3hp.png"),cv.imread("4hp.png"),cv.imread("5hp.png")
hps = [hp1,hp2,hp3,hp4,hp5]
if method == methods[0]:
    mon = mss.mss().monitors[2]
    monitor = {"top": mon["top"], "left": mon["left"], "width": mon["width"], "height": mon["height"], "mon": 2}
if method == methods[1]:
    capture = cv.VideoCapture('raw.mp4')

buf_size = 10
total_count = 0
buffer= []
count = 0
shop = 0
board = 0
board_ui = cv.imread('ui_2.png') # target
shop_ui = cv.imread('shop_ui.png') # target
sift = cv.SIFT_create(nfeatures=700000)
sift5 = cv.SIFT_create(nfeatures=50000)
lastBoard = None
lastHp = 5
while(True):
    img = None
    if method == methods[0]:
        img  = mss.mss().grab(monitor)
        img = np.array(img)
        
    for i in range(20):
        capture.grab()
    img = capture.read()[1]
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)    
    if len(buffer) < buf_size:
        buffer.append(img)
        count += 1
    else:    
        if count < 10:
            buffer[count] = img
            count += 1
        if count == 10:
            #print("10")
            #sys.stdout.flush()
            count = 0
            val = find_subimage_hard(buffer[9], board_ui)
            
            if(val[1]):#We found a board
                print("board found")
                sys.stdout.flush()
                if board == 0 and shop == 1:
                    lastBoard = bin_find_board(buffer, board_ui)
                board = 1
                shop = 0
            else:
                val = find_subimage_hard(buffer[9], shop_ui)
                if val[1]: #Found a shop
                    print("shop found")
                    sys.stdout.flush()
                    currentHp = getHp(val[0], hps)
                    if  board == 1:
                        hpDiff = lastHp - currentHp
                        print("HP: " + str(currentHp))
                        print("hp Diff: " + str(hpDiff))
                        lastHp = currentHp
                        sys.stdout.flush()
                        if hpDiff == 1: #loss
                            cv.imwrite("./scrapeOut/" + str(sessionID) + "_" + str(total_count) + "_L.png", lastBoard)
                            total_count += 1
                        elif hpDiff == 0: #win
                            cv.imwrite("./scrapeOut/" + str(sessionID) + "_" + str(total_count) + "_W.png", lastBoard)
                            total_count += 1
                    board = 0
                    shop = 1 
                    
    if method == methods[0]:               
        time.sleep(0.25)