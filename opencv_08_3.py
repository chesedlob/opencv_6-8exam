import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_COLOR)
height, width = image.shape[:2]

scale = 1
angle = -10



center = (width / 2, height / 2)



while True:
    key = cc.waitKey(1)
    a = float(input('회전할 각도를 입력해주세요 '))
    if key == ord('q'):
        break
    M = cc.getRotationMatrix2D(center,a,scale)
    trans_img = cc.warpAffine(image,M, (width,height),flags=cc.INTER_CUBIC)
    cc.imshow('transimg',trans_img)



cc.imshow('img', image)



cc.destroyAllWindows()
# 왜곡현상이 발생하는 이유 warpaffine이 실수값으로 작동하기 때문에 오차가 발생하고 회전을 해 이미지가 잘렸을 때 캔버스 사이즈가 조정되서 왜곡이 발생된다.
