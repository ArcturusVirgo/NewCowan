import asyncio
from concurrent.futures import ProcessPoolExecutor
from modules import *
from tqdm import tqdm


async def main(n_values, t_values):
    pool = ProcessPoolExecutor(os.cpu_count() - 1)
    tasks_out = []

    for n in n_values:
        tasks_in = []
        for t in t_values:
            temp_task = loop.run_in_executor(pool, sp.get_add_data, t, n)
            tasks_in.append(temp_task)
        tasks_out.append(tasks_in)

    # 等待所有任务完成并跟踪进度
    for tasks in tasks_out:
        temp = []
        for future in asyncio.as_completed(tasks):
            # 处理已完成任务的结果
            result = await future
            temp.append(result[1])
            tbar.update(1)
        res.append(temp)


if __name__ == '__main__':
    import time

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

    start = time.time()
    Te_num = 20
    Ne_num = 20
    Te = np.linspace(10, 50, Te_num)
    Ne = np.power(10, np.linspace(np.log10(1e17), np.log10(2e23), Ne_num))
    tbar = tqdm(total=Te_num * Ne_num)
    res = []

    # 多进程 ---------------------------------------------
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(Ne, Te))

    # 单进程 ---------------------------------------------
    # for n in Ne:
    #     temp = []
    #     for t in Te:
    #         tbar.update(1)
    #         temp.append(sp.get_add_data(t, n)[1])
    #     res.append(temp)

    print((time.time() - start) / (Ne_num * Te_num))
    # 结果展示
    Z = np.array(res)
    trace1 = go.Heatmap(x=Te, y=Ne, z=Z)
    data = [trace1]
    layout = go.Layout(
        yaxis={
            'type': 'log',
            'tickformat': '.4e'
        }
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename=Path.cwd().joinpath('a.html').as_posix(), auto_open=True)
