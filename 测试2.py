# from pathlib import Path
#
# import pandas as pd
# import plotly.graph_objects as go
# from matplotlib import pyplot as plt
# from plotly.offline import plot
#
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]})
#
# trace1 = go.Heatmap(x=df.columns, y=df.index, z=df.values)
# data = [trace1]
# layout = go.Layout()
# fig = go.Figure(data=data, layout=layout)
# plot(fig, filename=Path.cwd().joinpath('a.html').as_posix(), auto_open=True)

# import
#
# i = datetime.datetime.now()  # 获取当前时间
# print('今天是{}月{}日{}点{}分{}秒'.format(i.month, i.day, i.hour, i.minute, i.second))
import numpy as np

a = np.array([1,2,3,4,5])
print('{:.2f}'.format(a[0]))