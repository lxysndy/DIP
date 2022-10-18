# coding=gbk
# ʵ�ֶ�ȡһ��TXT�ļ������ļ��е����ݴ����һ���б��У�
# �ٽ��б���ת��Ϊ����;���
# ������þ����е����ݣ�������ͼ�����ʽ���ֳ���

from PIL import Image
import numpy as np

# ��ȡ�����ļ����ļ���ʽΪtxt,���ļ��е�����ת����һ��list�б���
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
    # ������numpy���б��װΪ����
    array1 = np.array(list_result)
    # ��һ����array��װ�ɾ���
    data = np.matrix(array1)
    # ����reshapeһ������Ϊһ������
    data = np.reshape(data, (8, 8))
    #print(data)
    # ����Image��formarray��������������ת��Ϊͼ��PIL���͵�����
    new_map = Image.fromarray(data)
    img = new_map.convert('RGB').resize((256,256))
    img.save("test.png")
    # ��ʾͼ��
    img.show()

