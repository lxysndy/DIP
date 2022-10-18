#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : face_prepare.py
# @Author: WangYe
# @Date  : 2019/4/17
# @Software: PyCharm


import numpy as np
from PIL import Image
#图像转换为矩阵
matrix=np.asarray(Image.open('123.png'))
#矩阵转换为图像
image=Image.fromarray(matrix)
print(matrix)
image.show()
