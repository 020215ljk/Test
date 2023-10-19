from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ])

# 导出
io.savemat('arr.mat', {"vec": arr})

# 导入
mydata = io.loadmat('../fileAll/Indian_pines_corrected.mat')




print(mydata)
