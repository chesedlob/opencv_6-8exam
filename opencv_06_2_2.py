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
        if tmp > 255: dst_[i,j] = 255
        elif tmp < 0:
            dst_ [i,j] = 0
        else:
            dst_[i,j] = tmp
const = np.full(image.shape,beta,np.int32)
dst_2 = cc.scaleAdd(image.astype(np.int32),alpha,const)
dst_2 = dst_2.clip(0,255).astype(np.uint8)

print(f"효과적인 명암비 조절 후 lenna.bmp의 그레이스케일 픽셀값의 최대, 최소값{cc.minMaxLoc(dst_2)}")
cc.imshow(title,dst_2)
cc.waitKey(0)
cc.destroyAllWindows()

#알파값이 높아지면 어두운곳은 더욱 어두워지고 밝은 곳은 더욱 밝아진다
# 알파값이 낮아지면 전체 이미지가 살짝 어두워져 회색빛이 강해진다

 