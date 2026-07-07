import cv2 as cc
import numpy as np

src = cc.imread("scaling.jpg", cc.IMREAD_GRAYSCALE)

h, w = src.shape

scale = 1.5

new_h = int(h * scale)
new_w = int(w * scale)

dst = np.zeros((new_h, new_w), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        new_x = int(x * scale)
        new_y = int(y * scale)

        if 0 <= new_x < new_w and 0 <= new_y < new_h:
            dst[new_y, new_x] = src[y, x]

# 결과 출력
cc.imshow("image", src)
cc.imshow("dst", dst)

cc.waitKey(0)
cc.destroyAllWindows()