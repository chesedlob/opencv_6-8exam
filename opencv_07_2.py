import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_GRAYSCALE)

kernel = np.ones((7,7) , np.float32) / 49
blur = cc.filter2D(image, -1 ,kernel)
cc.imshow('blur',blur)

sharp = np.array([[-1,-1,-1,],[-1,9,-1],[-1,-1,-1]],dtype=np.float32)
shar = cc.filter2D(blur,-1,sharp)

sharp2 = np.array([[-1,-1,-1,],[-1,9,-1],[-1,-1,-1]],dtype=np.float32)
shar2 = cc.filter2D(image,-1,sharp2)

kernel2 = np.ones((7,7) , np.float32) / 49
blur2 = cc.filter2D(shar2, -1 ,kernel2)
cc.imshow('blur',blur)
cc.imshow('blu->sh',shar)
cc.imshow('sharp',shar2)
cc.imshow('sh->blu',blur2)
cc.waitKey(0)
cc.destroyAllWindows()