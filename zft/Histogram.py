#!/usr/bin/env python
# coding=utf-8
import cv2
import matplotlib.pyplot as plt
#读图
img = cv2.imread("pollen-lowcontrast.tif")
#转换成灰度图
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#获取直方图，由于灰度图img2是二维数组，需转换成一维数组
plt.hist(img2.ravel(),256)
#显示直方图A
plt.show()
cv2.waitKey(0)