#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : face_prepare.py
# @Author: WangYe
# @Date  : 2019/4/17
# @Software: PyCharm

from PIL import Image
import numpy as np


def readData():
    image_dir = r"./img/IMG_0286.JPG"

    x = Image.open(image_dir)  # 打开图片
    data = np.asarray(x)  # 转换为矩阵
    print(data.shape)  # 输出矩阵

    image = Image.fromarray(data)  # 将之前的矩阵转换为图片
    image.show()  # 调用本地软件显示图片，win10是叫照片的工具


readData()