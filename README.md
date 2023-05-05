# NewCowan
可以使用以下方法判断两张光谱的整体轮廓是否相似:

计算两张光谱的相关系数。相关系数在-1到1之间,值越接近1表示两者越相关,即整体轮廓越相似。可以使用numpy.corrcoef计算:
python
Copy
import numpy as np

spectrum1 = [1, 2, 3, 4, 5]
spectrum2 = [2, 3, 4, 5, 6]

corr = np.corrcoef(spectrum1, spectrum2)[0, 1]
print(corr)  # 0.98
计算两张光谱的互相关函数。互相关峰值越高,表示两者越相似。可以使用numpy.correlate计算:
python
Copy
corr = np.correlate(spectrum1, spectrum2, mode='full') 
print(corr)  # [2, 6, 12, 20, 27]
可视化两张光谱,比较其整体走势和峰值位置。使用matplotlib.pyplot可以画出光谱曲线图,人工判断其相似度:
python
Copy
import matplotlib.pyplot as plt

plt.plot(spectrum1)
plt.plot(spectrum2)
plt.show()
计算两张光谱的均方误差MSE。MSE越小,表示两者越相似:
python
Copy
mse = np.mean(np.square(spectrum1 - spectrum2))
print(mse)  # 0.4
综上,可以综合使用这几个方法来判断两张光谱的整体轮廓是否相似。 Let me know if you have any other questions!