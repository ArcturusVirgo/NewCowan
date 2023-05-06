from modules import *

ph = Path('F:/Cowan/Al')
exp = ExpData(ph, Path('F:/Cowan/Al/EXP.txt'))
c4 = CalData(ph, exp, 'Ge_4')
c5 = CalData(ph, exp, 'Ge_5')
c6 = CalData(ph, exp, 'Ge_6')
c7 = CalData(ph, exp, 'Ge_7')
c8 = CalData(ph, exp, 'Ge_8')
c9 = CalData(ph, exp, 'Ge_9')
c10 = CalData(ph, exp, 'Ge_10')
c11 = CalData(ph, exp, 'Ge_11')
c12 = CalData(ph, exp, 'Ge_12')
c13 = CalData(ph, exp, 'Ge_13')
w4 = Widen(ph, exp, c4)
w5 = Widen(ph, exp, c5)
w6 = Widen(ph, exp, c6)
w7 = Widen(ph, exp, c7)
w8 = Widen(ph, exp, c8)
w9 = Widen(ph, exp, c9)
w10 = Widen(ph, exp, c10)
w11 = Widen(ph, exp, c11)
w12 = Widen(ph, exp, c12)
w13 = Widen(ph, exp, c13)

a = Atomic(32, 0)
sp = SpectraAdd(ph, a, exp, [w4, w5, w6, w7, w8, w9, w10, w11, w12, w13])


data = sp.get_add_data(24, 1.3e20)
print(data[1])

plt.plot(sp.result['wavelength'], sp.result['intensity'] / sp.result['intensity'].max())
plt.plot(sp.exp_data.data['wavelength'], sp.exp_data.data['intensity'] / sp.exp_data.data['intensity'].max())

plt.show()
