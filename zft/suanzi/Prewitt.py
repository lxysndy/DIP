import cv2
import numpy as np
import matplotlib.pyplot as plt

# 输入图像
image = cv2.imread('test.tif')
lena = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 灰度转化处理
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# kernel
kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelX)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernelY)

# 转uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

# 加权和
Prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 图象显示
plt.rcParams['font.sans-serif'] = ['SimHei']
titles = [u'原始图像', u'Prewitt图像']
images = [lena, Prewitt]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()