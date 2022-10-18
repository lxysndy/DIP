## 自动补齐代码

## 获取图片&显示图片
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# 获取图片
def getimg():
    return Image.open("girl.jpg")


# 显示图片
def showimg(img):
    ## 加上
    plt.axis("off")
    plt.imshow(img)
    plt.show()


## plt.imshow()负责对图片进行处理、plt.show()负责对图片进行显示
im = getimg()
im_gray = im.convert('1')
## PIL的九种不同模式：1，L，P，RGB，RGBA，CMYK，YCbCr,I，F
## 其中L表示的是灰度的图像

showimg(im_gray)
# ## 但是7.2.0之后 不能直接点出来了
# Image.Image.save(im_gray,'pictures/1学习资料.jpg')
