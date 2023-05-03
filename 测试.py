import matplotlib.pyplot as plt
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from modules import *

# in36 = In36()
# in2 = In2()
# recorder = Recorder(Path('F:/Cowan/Al'))
# in36.read_from_file(Path('F:/Cowan/Al/in36'))
# in2.read_from_file(Path('F:/Cowan/Al/in2'))
ph = Path('F:/Cowan/Al')
# r = Run(ph, 'Al_4', in36, in2, recorder)
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

if __name__ == '__main__':
    import time

    start = time.time()

    Te_num = 100
    Ne_num = 100
    Te = np.linspace(20, 50, Te_num)
    # Ne = np.linspace(1e21, 2.3e22, step)
    # Ne = np.array([1e17, 1e18, 1e19, 1e20, 1e21, 1e22, 1e23])
    temp = np.linspace(1, 10, Ne_num // 6).tolist()
    Ne = []
    for i in range(17, 23):
        Ne += list(map(lambda x: x * 10 ** i, temp))
    print(Ne)

    res = []
    # 多进程 ---------------------------------------------
    pool = ProcessPoolExecutor(os.cpu_count() - 1)

    tasks_out = []
    for n in Ne:
        tasks_in = []
        for t in Te:
            temp_task = pool.submit(sp.get_add_data, t, n)
            tasks_in.append(temp_task)
        tasks_out.append(tasks_in)

    pool.shutdown()

    for tasks in tasks_out:
        temp = []
        for task in tasks:
            temp.append(task.result()[1])
        res.append(temp)

    # 单进程 ---------------------------------------------
    # for n in Ne:
    #     temp = []
    #     for t in Te:
    #         temp.append(sp.get_add_data(t, n)[1])
    #     res.append(temp)

    print(time.time() - start)
    # 结果展示
    Z = np.array(res)
    plt.imshow(Z, cmap='coolwarm')
    plt.xticks(range(len(Te)), list(map(lambda x: '{:.4f}'.format(x), Te)), rotation=90)
    plt.yticks(range(len(Ne)), list(map(lambda x: '{:.4e}'.format(x), Ne)))
    plt.show()

    # sp.get_add_data(44.3, 1e22)
    #
    # plt.plot(sp.result['wavelength'], sp.result['intensity'] / sp.result['intensity'].max())
    # plt.plot(sp.exp_data.data['wavelength'], sp.exp_data.data['intensity'] / sp.exp_data.data['intensity'].max())
    # plt.show()
