import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_GRAYSCALE)
title = "rasd"
va = 10
def onChange(value):
    global va
    if value == 0:
        va = 10
    elif value == 1:
        va = -10

def onMouse(event,x,y,flags,param):
    global va
    if event == cc.EVENT_LBUTTONDOWN:

        image2 = cc.add(image,va,dst=image)
        cc.imshow(title,image)
cc.imshow(title,image)
cc.createTrackbar("Value",title,0,1,onChange)
cc.setMouseCallback(title,onMouse,image)

cc.waitKey(0)
cc.destroyAllWindows()