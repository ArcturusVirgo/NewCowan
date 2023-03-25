import os
from pathlib import Path
import numpy as np
import pandas as pd
import tqdm as tqdm
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
        temp_data = pd.read_csv(path, sep=';', skiprows=1, names=['wavelength', 'intensity'])
        temp_data['intensity_normalization'] = temp_data['intensity'] / temp_data['intensity'].max()
        # TODO 等待细化
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
    pass


class Widen:
    def __init__(self, path):
        self.path = Path(path)
        self.data_init = pd.read_csv(self.path / 'spectra.dat', sep='\s+',
                                     names=['lowenergy', 'wspecen', 'wavelength', 'gf', 'lowk',
                                            'highk', 'fjt', 'fjtp'])

        self.widen_data = {}

    def get_widen_data(self):
        data_grouped = self.data_init.groupby(by=['lowk', 'highk'])
        print('正在展宽...')
        all_data = self.widen(self.data_init)
        self.widen_data['all'] = all_data
        for index in tqdm(data_grouped.groups.keys()):
            temp_group = data_grouped.get_group(index)
            temp_result = self.widen(temp_group)
            # 如果这个波段没有跃迁正例
            if type(temp_result) == int:
                continue
            self.widen_data[f'{index[0]}-{index[1]}'] = temp_result
        print('展宽完成!')
        return self.widen_data

    def save_data(self, filename='result.xlsx'):
        writer = pd.ExcelWriter(filename)
        print('正在写入文件...')
        for key, value in tqdm(list(self.widen_data.items())):
            self.widen_data[key].to_excel(writer, sheet_name=key, index=False)
        writer.save()
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
    def widen(data, delta=0, emin=49, emax=250, Te=25, fwhmgauss=0.27, n=2001):
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

        wave = np.linspace(emin, emax, n)
        result = pd.DataFrame()
        result['wave'] = wave
        result['intensity'] = 0
        result['cross'] = 0
        result['crossb'] = 0
        for i in range(n):
            tt = new_data['intensitynew'] / np.sqrt(2 * np.pi) / fwhmgauss * 2.355 * np.exp(
                -2.355 ** 2 * (new_data['wavenew'] - wave[i]) ** 2 / fwhmgauss ** 2 / 2)
            ss = (new_data['intensitynew'] / (2 * new_data['ffjtp'] + 1)) * new_data['fwhmnew'] / (
                    2 * np.pi * ((new_data['wavenew'] - wave[i]) ** 2 + np.power(new_data['fwhmnew'], 2) / 4))
            uu = (new_data['intensitynew'] * new_data['population'] / (2 * new_data['ffjtp'] + 1)) * new_data[
                'fwhmnew'] / (
                         2 * np.pi * ((new_data['wavenew'] - wave[i]) ** 2 + np.power(new_data['fwhmnew'], 2) / 4))
            result['intensity'].iloc[i] = tt.sum()
            result['cross'].iloc[i] = ss.sum()
            result['crossb'].iloc[i] = uu.sum()
        return result


if __name__ == '__main__':
    pass
    # os.chdir('../')
    # data = ExpData('./temp_file/Merge0_0001.Raw8.txt')
    # data.plot_html()
