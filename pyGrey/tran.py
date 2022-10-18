# coding=gbk
# 实现读取一个TXT文件，将文件中的数据存放在一个列表中，
# 再将列表逐渐转换为数组和矩阵
# 最后利用矩阵中的数据，将其以图像的形式呈现出来

from PIL import Image
import numpy as np

# 读取本地文件，文件格式为txt,将文件中的数据转存在一个list列表中
def readfile(filename):
    with open(filename, 'r') as f:
        list1 = []
        for line in f.readlines():
            line_str = line.strip()
            for element in line_str:
                if element != " ":
                    list1.append(int(element))
    return list1

if __name__ == '__main__':
    list_result = readfile("target_matrix.txt")
    for i in range(0, len(list_result)):
        if list_result[i] == 1:
            list_result[i] = 255
        else:
            list_result[i] = 0
    # 再利用numpy将列表包装为数组
    array1 = np.array(list_result)
    # 进一步将array包装成矩阵
    data = np.matrix(array1)
    # 重新reshape一个矩阵为一个方阵
    data = np.reshape(data, (8, 8))
    #print(data)
    # 调用Image的formarray方法将矩阵数据转换为图像PIL类型的数据
    new_map = Image.fromarray(data)
    img = new_map.convert('RGB').resize((256,256))
    img.save("test.png")
    # 显示图像
    img.show()

