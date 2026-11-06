import cv2
import numpy as np
import res.yuv_lib as ryuv



image = cv2.imread('2.png')
cv2.imshow('image', image)

Y, U, V = ryuv.RGB2YUV(image)
cv2.imshow('Y1', np.array(V).astype(np.uint8))
print(np.min(V))
print(np.max(V))

V = ryuv.YUV_sumq(V, 100)

Y_image, U_image, V_image = ryuv.getYUVsep(Y,U,V)
result = np.hstack([Y_image, U_image, V_image])
cv2.imshow('YUV', result)

res = np.array(ryuv.YUV2RGB(Y, U, V)).astype(np.uint8)

cv2.imshow('res', res)


cv2.waitKey(0)


