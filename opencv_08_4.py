import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_COLOR)
height, width = image.shape[:2]

scale = 1
angle = -10



center = (width / 2, height / 2)



while True:
    key = cc.waitKey(0)
    if key == ord('q'):
        break
    elif key == ord('r'):
        angle += 10
    elif key == ord('b'):
        angle += -10
    M = cc.getRotationMatrix2D(center,angle,scale)
    trans_img = cc.warpAffine(image,M, (width,height),flags=cc.INTER_CUBIC)
    cc.imshow('transimg',trans_img)



cc.imshow('img', image)



cc.destroyAllWindows()