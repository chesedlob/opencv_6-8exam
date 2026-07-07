import cv2 as cc
import numpy as np

def mycalcGrayHist(image):
    hist = np.zeros(256, dtype=np.int32)

    height, width = image.shape

    for y in range(height):
        for x in range(width):
            gray = image[y, x]
            hist[gray] += 1
    return hist

def drawGrayHistImage(hist):
  win_shape=(100, 256) 
  hist_img = np.full( win_shape, 255, np.uint8)
  cc.normalize(hist, hist, 0, win_shape[0], cc.NORM_MINMAX)
  gap = hist_img.shape[1]/hist.shape[0]
  for i, h in enumerate(hist.flatten()):
    x = int(round(i * gap))             
    w = int(round(gap))
    cc.rectangle(hist_img, (x, 0, w, int(h)), 0, cc.FILLED)
  return cc.flip(hist_img, 0)
image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)

hist = mycalcGrayHist(image)
hist_image = drawGrayHistImage(hist)
print(type(hist),hist.ndim,hist.shape,hist.dtype)
cc.imshow("image", image)
cc.imshow("hist_image", hist_image)
cc.waitKey(0)