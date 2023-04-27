import matplotlib.pyplot as plt
import pandas as pd

df3 = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/widen_Al_3.dat', sep='\s+', names=['x', 'y'])
df4 = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/widen_Al_4.dat', sep='\s+', names=['x', 'y'])
df5 = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/widen_Al_5.dat', sep='\s+', names=['x', 'y'])
df6 = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/widen_Al_6.dat', sep='\s+', names=['x', 'y'])
exp = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/Al_EXP.dat', sep='\s+', names=['x', 'y'])
a = [0.08, 0.51, 0.38, 0.3]
print(sum(a))

y = df3['y'] * a[0] + df4['y'] * a[1] + df5['y'] * a[2] + df6['y'] * a[3]
# plt.plot(df3['x'], df3['y'])
# plt.plot(df4['x'], df4['y'])
# plt.plot(df5['x'], df5['y'])
# plt.plot(df6['x'], df6['y'])
y = y - y.min()
y = y / y.max()
plt.plot(df6['x'], y)
plt.plot(exp['x'], exp['y'] / exp['y'].max())
plt.show()
