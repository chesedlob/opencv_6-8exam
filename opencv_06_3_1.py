import cv2 as cc
import numpy as np

image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)
ls = []
count = 0

for i in range(256):
    ls.append(0)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        count += 1
        ls[image[i,j]] += 1
print(f"영상의 전체 픽셀수 : {count}")
mi,ma,mi_lo,ma_lo = cc.minMaxLoc(image)
print(f"영상에서 픽셀값의 최소값:{mi}")
print(f"영상에서 픽셀값의 최대값:{ma}")
print(f"빈도수가 가장 많은 픽셀값과 빈도수: {max(ls)} , {ls.index(max(ls))} ")
print(f"픽셀값 80의 빈도수 : {ls[81]}")