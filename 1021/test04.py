# import numpy as np
# from numpy import array
# from scipy import io as spi
#
# a = np.ones((3, 3))
# spi.savemat('../fileAll/Indian_pines.mat', {'a': a})
# data = spi.loadmat('mat/file.mat')
# data['a']
# array([[1.,  1.,  1.],
#        [1.,  1.,  1.],
#        [1.,  1.,  1.]])


from scipy import io
import numpy as np

mydate = io.loadmat('arr.mat')

print(mydate)
