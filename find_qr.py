import cv2
import numpy as np
"""
用于从QR码图像识别标记的实用程序功能
假设QR码的方向是这样，其中X，Y，Z是位置标记，
A是对齐标记
X----------Y
------------
------------
------------
---------A--
Z-----------
"""


def find_mark(img):
    # 检测图像中的轮廓
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    found = []
    # 寻找定位标记
    for i in range(len(contours)):
        k = i
        c = 0
        while hierarchy[k][2] != 1:
            k = hierarchy[k][2]
            c=c+1
        if c>=5:#嵌套层数大于等于5的取出来就可以
            found.append(i)
    for i in found:
        rect=cv2.minAreaRect(contours[i])
        # 获取每个定位矩形的4个边角点
        box = np.int0(cv2.boxPoints(rect))
        # 画出4个点
        cv2.drawContours(img, [box], -1, (0, 255, 0), 3)

    return int(1)