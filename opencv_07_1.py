import cv2 as cc 
import numpy as np

image = cc.imread('lenna.bmp', cc.IMREAD_GRAYSCALE)

mean = 0
sigma = 20

noise = np.random.normal(mean,sigma,image.shape)
noisy = image.astype(np.float32) + noise
noisy = np.clip(noisy,0,255).astype(np.uint8)
kernel = np.ones((9,9), np.float32) / 81
blur1 = cc.filter2D(noisy, -1 ,kernel)

cc.imshow("img",image)
cc.imshow('noise',noisy)
cc.imshow('blur',blur1)
cc.waitKey(0)
cc.destroyAllWindows()