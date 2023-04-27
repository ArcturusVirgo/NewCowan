from pprint import pprint

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#
# exp = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/Al_EXP.dat', sep='\s+', names=['x', 'y'])
# df = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/result-0.2558-1.dat', sep='\s+', names=['x', 'y'])
# exp['y'] = exp['y'] / exp['y'].max()
# df['y'] = df['y'] / df['y'].max()
# print(np.sqrt(np.power(exp['y'] - df['y'], 2).sum() / exp.shape[0]))
#
# plt.plot(df['x'], df['y'] / df['y'].max())
# # plt.plot(exp['x'], exp['y'] / exp['y'].max())
# plt.show()


abu = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/Al_data.dat', sep='\s+', names=['T', 'N', '3','4', '5', '6'])
plt.plot(abu['T'], abu['3'])
plt.plot(abu['T'], abu['4'])
plt.plot(abu['T'], abu['5'])
plt.plot(abu['T'], abu['6'])
plt.show()
