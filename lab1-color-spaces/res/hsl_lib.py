import numpy as np
import cv2

def HSL_sumq(a, b):
    res = np.empty_like(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] + b) >= 1.:
                res[i][j] = 1.
            elif (a[i][j] + b) <= 0.:
                res[i][j] = 0.
            else:
                res[i][j] = a[i][j] + b
    return res


def HSL_sumH(a, b):
    res = np.empty_like(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] + b) >= 360:
                res[i][j] = 360
            elif (a[i][j] + b) <= 0.:
                res[i][j] = 0.
            else:
                res[i][j] = a[i][j] + b
    return res

def myround(a):
    if a >= 255.:
        a = 255.
    elif a <= 0.:
        a = 0.
    else:
        a = a
    return a

def rgb_hsl(image):
    res = []
    for i in range(image.shape[0]):
        buf = []
        for j in range(image.shape[1]):
            r, g, b = image[i][j][0], image[i][j][1], image[i][j][2]
            r = r / 255
            g = g / 255
            b = b / 255
            h2, l, s, h = rgb_to_hsl(r, g, b)
            buf.append([h2, l, s, h])
        res.append(buf)
    return res

def rgb_to_hsl(r,g,b):
    MAX = max(r, g, b)
    MIN = min(r, g, b)
    l = (MAX+MIN)/2.
    if MAX == MIN:
        return 0.0, l, 0.0, 0.0
    if l <= 0.5:
        s = (MAX - MIN)/(2.*l)
    else:
        s = (MAX - MIN)/(2.-2.*l)

    #HUE
    if MAX == r and g >= b:
        h = (g - b) / (MAX - MIN)*60
        h2 = (g - b) / (MAX - MIN)
    elif MAX == r and g < b:
        h = (g - b) / (MAX - MIN)*60 + 360.
        h2 = (g - b) / (MAX - MIN)
    elif MAX == g:
        h = (b-r)/(MAX-MIN)*60 +120.
        h2 = (b-r)/(MAX-MIN)
    else: #MAX == b:
        h = (r-g)/(MAX-MIN) *60 +240.
        h2 = (r-g)/(MAX-MIN)
    return h2, l, s, h


def hsl_rgb(image):
    res = []
    for i in range(image.shape[0]):
        buf = []
        for j in range(image.shape[1]):
            h = image[i][j][0]
            l = image[i][j][1]
            s = image[i][j][2]
            r, g, b = hls_to_rgb(h, l, s)
            r = r*255
            g = g*255
            b = b*255
            # print(r,g,b)
            buf.append([r, g, b])
        res.append(buf)
    return res

def hls_to_rgb(h, l, s):
    if s == 0.0:
        return l, l, l
    if l <= 0.5:
        m2 = l * (1.0+s)
    else:
        m2 = l+s-(l*s)
    m1 = 2.0*l - m2
    h = h / 360.
    hr = h + 1. / 3.
    hb = h - 1. / 3.
    h = check(h)
    hr = check(hr)
    hb = check(hb)

    return (myround(_v(m1, m2, hr)), myround(_v(m1, m2, h)), myround(_v(m1, m2, hb)))

def check(h):
    if h < 0.:
        h = h+1.
    if h > 1.:
        h = h-1.
    return h

def _v(m1, m2, hue):
    hue = hue % 1.
    # print(hue)
    if hue < 1./6.:
        return m1 + (m2-m1)*hue*6
    if hue < 0.5:
        return m2
    if hue < 2./3.:
        return m1 + (m2-m1)*(2./3.-hue)*6
    return m1

def getHSLpic(h,l,s):
    hs_pic = np.array(h).astype(np.uint8)
    ls_pic = np.array(l*255).astype(np.uint8)
    ss_pic = np.array(s*255).astype(np.uint8)

    hs_pic = cv2.cvtColor(hs_pic, cv2.COLOR_GRAY2RGB)
    ls_pic = cv2.cvtColor(ls_pic, cv2.COLOR_GRAY2RGB)
    ss_pic = cv2.cvtColor(ss_pic, cv2.COLOR_GRAY2RGB)
    return hs_pic, ls_pic, ss_pic