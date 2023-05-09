import math
from pprint import pprint
from typing import List
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas
# import pandas
import pandas as pd
# import numba
# import numexpr as ne
# import modin.pandas as pd
# from multiprocessing import
from concurrent.futures import ProcessPoolExecutor

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


def widen(data: pandas.DataFrame,
          fwhmgauss,
          temperature: float,
          delta_lambda: float = 0.0,
          lambda_range: List[float] = (8, 14),
          n: int = 2000
          ):
    """

    Args:
        data (pandas.DataFrame):`
            pandas的DataFrame格式数据
            列标题依次为：energy_l, energy_h, wavelength_ev, intensity, index_l, index_h, J_l, J_h
            分别代表：下态能量，上态能量，波长，强度，下态序号，上态序号，下态J值，上态J值
        fwhmgauss (function): 半高宽随着波长的变化函数，
            调用实例：fwhmgauss(lambda)，其中lambda的单位是nm
        temperature (float): 等离子体温度
        delta_lambda: 谱线的整体偏移，单位是nm
        lambda_range(List[float]): 波长范围，单位是nm
        n: 展宽时的波长点的个数，即精度

    Returns:

    """
    new_data = data.copy()
    # 找到下态最小能量和最小能量对应的J值
    min_energy = new_data['energy_l'].min()
    min_J = new_data[new_data['energy_l'] == min_energy]['J_l'].min()
    # 筛选波长范围在实验数据范围内的跃迁正例个数
    min_wavelength_nm = lambda_range[0]
    max_wavelength_nm = lambda_range[1]
    min_wavelength_ev = 1239.85 / max_wavelength_nm
    max_wavelength_ev = 1239.85 / min_wavelength_nm
    new_data = new_data[(new_data['wavelength_ev'] > min_wavelength_ev) &
                        (new_data['wavelength_ev'] < max_wavelength_ev)]
    new_data = new_data.reindex()
    # 获取展宽所需要的数据
    new_wavelength = abs(1239.85 / (1239.85 / new_data['wavelength_ev'] - delta_lambda))  # 单位时ev
    new_wavelength = new_wavelength.values
    new_intensity = abs(new_data['intensity'])
    new_intensity = new_intensity.values
    flag = new_data['energy_l'] > new_data['energy_h']
    not_flag = np.bitwise_not(flag)
    temp_1 = new_data['energy_l'][flag]
    temp_2 = new_data['energy_h'][not_flag]
    new_energy = temp_1.combine_first(temp_2)
    new_energy = new_energy.values
    temp_1 = new_data['J_l'][flag]
    temp_2 = new_data['J_h'][not_flag]
    new_J = temp_1.combine_first(temp_2)
    new_J = new_J.values
    # 计算布居
    population = (2 * new_J + 1) * np.exp(-abs(new_energy - min_energy) * 0.124 / temperature) / (2 * min_J + 1)
    wave = np.linspace(min_wavelength_ev, max_wavelength_ev, n)
    result = pd.DataFrame()
    result['wavelength'] = 1239.85 / wave

    def complex_cal(wave: float,
                    new_intensity: numpy.array,
                    fwhmgauss: float,
                    new_wavelength: numpy.array,
                    population: numpy.array,
                    new_J: numpy.array):
        tt = new_intensity / np.sqrt(2 * np.pi) / fwhmgauss * 2.355 * np.exp(
            -2.355 ** 2 * (new_wavelength - wave) ** 2 / fwhmgauss ** 2 / 2)
        ss = (new_intensity / (2 * new_J + 1)) * 2 * fwhmgauss / (
                2 * np.pi * ((new_wavelength - wave) ** 2 + np.power(2 * fwhmgauss, 2) / 4))
        uu = (new_intensity * population / (2 * new_J + 1)) * 2 * fwhmgauss / (
                2 * np.pi * ((new_wavelength - wave) ** 2 + np.power(2 * fwhmgauss, 2) / 4))

        return tt.sum(), ss.sum(), uu.sum()

    res = [complex_cal(wave[i], new_intensity, fwhmgauss(wave[i]), new_wavelength, population, new_J) for i in range(n)]
    res = list(zip(*res))
    # pprint(res)
    result['gauss'] = res[0]
    result['cross_NP'] = res[1]
    result['cross_P'] = res[2]

    return result


if __name__ == '__main__':
    import time

    df = pd.read_csv('spectra.dat', sep='\s+',
                     names=['energy_l', 'energy_h', 'wavelength_ev', 'intensity', 'index_l', 'index_h', 'J_l', 'J_h'],
                     dtype=np.float64)
    s = time.time()
    df1 = widen(df, lambda x: 0.27, 34.6, 0, [6, 309], 405)
    print(time.time() - s)
    plt.plot(df1['wavelength'], df1['cross_P'])
    df = pd.read_csv('F:/Project/Fortran/CLion/Cowan_F/working_directory/widen_Al3.dat', sep='\s+', names=['x', 'y'])
    plt.plot(df['x'], df['y'])
    plt.show()
