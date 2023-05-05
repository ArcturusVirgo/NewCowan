from modules import *


ph = Path('F:/Cowan/Al')
exp = ExpData(ph, Path('F:/Cowan/Al/exp_data.csv'))
c3 = CalData(ph, exp, 'Al_3')
c4 = CalData(ph, exp, 'Al_4')
c5 = CalData(ph, exp, 'Al_5')
c6 = CalData(ph, exp, 'Al_6')
w3 = Widen(ph, exp, c3)
w4 = Widen(ph, exp, c4)
w5 = Widen(ph, exp, c5)
w6 = Widen(ph, exp, c6)
a = Atomic(13, 0)
sp = SpectraAdd(ph, a, exp, [w3, w4, w5, w6])


data = sp.get_add_data(22.63, 6.95e19)

plt.plot(sp.result['wavelength'], sp.result['intensity'] / sp.result['intensity'].max())
plt.plot(sp.exp_data.data['wavelength'], sp.exp_data.data['intensity'] / sp.exp_data.data['intensity'].max())

plt.show()
