from pathlib import Path
from typing import List, Dict

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from fastdtw import fastdtw
from matplotlib import pyplot as plt
from plotly.offline import plot
from scipy.interpolate import interp1d
from scipy.signal import correlate

from .atom import Atomic


class ExpData:
    def __init__(self, project_path: Path, filepath: Path):
        """
        实验数据
        Args:
            project_path: 项目路径
            filepath: 实验谱的文件路径
        """
        self.plot_path = (project_path / 'figure/exp.html').as_posix()
        self.filepath: Path = filepath

        self.data: pd.DataFrame | None = None
        self.x_range: List[float] | None = None

        self.__read_file()
        self.__plot_html()

    def set_range(self, x_range: List[float]):
        """
        设置x轴范围
        Args:
            x_range: x轴范围，单位是nm
        """
        self.x_range = x_range
        self.data = self.data[(self.data['wavelength'] < self.x_range[1]) &
                              (self.data['wavelength'] > self.x_range[0])]
        self.__plot_html()

    def __read_file(self):
        """
        读取实验数据
        设置最小值和最大值
        """
        filetype = self.filepath.suffix[1:]
        if filetype == 'csv':
            temp_data = pd.read_csv(self.filepath, sep=',', skiprows=1, names=['wavelength', 'intensity'])
        elif filetype == 'txt':
            temp_data = pd.read_csv(self.filepath, sep='\s+', skiprows=1, names=['wavelength', 'intensity'])
        else:
            raise ValueError(f'filetype {filetype} is not supported')
        temp_data['intensity_normalization'] = temp_data['intensity'] / temp_data['intensity'].max()

        self.data = temp_data
        self.x_range = [self.data['wavelength'].min(), self.data['wavelength'].max()]

    def __plot_html(self):
        trace1 = go.Scatter(x=self.data['wavelength'], y=self.data['intensity'], mode='lines')
        data = [trace1]
        layout = go.Layout(margin=go.layout.Margin(autoexpand=False, b=15, l=30, r=0, t=0),
                           xaxis=go.layout.XAxis(range=self.x_range), )
        # yaxis=go.layout.YAxis(range=[self.min_strength, self.max_strength]))
        fig = go.Figure(data=data, layout=layout)

        plot(fig, filename=self.plot_path, auto_open=False)


class CalData:
    def __init__(self, project_path: Path, exp_data: ExpData, name):
        """

        Args:
            project_path: 项目路径
            exp_data: 实验数据类
            name: 计算的名称
        """
        self.name = name
        self.exp_data = exp_data
        self.plot_path = (project_path / f'figure/line/{self.name}.html').as_posix()
        self.filepath = (project_path / f'cal_result/{self.name}/spectra.dat').as_posix()
        self.data: pd.DataFrame | None = None

        self.__read_file()
        self.__plot_html()

    def __read_file(self):
        self.data = pd.read_csv(self.filepath, sep='\s+',
                                names=['energy_l', 'energy_h', 'wavelength_ev', 'intensity',
                                       'index_l', 'index_h', 'J_l', 'J_h'])

    def __plot_html(self):
        temp_data = self.__get_line_data(self.data[['wavelength_ev', 'intensity']])
        trace1 = go.Scatter(x=temp_data['wavelength'], y=temp_data['intensity'], mode='lines')
        data = [trace1]
        layout = go.Layout(margin=go.layout.Margin(autoexpand=False, b=15, l=30, r=0, t=0),
                           xaxis=go.layout.XAxis(range=self.exp_data.x_range),
                           )
        # yaxis=go.layout.YAxis(range=[self.min_strength, self.max_strength]))
        fig = go.Figure(data=data, layout=layout)
        plot(fig, filename=self.plot_path, auto_open=False)

    def __get_line_data(self, origin_data):
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
    def __init__(self,
                 project_path: Path,
                 exp_data: ExpData,
                 cal_data: CalData,
                 delta_lambda=0.0,
                 n=None):
        self.exp_data = exp_data
        self.cal_data = cal_data
        self.name = cal_data.name
        self.project_path = project_path

        self.plot_path_gauss = (project_path / f'figure/gauss/{self.name}.html').as_posix()
        self.plot_path_cross_NP = (project_path / f'figure/cross_NP/{self.name}.html').as_posix()
        self.plot_path_cross_P = (project_path / f'figure/cross_P/{self.name}.html').as_posix()
        self.plot_path_by_group_gauss: dict | None = None
        self.plot_path_by_group_cross_NP: dict | None = None
        self.plot_path_by_group_cross_P: dict | None = None

        self.delta_lambda: float = delta_lambda

        self.n = n

        self.init_data = self.cal_data.data.copy()

        self.widen_data: pd.DataFrame | None = None
        self.grouped_widen_data: Dict[str: pd.DataFrame] | None = None

    def widen(self,
              temperature: float,
              data: pd.DataFrame | None = None,
              save_in_memory: bool = True
              ):
        """

        Args:
            save_in_memory:
            data (pandas.DataFrame):
                pandas的DataFrame格式数据
                列标题依次为：energy_l, energy_h, wavelength_ev, intensity, index_l, index_h, J_l, J_h
                分别代表：下态能量，上态能量，波长，强度，下态序号，上态序号，下态J值，上态J值
            temperature (float): 等离子体温度

        Returns:
            返回一个DataFrame，包含了展宽后的数据
            列标题为：wavelength, gaussian, cross-NP, cross-P
        """
        if data is None:
            data = self.init_data.copy()
        fwhmgauss = self.__fwhmgauss
        lambda_range = self.exp_data.x_range

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
        if new_data.empty:
            return -1
        new_data = new_data.reindex()
        # 获取展宽所需要的数据
        new_wavelength = abs(1239.85 / (1239.85 / new_data['wavelength_ev'] - self.delta_lambda))  # 单位时ev
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
        if self.n is None:
            wave = np.array(self.exp_data.data['wavelength'].values)
        else:
            wave = np.linspace(min_wavelength_ev, max_wavelength_ev, self.n)
        result = pd.DataFrame()
        result['wavelength'] = 1239.85 / wave

        res = [self.__complex_cal(val, new_intensity, fwhmgauss(val), new_wavelength, population, new_J)
               for val in wave]
        res = list(zip(*res))
        result['gauss'] = res[0]
        result['cross_NP'] = res[1]
        result['cross_P'] = res[2]
        if save_in_memory:
            self.widen_data = result
        return result

    def widen_by_group(self, temperature):
        """
        返回一个字典，包含了按跃迁正例分组后的展宽数据，例如
        {'1-2': pd.DataFrame, '1-3': pd.DataFrame, ...}
        pd.DataFrame的列标题为：wavelength, gaussian, cross-NP, cross-P
        Args:
            temperature: 展宽时的温度

        Returns:

        """
        temp_data = {}
        # 按照跃迁正例展宽
        data_grouped = self.init_data.groupby(by=['index_l', 'index_h'])
        for index in data_grouped.groups.keys():
            temp_group = pd.DataFrame(data_grouped.get_group(index))
            temp_result = self.widen(temperature, temp_group, save_in_memory=False)
            # 如果这个波段没有跃迁正例
            if type(temp_result) == int:
                continue
            temp_data[f'{index[0]}-{index[1]}'] = temp_result
        self.grouped_widen_data = temp_data
        # self.plot_widen_by_group()

    def plot_widen(self):
        self.__plot_html(self.widen_data, self.plot_path_gauss, 'wavelength', 'gauss')
        self.__plot_html(self.widen_data, self.plot_path_cross_NP, 'wavelength', 'cross_NP')
        self.__plot_html(self.widen_data, self.plot_path_cross_P, 'wavelength', 'cross_P')

    def plot_widen_by_group(self):
        self.plot_path_by_group_gauss = {}
        self.plot_path_by_group_cross_NP = {}
        self.plot_path_by_group_cross_P = {}
        for key, value in self.grouped_widen_data.items():
            temp_path_1 = (self.project_path / f'figure/gauss/{self.name}_{key}.html').as_posix()
            temp_path_2 = (self.project_path / f'figure/cross_NP/{self.name}_{key}.html').as_posix()
            temp_path_3 = (self.project_path / f'figure/cross_P/{self.name}_{key}.html').as_posix()
            self.plot_path_by_group_gauss[key] = temp_path_1
            self.plot_path_by_group_cross_NP[key] = temp_path_2
            self.plot_path_by_group_cross_P[key] = temp_path_3
            self.__plot_html(value, temp_path_1, 'wavelength', 'gauss')
            self.__plot_html(value, temp_path_2, 'wavelength', 'cross_NP')
            self.__plot_html(value, temp_path_3, 'wavelength', 'cross_P')

    def __plot_html(self, data, path, x_name, y_name):
        trace1 = go.Scatter(x=data[x_name], y=data[y_name], mode='lines')
        data = [trace1]
        layout = go.Layout(margin=go.layout.Margin(autoexpand=False, b=15, l=30, r=0, t=0),
                           xaxis=go.layout.XAxis(range=self.exp_data.x_range),
                           )
        # yaxis=go.layout.YAxis(range=[self.min_strength, self.max_strength]))
        fig = go.Figure(data=data, layout=layout)
        plot(fig, filename=path, auto_open=False)

    @staticmethod
    def __complex_cal(wave: float,
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

    @staticmethod
    def __fwhmgauss(wavelength: float):
        return 0.5


class SpectraAdd:
    def __init__(self, project_path: Path, atom: Atomic, exp_data: ExpData, widen_list: List[Widen]):
        self.project_path = project_path
        self.exp_data = exp_data
        self.atom = atom
        self.widen_list = widen_list

        self.result: pd.DataFrame | None = None

    def get_add_data(self, temperature, electron_density):
        abundance = self.atom.get_ion_abundance2(temperature, electron_density)
        for widen in self.widen_list:
            # if widen.widen_data is None:
            widen.widen(temperature)
        res = pd.DataFrame()
        res['wavelength'] = self.widen_list[0].widen_data['wavelength']
        temp = np.zeros(res.shape[0])
        for widen in self.widen_list:
            ion = int(widen.name.split('_')[-1])
            temp += widen.widen_data['cross_P'].values * abundance[ion]
        res['intensity'] = temp
        self.result = res
        similarity = self.get_similarity()
        return res, similarity

    def get_similarity(self):
        return self.similarity4(self.exp_data.data[['wavelength', 'intensity']],
                               self.result[['wavelength', 'intensity']])

    @staticmethod
    def similarity(fax: pd.DataFrame, fbx: pd.DataFrame):
        """
        计算两个光谱的相似度
        遍历实验光谱的每个点，找到模拟光谱中最近的点，计算距离，并求和
        Args:
            fax: 实验光谱
            fbx: 模拟光谱

        Returns:

        """
        col_names_a = fax.columns
        col_names_b = fbx.columns
        x1 = fax[col_names_a[0]].values
        y1 = fax[col_names_a[1]].values
        x2 = fbx[col_names_b[0]].values
        y2 = fbx[col_names_b[1]].values
        y1 = y1 / y1.max()
        y2 = y2 / y2.max()

        res = 0
        for i in range(fax.shape[0]):
            res += min(np.sqrt((x1[i] - x2) ** 2 + (y1[i] - y2) ** 2))
        return res / fax.shape[0]

    def similarity2(self, fax: pd.DataFrame, fbx: pd.DataFrame):
        """
        计算两个光谱的相似度，根据R2进行判断
        Args:
            fax: 实验光谱
            fbx: 模拟光谱

        Returns:

        """
        y1, y2 = self.get_y1y2(fax, fbx)

        # y2是测量值，y1是预测值
        SS_reg = np.power(y1 - y2.mean(), 2).sum()
        SS_tot = np.power(y2 - y2.mean(), 2).sum()
        R2 = SS_reg / SS_tot
        if R2 > 1:
            return 1 / R2
        else:
            return R2

    def similarity3(self, fax: pd.DataFrame, fbx: pd.DataFrame):
        y1, y2 = self.get_y1y2(fax, fbx)

        distance, path = fastdtw(y1, y2)
        return distance

    def similarity4(self, fax: pd.DataFrame, fbx: pd.DataFrame):
        y1, y2 = self.get_y1y2(fax, fbx)
        corr = np.corrcoef(y1, y2)[0, 1]
        return corr

    @staticmethod
    def get_y1y2(fax: pd.DataFrame, fbx: pd.DataFrame, min_x=None, max_x=None):

        col_names_a = fax.columns
        col_names_b = fbx.columns
        if (min_x is None) and (max_x is None):
            min_x = max(fax[col_names_a[0]].min(), fbx[col_names_b[0]].min())
            max_x = min(fax[col_names_a[0]].max(), fbx[col_names_b[0]].max())
        fax_new = fax[(fax[col_names_a[0]] <= max_x) & (min_x <= fax[col_names_a[0]])]
        fbx_new = fbx[(fbx[col_names_b[0]] <= max_x) & (min_x <= fbx[col_names_b[0]])]
        print(col_names_b)
        print(fbx_new)
        f2 = interp1d(fbx_new[col_names_b[0]], fbx_new[col_names_b[1]], fill_value="extrapolate")
        x = fax_new[col_names_a[0]].values
        y1 = fax_new[col_names_a[1]].values
        y2 = f2(x)
        y1 = y1 / max(y1)
        y2 = y2 / max(y2)
        return y1, y2
