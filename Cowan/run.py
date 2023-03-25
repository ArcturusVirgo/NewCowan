import os
import shutil
import subprocess

from .input_files import *


class Run:
    def __init__(self, name, in36_obj: In36, in2_obj: In2, coupling_mode=1, bin_path='./program/bin'):
        """

        Args:
            name: 此次运行的名称
            in36_obj:
            in2_obj:
            coupling_mode: 1是L-S耦合 2是j-j耦合
            bin_path:
        """
        self.name = name
        self.bin_path = bin_path
        self.coupling_mode = coupling_mode  # 1是L-S耦合 2是j-j耦合

    def run(self):
        # 切换路径
        original_path = os.getcwd()  # 获取最初的运行路径
        os.chdir(self.bin_path)

        file_list = os.listdir()  # 获取文件夹下的所有文件名称
        necessary = ['RCN.exe', 'RCN2.exe', 'RCG.exe', 'Resonance lines.exe', 'tape72', 'tape73', 'tape74']  # 运行的必要的文件

        # 检查文件完整性
        for file in necessary:
            if file not in file_list:
                raise Exception('运行所需要的文件不完整')

        # 把输出文件拷贝至运行目录
        shutil.copyfile('../input/in36', './in36')
        shutil.copyfile('../input/in2', './in2')

        # 运行文件
        rcn = subprocess.run('./RCN.exe')
        rcn2 = subprocess.run('./RCN2.exe')
        shutil.copyfile('out2ing', 'ing11')
        # edit = subprocess.run(['notepad', 'ing11'])
        self.edit_ing11()
        rcg = subprocess.run('./RCG.exe')
        # resonance = subprocess.run('./Resonance lines.exe')

        # 创建目录
        if not os.path.exists(f'../result/{self.name}'):
            os.mkdir(f'../result/{self.name}')
        else:
            shutil.rmtree(f'../result/{self.name}')
            os.mkdir(f'../result/{self.name}')

        # 将结果 移动 至 result 文件夹
        file_list = os.listdir()  # 获取文件夹下的所有文件名称
        for file in file_list:
            if file not in necessary:
                # 先复制文件，再删除文件
                shutil.copyfile(f'{file}', f'../result/{self.name}/{file}')
                os.remove(file)

        # 切换回当前的运行目录
        os.chdir(original_path)

    def edit_ing11(self):
        with open('./ing11', 'r', encoding='utf-8') as f:
            text = f.read()
        text = f'    {self.coupling_mode}{text[5:]}'
        with open('./ing11', 'w', encoding='utf-8') as f:
            f.write(text)

    def clear_directory(self):
        original_path = os.getcwd()  # 获取最初的运行路径
        os.chdir(self.bin_path)
        for name in os.listdir('../result'):
            shutil.rmtree(f'../result/{name}')
        os.chdir(original_path)


if __name__ == '__main__':
    os.chdir('./../')
    # in36 = In36(path='./program/input/in36')
    # in2 = In2('./program/input/in2')
    # r = Run('Al+3', in36, in2)
    # r.run()
    # r.clear_directory()
