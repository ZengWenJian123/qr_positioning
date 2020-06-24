import cv2
import glob
import find_qr

images = glob.glob('./photo/*.jpg')  # 检索所有图像
for frame in images:
    img = cv2.imread(frame, 0)
    #图片由iPhone6拍摄，分辨率为2448*3264 现在缩小4倍
    img = cv2.resize(img, (612, 816))
    cv2.imshow('img',img)
    # 应用阈值从地毯背景中取出纸张和QR码和二值化
    blur=cv2.GaussianBlur(img,(3,3),0)
    ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 查找标记位置
    marker_x, marker_y, marker_z, align_marker=find_qr.find_mark(img)
    cv2.waitKey(100)

cv2.destroyAllWindows()

