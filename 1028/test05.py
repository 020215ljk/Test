import pickle
import numpy as np
import matplotlib.pyplot as plt
from PIL.Image import Image
from PIL import Image


# 1. 从CIFAR-10数据文件中加载数据
def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data


# CIFAR-10数据集的文件前缀
data_dir = '../fileAll/data/'

# 2. 加载数据批次
batch_1 = unpickle(data_dir + 'data_batch_1')

# 3. 提取图像和标签
data = batch_1[b'data']
labels = batch_1[b'labels']

Xtr = data  # 训练集图像数据
Ytr = labels  # 训练集标签

Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)

print(type(Xtr_rows))

print(Xtr_rows)


# img = Image.fromarray(Xtr_rows.astype('uint8'))
#
# # 显示图像
# img.show()
