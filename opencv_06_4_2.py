import cv2 as cc
import numpy as np

cap = cc.imread('crayfish.jpg',cc.IMREAD_GRAYSCALE)

def calcGrayHist(image):
    images = [image]
    channels = [0]
    hsize = [256]
    ranges = [0,256]
    hist = cc.calcHist(images,channels,None,hsize,ranges)
    return hist
def drawGrayHistImage(hist):
    win_shape = (100,256)
    hist_img = np.full(win_shape,255,np.uint8)
    cc.normalize(hist, hist, 0, win_shape[0], cc.NORM_MINMAX)
    gap = hist_img.shape[1]/ hist.shape[0]

    for i ,h in enumerate(hist.flatten()):
        x = int(round(i * gap))
        w = int(round(gap))
        cc.line(hist_img,(x,0),(x,int(h)),0,1)
    return cc.flip(hist_img,0)

hist = calcGrayHist(cap)
hist_image = drawGrayHistImage(hist)

dst = cc.equalizeHist(cap)
hist2 = calcGrayHist(dst)
hist_image2 = drawGrayHistImage(hist2)
cc.imshow("image",cap)
cc.imshow("hist_image", hist_image)
cc.imshow("dst",dst)
cc.imshow("hist_image2", hist_image2)
cc.waitKey(0)
cc.destroyAllWindows()