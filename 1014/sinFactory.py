# 绘制 cos 与 sin 函数图像
# 载入 绘图pyplot模块，假定为 plt
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 5), dpi=80)  # 创建绘图图形对象figure，参数figsize决定尺寸，dpi为分辨率

X = np.linspace(-np.pi * 2, np.pi * 2, 256, endpoint=True)  # 创建等差一维数组
C = np.cos(X) / 2  # C == cos函数 y轴上的值
S = np.sin(X) / 2  # S == sin函数 y轴上的值

plt.plot(X, C, color='b', linewidth=2.0, linestyle="-.")  # plot方法绘点制图
plt.plot(X, S, color='g', linewidth=4.0, linestyle="--")  # X、Y轴数据是前面两个参数，后面的参数可以设置曲线各种属性
# linewidth 为 线宽    linestyle 为 指定线型

plt.xlabel("X")  # X轴标题名字
plt.ylabel("Y")
plt.xlim(-6.0, 6.0)  # 设置 x轴的上下限为6
plt.xticks(np.linspace(-7, 7, 15, endpoint=True))  # 设置x轴上标点距离，用等差方法
plt.ylim(-0.7, 0.7)
plt.yticks(np.linspace(-0.7, 0.7, 15, endpoint=True))

plt.savefig(r"C:\Users\666666\Desktop", dpi=72)  # 保存分辨率为72的图片
plt.show()
