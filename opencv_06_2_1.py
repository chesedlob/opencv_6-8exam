import numpy as np
import cv2 as cc

title = 'aa'
image = cc.imread('lenna.bmp', cc.IMREAD_GRAYSCALE)
cc.imshow(title,image)
print(f"lenna.bmp의 그레이스케일 픽셀값의 최대, 최소값{cc.minMaxLoc(image)}")
cc.waitKey(0)
dst = np.zeros(image.shape,image.dtype)
noimage = np.zeros(image.shape,image.dtype)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        tmp = 2 * int(image[i,j])
        if tmp > 255: 
            dst[i,j] = 255
        elif tmp < 0 : 
            dst[i,j] = 0
        else : 
            dst[i,j] = tmp
dst2 = cc.scaleAdd(image,2,noimage)
print(f"기본적인 명암비 조절 후 lenna.bmp의 그레이스케일 픽셀값의 최대, 최소값{cc.minMaxLoc(dst2)}")
cc.imshow(title,dst2)
cc.waitKey(0)
cc.destroyAllWindows()

alpha = 2
beta = -128*alpha  + 128
dst_ = np.zeros(image.shape,image.dtype)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        tmp = alpha*int(image[i,j]) + beta 
        if tmp > 255: dst[i,j] = 255
        elif tmp < 0:
            dst[i,j] = 0
        else:
            dst[i,j] = tmp
const = np.full(image.shape,beta,np.int32)
dst_2 = cc.scaleAdd(image.astype(np.int32),alpha,const)
dst_2 = dst_2.clip(0,255).astype(np.uint8)

print(f"효과적인 명암비 조절 후 lenna.bmp의 그레이스케일 픽셀값의 최대, 최소값{cc.minMaxLoc(dst_2)}")
cc.imshow(title,dst_2)
cc.waitKey(0)
cc.destroyAllWindows()
