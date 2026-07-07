
import cv2 as cc
import numpy as np

image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)

embos = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype = np.float32)

sharp = cc.filter2D(image,-1,embos,delta=128)

cc.imshow('image',image)
cc.imshow('sharp',sharp)
cc.waitKey(0)
cc.destroyAllWindows()


# 위 마스크는 평탄한 부분은 회색으로 만들고 외곽신 부분은 완전히 하얀색이거나 검은색으로 만든다.

