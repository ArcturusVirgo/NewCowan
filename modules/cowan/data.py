import os
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from partd import pandas
from tqdm import tqdm
import plotly.graph_objects as go
from plotly.offline import plot


class ExpData:
    def __init__(self, path, x_range=None):
        self.plot_path = Path.cwd().joinpath('./cache/exp/exp.html').__str__()
        self.data = self.read_file(path)
        if x_range:
            self.x_range = x_range
        else:
            self.x_range = [self.data['wavelength'].min(), self.data['wavelength'].max()]
        self.data = self.data[self.data['wavelength'] < self.x_range[1]]
        self.data = self.data[self.data['wavelength'] > self.x_range[0]]

    @staticmethod
    def read_file(path, filetype='csv'):
        if filetype == 'csv':
            temp_data = pd.read_csv(path, sep=',', skiprows=1, names=['wavelength', 'intensity'])
        elif filetype == 'txt':
            temp_data = pd.read_csv(path, sep='\s+', skiprows=1, names=['wavelength', 'intensity'])
        temp_data['intensity_normalization'] = temp_data['intensity'] / temp_data['intensity'].max()
        return temp_data

    def plot_html(self):
        trace1 = go.Scatter(x=self.data['wavelength'], y=self.data['intensity'], mode='lines')
        data = [trace1]
        layout = go.Layout(margin=go.layout.Margin(autoexpand=False, b=15, l=30, r=0, t=0),
                           xaxis=go.layout.XAxis(range=self.x_range), )
        # yaxis=go.layout.YAxis(range=[self.min_strength, self.max_strength]))
        fig = go.Figure(data=data, layout=layout)

        plot(fig, filename=self.plot_path, auto_open=False)


class CalData:
    def __init__(self, name, exp_data: ExpData):
        self.path = f'./program/result/{name}'
        self.line_path = Path.cwd().joinpath(f'./cache/cal/{name}_line.html').__str__()
        self.gauss_path = Path.cwd().joinpath(f'./cache/cal/{name}_gauss.html').__str__()
        self.crossNP_path = Path.cwd().joinpath(f'./cache/cal/{name}_crossNP.html').__str__()
        self.crossP_path = Path.cwd().joinpath(f'./cache/cal/{name}_crossP.html').__str__()
        self.widen = Widen(self.path)
        self.exp_data = exp_data
        self.get_html()

    def get_html(self):
        self.plot_html('line')
        self.plot_html('gauss')
        self.plot_html('cross-P')
        self.plot_html('cross-NP')

    def plot_html(self, type_):
        if type_ == 'line':
            temp_data = self.get_line_data(self.widen.data_init[['wavelength_ev', 'intensity']])
            path = self.line_path
        elif type_ == 'gauss':
            temp_data = self.widen.widen_data['all'][['wavelength', 'gauss']]
            path = self.gauss_path
        elif type_ == 'cross-P':
            temp_data = self.widen.widen_data['all'][['wavelength', 'cross_P']]
            path = self.crossP_path
        elif type_ == 'cross-NP':
            temp_data = self.widen.widen_data['all'][['wavelength', 'cross_NP']]
            path = self.crossNP_path
        else:
            raise Exception()
        temp_data.columns = ['x', 'y']
        trace1 = go.Scatter(x=temp_data['x'], y=temp_data['y'], mode='lines')
        data = [trace1]
        layout = go.Layout(margin=go.layout.Margin(autoexpand=False, b=15, l=30, r=0, t=0),
                           xaxis=go.layout.XAxis(range=self.exp_data.x_range),
                           )
        # yaxis=go.layout.YAxis(range=[self.min_strength, self.max_strength]))
        fig = go.Figure(data=data, layout=layout)
        plot(fig, filename=path, auto_open=False)

    def get_line_data(self, origin_data):
        temp_data = origin_data.copy()
        temp_data['wavelength'] = 1239.85 / temp_data['wavelength_ev']
        temp_data = temp_data[(temp_data['wavelength'] < self.exp_data.x_range[1]) &
                               (temp_data['wavelength'] > self.exp_data.x_range[0])]
        lambda_ = []
        strength = []
        if temp_data['wavelength'].min() > self.exp_data.x_range[0]:
            lambda_ += [self.exp_data.x_range[0]]
            strength += [0]
        for x, y in zip(temp_data['wavelength'], temp_data['intensity']):
            lambda_ += [x, x, x]
            strength += [0, y, 0]
        if temp_data['wavelength'].max() < self.exp_data.x_range[1]:
            lambda_ += [self.exp_data.x_range[1]]
            strength += [0]
        temp = pd.DataFrame({
            'wavelength': lambda_,
            'intensity': strength
        })
        return temp


class Widen:
    def __init__(self, path):
        self.path = Path(path)
        self.data_init = pd.read_csv(self.path / 'spectra.dat', sep='\s+',
                                     names=['energy_l', 'energy_h', 'wavelength_ev', 'intensity', 'index_l',
                                            'index_h', 'J_l', 'J_h'])

        self.widen_data = self.get_widen_data()

    def get_widen_data(self):
        temp_data = {}
        data_grouped = self.data_init.groupby(by=['index_l', 'index_h'])
        print('正在展宽...')
        all_data = self.widen(self.data_init, lambda x: 0.27, 34)
        temp_data['all'] = all_data
        # for index in tqdm(data_grouped.groups.keys()):
        #     temp_group = pd.DataFrame(data_grouped.get_group(index))
        #     temp_result = self.widen(temp_group)
        #     # 如果这个波段没有跃迁正例
        #     if type(temp_result) == int:
        #         continue
        #     temp_data[f'{index[0]}-{index[1]}'] = temp_result
        print('展宽完成!')
        return temp_data

    def save_data(self, filename='result.xlsx'):
        writer = pd.ExcelWriter(filename)
        print('正在写入文件...')
        for key, value in tqdm(list(self.widen_data.items())):
            self.widen_data[key].to_excel(writer, sheet_name=key, index=False)
        writer.close()
        print('写入完成!')

    def draw_spect(self, from_result=False, filename='result.xlsx', save_as_pic=False, pic_name='pic.png', plt=None):
        if from_result:
            df = pd.read_excel(filename, sheet_name=None)
        else:
            df = self.widen_data

        intensity_max = -1
        cross_max = -1
        crossb_max = -1

        rows = len(df.keys())

        plt.figure(figsize=(12, 2 * rows), dpi=300)
        plt.subplots_adjust(left=0.05, bottom=0.025, top=0.975, right=0.95, wspace=0.2, hspace=0.5)

        for v in df.keys():
            data = df[v]
            if intensity_max < data['intensity'].max():
                intensity_max = data['intensity'].max()
            if cross_max < data['cross'].max():
                cross_max = data['cross'].max()
            if crossb_max < data['crossb'].max():
                crossb_max = data['crossb'].max()
        for index, v in enumerate(df.keys()):
            data = df[v]
            plt.subplot(rows, 3, 3 * index + 1)
            plt.ylim(0, intensity_max)
            plt.xlabel(f'{v} - intensity')
            plt.plot(data['wave'], data['intensity'])

            plt.subplot(rows, 3, 3 * index + 2)
            plt.ylim(0, cross_max)
            plt.xlabel(f'{v} - cross')
            plt.plot(data['wave'], data['cross'])

            plt.subplot(rows, 3, 3 * index + 3)
            plt.ylim(0, crossb_max)
            plt.xlabel(f'{v} - crossb')
            plt.plot(data['wave'], data['crossb'])

        if save_as_pic:
            plt.savefig(pic_name)
        else:
            plt.show()

    def widen(self,
              data: pd.DataFrame,
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

        res = [self.complex_cal(wave[i], new_intensity, fwhmgauss(wave[i]), new_wavelength, population, new_J) for i in
               range(n)]
        res = list(zip(*res))
        # pprint(res)
        result['gauss'] = res[0]
        result['cross_NP'] = res[1]
        result['cross_P'] = res[2]

        return result

    @staticmethod
    def complex_cal(wave: float,
                    new_intensity: np.array,
                    fwhmgauss: float,
                    new_wavelength: np.array,
                    population: np.array,
                    new_J: np.array):
        tt = new_intensity / np.sqrt(2 * np.pi) / fwhmgauss * 2.355 * np.exp(
            -2.355 ** 2 * (new_wavelength - wave) ** 2 / fwhmgauss ** 2 / 2)
        ss = (new_intensity / (2 * new_J + 1)) * 2 * fwhmgauss / (
                2 * np.pi * ((new_wavelength - wave) ** 2 + np.power(2 * fwhmgauss, 2) / 4))
        uu = (new_intensity * population / (2 * new_J + 1)) * 2 * fwhmgauss / (
                2 * np.pi * ((new_wavelength - wave) ** 2 + np.power(2 * fwhmgauss, 2) / 4))

        return tt.sum(), ss.sum(), uu.sum()
