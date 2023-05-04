import matplotlib.pyplot as plt
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from modules import *
from tqdm import tqdm

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

    # 计算多个 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # import time
    #
    # start = time.time()
    # Te_num = 10
    # Ne_num = 40
    # Te = np.linspace(33.33, 36.67, Te_num)
    # temp = np.linspace(1, 10, Ne_num // 6)
    # Ne = []
    # for i in range(20, 22):
    #     Ne += list(map(lambda x: x * 10 ** i, temp))
    # res = []
    #
    # # 多进程 ---------------------------------------------
    # pool = ProcessPoolExecutor(os.cpu_count() - 1)
    #
    # tasks_out = []
    # for n in Ne:
    #     tasks_in = []
    #     for t in Te:
    #         temp_task = pool.submit(sp.get_add_data, t, n)
    #         tasks_in.append(temp_task)
    #     tasks_out.append(tasks_in)
    #
    # pool.shutdown()
    #
    # for tasks in tasks_out:
    #     temp = []
    #     for task in tasks:
    #         temp.append(task.result()[1])
    #     res.append(temp)
    #
    # # 单进程 ---------------------------------------------
    # # for n in Ne:
    # #     temp = []
    # #     for t in Te:
    # #         temp.append(sp.get_add_data(t, n)[1])
    # #     res.append(temp)
    #
    # print(time.time() - start)
    # # 结果展示
    # Z = np.array(res)
    # trace1 = go.Heatmap(x=list(map(lambda x: '{:.2f}'.format(x), Te)), y=list(map(lambda x: '{:.2e}'.format(x), Ne)),
    #                     z=Z)
    # data = [trace1]
    # layout = go.Layout()
    # fig = go.Figure(data=data, layout=layout)
    # plot(fig, filename=Path.cwd().joinpath('a.html').as_posix(), auto_open=True)


    # 单个计算 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    print(sp.get_add_data(25.6, 3.15e20)[1])

    plt.plot(sp.result['wavelength'], sp.result['intensity'] / sp.result['intensity'].max())
    plt.plot(sp.exp_data.data['wavelength'], sp.exp_data.data['intensity'] / sp.exp_data.data['intensity'].max())
    plt.show()
