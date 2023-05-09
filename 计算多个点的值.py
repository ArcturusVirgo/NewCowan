import asyncio
from concurrent.futures import ProcessPoolExecutor
from modules import *
from tqdm import tqdm


async def cal_grid(n_values, t_values):
    res = []
    pool = ProcessPoolExecutor(os.cpu_count())
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
    return res


if __name__ == '__main__':
    import time

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

    start = time.time()
    Te_num = 2
    Ne_num = 2
    Te = np.linspace(21, 24, Te_num)
    Ne = np.power(10, np.linspace(np.log10(1e17), np.log10(2e20), Ne_num))
    tbar = tqdm(total=Te_num * Ne_num)

    # 多进程 ---------------------------------------------
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(cal_grid(Ne, Te))

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
