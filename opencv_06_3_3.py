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
def mydrawGrayHistImage(hist):
    win_shape = (100, 256)
    hist_img = np.full(win_shape, 255, np.uint8)
    hist = hist.astype(np.float32)
    cc.normalize(hist, hist, 0, win_shape[0]-1, cc.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]
    prev = None
    for i, h in enumerate(hist.flatten()):
        x = int(round(i * gap))
        y = win_shape[0] - 1 - int(h)   # flip을 안 쓸 경우
        if prev is not None:
            cc.line(hist_img, prev, (x, y), 0, 1)
        prev = (x, y)
    return hist_img
image = cc.imread('lenna.bmp',cc.IMREAD_GRAYSCALE)

hist = mycalcGrayHist(image)
hist_image = mydrawGrayHistImage(hist)

print(type(hist),hist.ndim,hist.shape,hist.dtype)
cc.imshow("image", image)
cc.imshow("hist_image", hist_image)
cc.waitKey(0)