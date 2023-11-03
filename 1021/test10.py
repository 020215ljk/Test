from scipy import io
import matplotlib.pyplot as plt

# 加载MAT文件
mat_data = io.loadmat('../fileAll/Indian_pines.mat')

# 提取你感兴趣的通道的数据
channel_data = mat_data['a']

# 绘制数据
plt.plot(channel_data)
plt.xlabel('time')
plt.ylabel('channel_data')
plt.title('channel_data_imag')
plt.show()
