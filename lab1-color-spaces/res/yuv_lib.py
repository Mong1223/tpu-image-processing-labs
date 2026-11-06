
import cv2
import numpy as np


def make_lut_v():
    return np.array([[[i,255-i,0] for i in range(256)]], dtype=np.uint8)


def make_lut_u():
    return np.array([[[0,255-i,i] for i in range(256)]], dtype=np.uint8)


def YUV_sumq(a, b):
    res = np.empty_like(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] + b) >= 255.:
                res[i][j] = 255.
            elif (a[i][j] + b) <= 0.:
                res[i][j] = 0.
            else:
                res[i][j] = a[i][j] + b
    return res


def myround(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] >= 255.:
                a[i][j] = 255.
            elif a[i][j] <= 0.:
                a[i][j] = 0.
            else:
                a[i][j] = a[i][j]
    return a


def RGB2YUV(image):
    R,G,B = cv2.split(image)

    Y = R *.299000 + G * .587000 + B * .114000
    U = R * -.168736 + G * -.331264 + B * .500000 + 128
    V = R * .500000 + G * -.418688 + B * -.081312 + 128
    return Y, U, V

def YUV2RGB(Y,U,V):
    R = Y + 1.4075 * (V - 128)
    G = Y - 0.3455 * (U - 128) - (0.7169 * (V - 128))
    B = Y + 1.7790 * (U - 128)
    R = myround(R)
    G = myround(G)
    B = myround(B)
    return np.array(cv2.merge([R, G, B])).astype(np.uint8)


def getYUVsep(Y,U,V):
    lut_u, lut_v = make_lut_u(), make_lut_v()
    Y = np.array(Y).astype(np.uint8)
    U = np.array(U).astype(np.uint8)
    V = np.array(V).astype(np.uint8)
    Y = cv2.cvtColor(Y, cv2.COLOR_GRAY2RGB)
    U = cv2.cvtColor(U, cv2.COLOR_GRAY2RGB)
    V = cv2.cvtColor(V, cv2.COLOR_GRAY2RGB)
    u_mapped = cv2.LUT(U, lut_u)
    v_mapped = cv2.LUT(V, lut_v)
    return Y, u_mapped, v_mapped