from PIL import Image
import numpy as np

# 创建一个RGB图像数组
arr = np.array([[[0, 0, 0], [255, 255, 255], [0, 255, 0]], [[255, 0, 0], [0, 0, 255], [255, 255, 255]]])

# 将数组转换为图像
img = Image.fromarray(arr.astype('uint8'))

# 显示图像
img.show()