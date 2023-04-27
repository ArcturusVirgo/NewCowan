import os
from pathlib import Path
import numpy as np
import pandas as pd
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
    def read_file(path):
        temp_data = pd.read_csv(path, sep=',', skiprows=1, names=['wavelength', 'intensity'])
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
            temp_data = self.get_line_data(self.widen.data_init[['wavelength', 'gf']])
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
        temp_data['wavelength'] = 1239.85 / temp_data['wavelength']
        temp_data = temp_data[temp_data['wavelength'] < self.exp_data.x_range[1]]
        temp_data = temp_data[temp_data['wavelength'] > self.exp_data.x_range[0]]
        lambda_ = []
        strength = []
        if temp_data['wavelength'].min() > self.exp_data.x_range[0]:
            lambda_ += [self.exp_data.x_range[0]]
            strength += [0]
        for x, y in zip(temp_data['wavelength'], temp_data['gf']):
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
                                     names=['lowenergy', 'wspecen', 'wavelength', 'gf', 'lowk',
                                            'highk', 'fjt', 'fjtp'])

        self.widen_data = self.get_widen_data()

    def get_widen_data(self):
        temp_data = {}
        data_grouped = self.data_init.groupby(by=['lowk', 'highk'])
        print('正在展宽...')
        all_data = self.widen(self.data_init)
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

    @staticmethod
    def widen(data, delta=0, emin=91.88, emax=145.929, Te=25, fwhmgauss=0.27, n=2001):
        """
        二级函数
        Args:
            data: 'lowenergy', 'wspecen', 'wavelength', 'gf', 'lowk', 'highk', 'fjt', 'fjtp'
            delta: 偏移
            emin: 最小能量
            emax: 最大能量
            Te: 电子温度
            fwhmgauss: 半高宽
            n: 精度

        Returns: 展宽后的结果

        """
        min_energy_index = data['lowenergy'].argmin()
        min_energy = data['lowenergy'].iloc[min_energy_index]
        min_fjt = data['fjt'].iloc[min_energy_index]

        data['wfwhm'] = fwhmgauss
        data = data[abs(data['wavelength']) > emin]
        data = data[abs(data['wavelength']) < emax]
        if data.empty:
            return -1

        new_data = pd.DataFrame()
        new_data['wavenew'] = abs(1239.85 / (1239.85 / data['wavelength'] - delta))
        new_data['intensitynew'] = abs(data['gf'])
        new_data['fwhmnew'] = data['wfwhm'] * 2
        new_data['flowk'] = data['lowk']
        new_data['fhighk'] = data['highk']
        new_data['newfjtp'] = data['fjtp']
        new_data['newfjt'] = data['fjt']
        new_data['fwspecen'] = data['wspecen']
        new_data['flowenergy'] = data['lowenergy']
        flag = new_data['flowenergy'] > new_data['fwspecen']

        not_flag = np.bitwise_not(flag)
        newwspecen_1 = new_data['flowenergy'][flag]
        newwspecen_2 = new_data['fwspecen'][not_flag]
        new_data['newwspecen'] = newwspecen_1.combine_first(newwspecen_2)
        ffjtp_1 = new_data['newfjt'][flag]
        ffjtp_2 = new_data['newfjtp'][not_flag]
        new_data['ffjtp'] = ffjtp_1.combine_first(ffjtp_2)
        new_data['population'] = (2 * new_data['ffjtp'] + 1) * np.exp(
            -abs(new_data['newwspecen'] - min_energy) * 0.124 / Te) / (2 * min_fjt + 1)

        wave = np.linspace(new_data['wavenew'].min(), new_data['wavenew'].max(), n)
        # print(1239.85 / wave)
        result = pd.DataFrame()
        result['wavelength'] = wave
        result['wavelength'] = 1239.85 / result['wavelength']
        result['gauss'] = 0
        result['cross_NP'] = 0
        result['cross_P'] = 0
        for i in range(n):
            tt = new_data['intensitynew'] / np.sqrt(2 * np.pi) / fwhmgauss * 2.355 * np.exp(
                -2.355 ** 2 * (new_data['wavenew'] - wave[i]) ** 2 / fwhmgauss ** 2 / 2)
            ss = (new_data['intensitynew'] / (2 * new_data['ffjtp'] + 1)) * new_data['fwhmnew'] / (
                    2 * np.pi * ((new_data['wavenew'] - wave[i]) ** 2 + np.power(new_data['fwhmnew'], 2) / 4))
            uu = (new_data['intensitynew'] * new_data['population'] / (2 * new_data['ffjtp'] + 1)) * new_data[
                'fwhmnew'] / (
                         2 * np.pi * ((new_data['wavenew'] - wave[i]) ** 2 + np.power(new_data['fwhmnew'], 2) / 4))
            result.iloc[i, 1] = tt.sum()
            result.iloc[i, 2] = ss.sum()
            result.iloc[i, 3] = uu.sum()
            print(wave[i], tt.sum(), ss.sum(), uu.sum())
        return result



