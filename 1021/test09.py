from scipy import io
import matplotlib.pyplot as plt

import scipy.io as scio

data = scio.loadmat('../fileAll/Indian_pines_corrected.mat')
print('data:\n', data)  # 大致看一下data的结构
print('datatype:\n', type(data))  # 看一下data的类型
print('keys:\n', data.keys)  # 查看data的键，这里验证一下是否需要加括号
print('keys:\n', data.keys())  # 当然也可以用data.values查看值
# print(data['EKG'])  # 查看数据集
# print('target shape\n', data['EKG'].shape)

# import scipy.io as sio
#
# # 加载mat文件
# mat_data = sio.loadmat('../fileAll/Indian_pines_gt.mat')
#
# # 获取键值
# keys = mat_data.keys()
#
# # 打印所有键
# for key in keys:
#     print(key)
