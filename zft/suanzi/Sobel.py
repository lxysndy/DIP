import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('test.tif')
lean = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 转灰度图像
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel算子
x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)  # 对x一阶求导
y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)  # 对y一阶求导
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 图像输出
plt.rcParams['font.sans-serif'] = ['SimHei']
titles = [u'原始图像', u'Sobel图像']
images = [lean, Sobel]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()