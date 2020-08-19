import cv2
import numpy as np
import copy
import glob
#静态轮廓检测

img=cv2.imread('./photo/IMG_6719.JPG')
img=cv2.resize(img, (612, 816))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gb = cv2.GaussianBlur(img_gray, (5, 5), 0)
#边缘检测
edges = cv2.Canny(img_gb, 100 , 200)
cv2.imshow('edges',edges)
#寻找定位标记
#cv2.findContours返回第一个是轮廓检索模式，第二个是轮廓近似方法
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hierarchy = hierarchy[0]
found=[]
img_new=copy.deepcopy(img)

for i in range(len(contours)):
    k = i
    c = 0
    while hierarchy[k][2] != -1:
        k = hierarchy[k][2]
        c = c + 1
    if c >= 5:#嵌套层数大于等于5的取出来就可以
        found.append(i)



for i in found:
    rect = cv2.minAreaRect(contours[i])
    #获取每个定位矩形的4个边角点
    box = np.int0(cv2.boxPoints(rect))
    #画出4个点
    cv2.drawContours(img_new,[box],-1,(0,255,0),3)
    cv2.imshow('img', img_new)



cv2.waitKey(0)