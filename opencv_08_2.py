import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_COLOR)
height, width = image.shape[:2]

scale = 2
angle = -45 


cc.imshow('img', image)
new_wid ,new_hei = width *2 , height * 2
center = (width / 2, height / 2)
M = cc.getRotationMatrix2D(center,angle,scale)
M[0,2] += width /2
M[1,2] += height / 2 
trans_img = cc.warpAffine(image,M, (new_wid,new_hei))





cc.imshow('transimg',trans_img)

cc.waitKey(0)
cc.destroyAllWindows()