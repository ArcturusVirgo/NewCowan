import json
import os
import shutil
import subprocess

from .input_files import *


class Run:
    def __init__(self, name, coupling_mode=1, cowan_path: Path = Path('./program').resolve()):
        """

        Args:
            name: 此次运行的名称
            coupling_mode: 1是L-S耦合 2是j-j耦合
        """
        self.name = name
        self.cowan_path = cowan_path
        self.bin_path = self.cowan_path.joinpath('bin')
        self.result_path = self.cowan_path.joinpath(f'result/{name}')
        self.coupling_mode = coupling_mode  # 1是L-S耦合 2是j-j耦合

    def run(self):
        # 获取最初的运行路径
        original_path = os.getcwd()
        # 把输出文件拷贝至运行目录
        shutil.copyfile(self.bin_path.parent.joinpath('input/in36'), self.bin_path.joinpath('in36'))
        shutil.copyfile(self.bin_path.parent.joinpath('input/in2'), self.bin_path.joinpath('in2'))
        # 创建结果存放目录
        if self.result_path.exists():
            shutil.rmtree(self.result_path)
            self.result_path.mkdir(parents=False)
        else:
            self.result_path.mkdir(parents=False)

        # 检查文件完整性
        file_list = list(map(lambda x: x.name, self.bin_path.iterdir()))
        necessary = ['RCN.exe', 'RCN2.exe', 'RCG.exe', 'tape72', 'tape73', 'tape74']  # 运行的必要的文件
        for file in necessary:
            if file not in file_list:
                raise Exception('运行所需要的文件不完整')

        # 运行文件
        os.chdir(self.bin_path)
        rcn = subprocess.run('./RCN.exe')
        rcn2 = subprocess.run('./RCN2.exe')
        self.edit_ing11()
        rcg = subprocess.run('./RCG.exe')
        # resonance = subprocess.run('./Resonance lines.exe')
        os.chdir(original_path)

        # 将结果 移动 至 result 文件夹
        file_list = list(map(lambda x: x.name, self.bin_path.iterdir()))
        for file in file_list:
            if file not in necessary:
                # 先复制文件，再删除文件
                shutil.copyfile(self.bin_path.joinpath(file), self.result_path.joinpath(file))
                os.remove(self.bin_path.joinpath(file))

    def edit_ing11(self):
        with open('./out2ing', 'r', encoding='utf-8') as f:
            text = f.read()
        text = f'    {self.coupling_mode}{text[5:]}'
        with open('./ing11', 'w', encoding='utf-8') as f:
            f.write(text)
        with open('./out2ing', 'w', encoding='utf-8') as f:
            f.write(text)

    def clear_directory(self):
        """
        清空运行目录
        Returns:

        """
        for path in self.result_path.parent.iterdir():
            shutil.rmtree(path)


class History:
    def __init__(self, path):
        self.path = path
        self.run_history = []
        self.selection = []
        self.load()

    def add_history(self, name):
        self.run_history.append(name)

    def clear_history(self):
        self.run_history = []

    def add_selection(self, name):
        self.selection.append(name)

    def del_selection(self, index):
        self.selection.pop(index)

    def load(self):
        file_path = self.path / './.cowan/history.json'
        text = file_path.read_text(encoding='utf-8')
        temp = json.loads(text)
        self.run_history = temp['history']
        self.selection = temp['selection']

    def save(self):
        file_path = self.path / './.cowan/history.json'
        f = open(file_path, 'w', encoding='utf-8')
        temp = {
            'history': self.run_history,
            'selection': self.selection
        }
        json.dump(temp, f)
        f.close()
