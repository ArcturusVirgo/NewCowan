import numpy as np
import matplotlib.pyplot as plt

# 生成模拟光谱数据和实验光谱数据
x = np.arange(0, 10, 0.01)
sim_spectrum = np.sin(x) + np.random.normal(0, 0.1, size=len(x))
exp_spectrum = np.cos(x) + np.random.normal(0, 0.1, size=len(x))

# 计算模拟光谱数据和实验光谱数据的相关性
corr_coef = np.corrcoef(sim_spectrum, exp_spectrum)[0, 1]

# 绘制模拟光谱数据和实验光谱数据的图像
plt.plot(x, sim_spectrum, label='Simulated spectrum')
plt.plot(x, exp_spectrum, label='Experimental spectrum')
plt.legend()
plt.show()

print('Correlation coefficient:', corr_coef)
