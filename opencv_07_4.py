import cv2 as cc
import numpy as np
import copy
image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)
title = 'TT'
def_image = copy.deepcopy(image) 
a = (0,0)
b = (0,0)
kernel = np.ones((5,5),np.float32) / 25

def onMouse(event,x,y,flags,param):
    global image,a,b
    if event == cc.EVENT_LBUTTONDOWN:
        a = (x,y)
    if event == cc.EVENT_LBUTTONUP:
        b= (x,y)
        roi = image[a[1]:b[1],a[0]:b[0]]
        roi = cc.filter2D(roi, -1,kernel)
        image[a[1]:b[1],a[0]:b[0]] = roi 
        cc.imshow(title,image)

cc.imshow(title,image)
cc.setMouseCallback(title,onMouse,image)
cc.waitKey(0)
cc.destroyAllWindows()
