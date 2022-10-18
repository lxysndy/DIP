import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取图像
image = cv2.imread('test.tif')
lena = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 灰度转化处理
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# roberts算子
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

# 转uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

# 加权和
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 图像显示
titles = [u'原始图像', u'Robertes图像']
images = [lena, Roberts]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()