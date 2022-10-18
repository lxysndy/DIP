import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('pollen-lowcontrast.tif', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = np.zeros(256, np.float) # 因为是概率, 有可能是浮点数

# 统计像素个数并计算概率
for i in range(height):
    for j in range(width):
        pixel = gray[i, j]
        index = int(pixel)
        count[index] = count[index] + 1

total = height * width # 总像素个数
count =  count / total  # 计算概率
# 计算累计概率
sum = float(0)
for i in range(256):
    sum += count[i]
    count[i] = sum # 计算出累积概率

# 计算映射表
mapl = np.uint16(255 * count)

# 将图像进行映射
for i in range(height):
    for j in range(width):
        pixel = gray[i, j]
        gray[i, j] = mapl[pixel]

plt.rcParams['font.sans-serif'] = ['SimHei']
titles = [u'原始图像', u'输出图像']
images = [img, gray]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()
# new_map = Image.fromarray(gray)
# img1 = new_map.convert('L').resize((256,256))
# img1.save("suanzi/test.tif") 图片已保存
plt.hist(gray.ravel(),256)
# #显示直方图
plt.show()
cv2.waitKey(0)



