import numpy as np
import cv2 as cc


title = 'aa'
image = cc.imread('lenna.bmp', cc.IMREAD_GRAYSCALE)
alpha = 2
beta = -128*alpha  + 128
dst_ = np.zeros(image.shape,image.dtype)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        tmp = alpha*int(image[i,j]) + beta 
        if tmp >= 200: dst_[i,j] = 255
        elif tmp > 128 and tmp < 200:
            dst_ [i,j] = 128 + (127.0 / 72.0) * (tmp - 128)
        else:
            dst_[i,j] = 50 + (78.0 / 128.0) * tmp
const = np.full(image.shape,beta,np.int32)
dst_2 = cc.scaleAdd(image.astype(np.int32),alpha,const)
dst_2 = dst_2.clip(0,255).astype(np.uint8)

print(f"효과적인 명암비 조절 후 lenna.bmp의 그레이스케일 픽셀값의 최대, 최소값{cc.minMaxLoc(dst_2)}")
cc.imshow(title,dst_2)
cc.waitKey(0)
cc.destroyAllWindows()
