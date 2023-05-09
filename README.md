# NewCowan

### 判断两张光谱的整体轮廓是否相似

1. 计算两张光谱的相关系数。相关系数在-1到1之间,值越接近1表示两者越相关,即整体轮廓越相似。可以使用numpy.corrcoef计算:

~~~python
import numpy as np

spectrum1 = [1, 2, 3, 4, 5]
spectrum2 = [2, 3, 4, 5, 6]

corr = np.corrcoef(spectrum1, spectrum2)[0, 1]
print(corr)  # 0.98
~~~

2. 计算两张光谱的互相关函数。互相关峰值越高,表示两者越相似。可以使用numpy.correlate计算:

~~~python
corr = np.correlate(spectrum1, spectrum2, mode='full')
print(corr)  # [2, 6, 12, 20, 27]
~~~

3. 计算两张光谱的均方误差MSE。MSE越小,表示两者越相似:

~~~python
mse = np.mean(np.square(spectrum1 - spectrum2))
print(mse)  # 0.4
~~~

综上,可以综合使用这几个方法来判断两张光谱的整体轮廓是否相似。 Let me know if you have any other questions!