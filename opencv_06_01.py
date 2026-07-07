import cv2 as cc
import numpy as np

title = 'titl'
image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)
def onChange(value):
    image2 = cc.add(image,value)
    cc.imshow(title,image2)
cc.imshow(title,image)

cc.createTrackbar("Value",title,0,100,onChange)
while True:
    if cc.waitKey(1000) == 27:
        break
cc.destroyAllWindows()
