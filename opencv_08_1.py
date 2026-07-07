import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_COLOR)
height, width = image.shape[:2]

sx = 0.5
sy = 0.5

tx = 50
ty = 50
# Mi = np.array([[sx,0,0],[0,sy,0]],np.float32)
# trans_img=  cc.warpAffine(image,Mi,(width, height))
tx = (width - width * sx) / 2
ty = (height - height * sy) / 2

M = np.array([
    [sx, 0, tx],
    [0, sy, ty]
], dtype=np.float32)
trans_img = cc.warpAffine(image,M, (width,height))

cc.imshow('img', image)
cc.imshow('transimg',trans_img)
cc.waitKey(0)
cc.destroyAllWindows()