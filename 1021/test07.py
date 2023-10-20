import numpy as np
from PIL import Image

# image = Image.open('./img/0002.png')
#
# imageArr = np.array(image)
#
# print(imageArr)

# array_str = np.array2string(imageArr, separator=',', threshold = np.inf)
# print(array_str)


# 将数组转换为numpy数组
arr = np.array([[[255, 255, 255],
                 [251, 251, 251],
                 [225, 218, 219],
                 [249, 249, 249],
                 [255, 255, 255]],

                [[255, 255, 255],
                 [233, 230, 231],
                 [190, 163, 177],
                 [229, 225, 227],
                 [248, 247, 247]],

                [[247, 247, 247],
                 [221, 219, 228],
                 [197, 186, 223],
                 [200, 195, 203],
                 [208, 199, 203]],

                [[233, 232, 231],
                 [208, 205, 211],
                 [167, 159, 184],
                 [194, 193, 197],
                 [255, 255, 255]],

                [[247, 246, 246],
                 [209, 207, 208],
                 [187, 183, 189],
                 [232, 231, 233],
                 [255, 255, 255]]])

# 将numpy数组转换为图像
img = Image.fromarray(arr.astype('uint8'))

# 显示图像
img.show()

img.save('./img/0003.png')
