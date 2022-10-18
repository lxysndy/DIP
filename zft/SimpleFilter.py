
import numpy as np
import matplotlib.pyplot as plt

## 图像
img = np.array([[0, 1, 1],
                [2, 4, 0],
                [4, 2, 1]])


## 核
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) / 9

## 图像上下左右补0
img = np.insert(img, 0, values=np.array([0, 0, 0]), axis=1)
img = np.insert(img, 4, values=np.array([0, 0, 0]), axis=1)
img = np.insert(img, 0, values=np.array([0, 0, 0, 0, 0]), axis=0)
img = np.insert(img, 4, values=np.array([0, 0, 0, 0, 0]), axis=0)
box = np.zeros((3,3))
## 滤波操作
for i in range(1,4):
    for j in range(1,4):
        box[i-1][j-1] = np.sum(img[i-1:i+2,j-1:j+2] * kernel)

print("滤波结果：")
print(box)
print("四舍五入之后：")
print(np.around(box))
