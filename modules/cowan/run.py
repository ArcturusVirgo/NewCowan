import json
import os
import shutil
import subprocess
from pathlib import Path

from .input_files import In36, In2


class Recorder:
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


class Run:
    def __init__(self, project_path: Path, name: str, in36: In36, in2: In2, recorder: Recorder, coupling_mode=1, ):
        """

        Args:
            name: 此次运行的名称
            coupling_mode: 1是L-S耦合 2是j-j耦合
        """
        self.name = name
        self.in36 = in36
        self.in2 = in2
        self.recorder = recorder
        self.project_path = project_path

        self.run_path = self.project_path / f'cal_result/{self.name}'

        self.coupling_mode = coupling_mode  # 1是L-S耦合 2是j-j耦合

        self.__get_ready()
        self.__run()
        self.recorder.add_history(self.name)

    def __get_ready(self):
        if self.run_path.exists():
            shutil.rmtree(self.run_path)
        shutil.copytree(self.project_path / 'bin', self.run_path)
        self.in36.save_as_in36(self.run_path / 'in36')
        self.in2.save_as_in2(self.run_path / 'in2')

    def __run(self):
        # 获取最初的运行路径
        original_path = Path.cwd()

        # 运行文件
        os.chdir(self.run_path)
        rcn = subprocess.run('./RCN.exe')
        rcn2 = subprocess.run('./RCN2.exe')
        self.__edit_ing11()
        rcg = subprocess.run('./RCG.exe')
        os.chdir(original_path)

    def __edit_ing11(self):
        with open('./out2ing', 'r', encoding='utf-8') as f:
            text = f.read()
        text = f'    {self.coupling_mode}{text[5:]}'
        with open('./ing11', 'w', encoding='utf-8') as f:
            f.write(text)
        with open('./out2ing', 'w', encoding='utf-8') as f:
            f.write(text)
