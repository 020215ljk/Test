
from PIL import Image
from scipy import io
import numpy as np

# image = Image.open('./img/0002.png')
#
# imageArr = np.array(image)
#
# arr = np.array(imageArr)
#
# io.savemat('./mat/Img_arr02.mat', {"vec": arr})

# 导入
mydata = io.loadmat('../fileAll/Indian_pines_corrected.mat')

print(mydata)
