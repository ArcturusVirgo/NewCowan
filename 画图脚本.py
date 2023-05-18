import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('21.00ns-Plasma_parameters.txt', sep='\s+', header=None, low_memory=False)
# df[0] = df[0].astype(int)
# df[1] = df[1].astype(int)
df = df[[0, 1, 6]].values

# 获取横坐标、纵坐标和值
x = df[:, 0].astype(int)
y = df[:, 1].astype(int)
z = df[:, 2]

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


plt.scatter(x, y, c=z, cmap='coolwarm')
plt.show()
