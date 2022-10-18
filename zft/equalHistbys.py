import cv2
import matplotlib.pyplot as plt

image = cv2.imread('pollen-lowcontrast.tif', 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized1 = cv2.equalizeHist(gray) #实现基本直方图均衡

# 应用CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized = clahe.apply(gray)

cv2.imshow("normal", equalized1)
cv2.imshow("bys", equalized)
cv2.waitKey(0)