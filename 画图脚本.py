import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.loadtxt('21.00ns-Plasma_parameters.txt', usecols=(0, 1, 6))


# 生成横纵坐标的网格点
x = np.sort(np.unique(data[:, 0]))
x_num = len(x)
x_ = -x[::-1]
x_new = np.concatenate((x_, x))
y = np.sort(np.unique(data[:, 1]))
xx, yy = np.meshgrid(x_new, y)

# 将第三列数据作为网格点的值
z = np.zeros((len(y), 2*len(x)))
for i in range(data.shape[0]):
    ix = np.where(x == data[i, 0])[0][0]
    iy = np.where(y == data[i, 1])[0][0]
    z[iy, x_num + ix] = data[i, 2]
    z[iy, x_num - ix] = data[i, 2]


# 输出结果
plt.pcolormesh(xx, yy, z)
plt.show()









# plt.style.use('_mpl-gallery-nogrid')
# x = np.array([0.1, 2, 3, 4, 5])
# y = np.array([1, 2, 3, 4, 5])
# x, y = np.meshgrid(x, y)
# z = np.array([[1, 2, 3, 4, 5],
#               [11, 12, 13, 14, 15],
#               [11, 12, 13, 14, 15],
#               [11, 12, 13, 14, 15],
#               [11, 12, 13, 14, 15]])
# plt.pcolormesh(x, y, z)
# plt.colorbar()
# plt.show()

# df = pd.read_csv('21.00ns-Plasma_parameters.txt', sep='\s+', header=None, low_memory=False)
# # df[0] = df[0].astype(int)
# # df[1] = df[1].astype(int)
# df = df[[0, 1, 6]].values
#
# # 获取横坐标、纵坐标和值
# x = df[:, 0].astype(int)
# y = df[:, 1].astype(int)
# z = df[:, 2]

# # 设置网格大小和颜色映射
# grid_size = max(max(x), max(y)) + 1
# # cmap = plt.cm.get_cmap('coolwarm')
#
# # 创建网格和热力图对象，并绘制热力图
# grid = np.zeros((grid_size, grid_size))
# for i in range(len(x)):
#     grid[-(x[i] - 1)][y[i] - 1] = z[i]
# plt.imshow(grid)
#
# # 设置坐标轴标签和标题，并显示图像
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Heatmap')
# plt.show()

#
# plt.scatter(x, y, c=z, cmap='coolwarm')
# plt.show()
