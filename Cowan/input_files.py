from pathlib import Path
from typing import List

from .constant import *


class In36:
    def __init__(self, atomic_num, atomic_ion, path=None, ):
        # 这两个里边装的都是格式化好的数据
        if path:
            self.control_card, self.configuration_card = self.read_file(path)
            self.atomic_num = int(self.configuration_card[0][0].split(' ')[-1])
            self.atomic_ion = int(self.configuration_card[0][1].split('+')[-1])
            self.parity = self.get_parity()
        else:
            self.control_card, self.configuration_card = [], []
            self.atomic_num = atomic_num
            self.atomic_ion = atomic_ion
            self.parity = []

    @staticmethod
    def read_file(path):
        """
        读取in36文件
        Args:
            path: 文件路径
        """
        path = Path(path)
        with open(path, 'r') as f:
            lines = f.readlines()
        # 控制卡读入
        control_card_text = lines[0]
        control_card_list = []
        if len(control_card_text) != 80:
            control_card_text += ' ' * (80 - len(control_card_text))
        rules = [1, 1, 1, 2, 1, 2, 2, 3, 2, 5, 10, 10, 2, 2, 1, 1, 2, 2, 5, 5, 5, 5, 5]
        for rule in rules:
            control_card_list.append(control_card_text[:rule])
            control_card_text = control_card_text[rule:]
        # 组态卡读入
        input_card_list = []
        for line in lines[1:]:
            value = line.split()
            if value == ['-1']:
                break
            v0 = '{:>5}'.format(value[0])
            v1 = '{:>9}'.format(value[1])
            v2 = '{:>7}'.format(value[2])
            v3 = '             '
            v4 = ' '.join(value[3:])
            input_card_list.append([v0, v1, v2, v3, v4])
        return control_card_list, input_card_list

    def add_configuration(self, configuration):
        """
        添加组态，自动剔除重复数据
        Args:
            configuration: 要添加的组态
        """
        if self.configuration_card:
            temp_list = list(zip(*self.configuration_card))[-1]
        else:
            temp_list = []
        if configuration not in temp_list:
            v0 = '{:>5}'.format(self.atomic_num)
            v1 = '{:>9}'.format(f'{self.atomic_ion + 1}{ATOM[self.atomic_num][0]}+{self.atomic_ion}')
            v2 = '{:>7}'.format('11111')
            v3 = '             '
            v4 = configuration
            self.configuration_card.append([v0, v1, v2, v3, v4])

            self.update()

    def del_configuration(self, series):
        self.configuration_card.pop(series - 1)

        self.update()

    @staticmethod
    def judge_parity(configuration: str) -> int:
        """
        判断指定组态的宇称
            Args:
                configuration: 要判断的电子组态

            Returns:
                0: 偶宇称
                1: 奇宇称
            """

        configuration = list(configuration.split(' '))
        sum_ = 0
        for v in configuration:
            sum_ += ANGULAR_QUANTUM_NUM_NAME.index(v[1]) * eval(v[3:])

        if sum_ % 2 == 0:
            return 0
        else:
            return 1

    def get_parity(self) -> List[int]:
        """
        获取组态卡中所有组态的宇称
        Returns:
            所有组态的宇称
        """
        parity_list = []
        for v in self.configuration_card:
            parity_list.append(self.judge_parity(v[-1]))
        return parity_list

    def update(self):
        self.parity = self.get_parity()

    def get_in36_text(self):
        in36 = ''
        in36 += ''.join(self.control_card)
        in36 += '\n'
        for v in self.configuration_card:
            in36 += ''.join(v)
            in36 += '\n'
        in36 += '   -1\n'
        return in36

    def save_as_in36(self, path):
        path = Path(path)
        with open(path.joinpath('in36'), 'w') as f:
            f.write(self.get_in36_text())


class In2:
    def __init__(self, path=None):
        if type(path) == str:
            self.input_card = self.read_file(path)
        else:
            self.input_card = None

    @staticmethod
    def read_file(path):
        with open(path, "r") as f:
            line = f.readline()
        line = line.strip('\n')
        if len(line) != 80:
            line += ' ' * (80 - len(line))
        rules = [5, 2, 1, 2, 1, 2, 7, 1, 8, 8, 8, 4, 1, 2, 2, 2, 2, 2, 5, 5, 1, 1, 1, 1, 1, 5]
        input_card_list = []
        for rule in rules:
            input_card_list.append(line[:rule])
            line = line[rule:]
        return input_card_list

    def update_slater(self, *args):
        for arg in args:
            if not 10 < arg < 100:
                raise Exception('输入错误!')

        for i in range(13, 18):
            self.input_card[i] = str(args[i - 13])

    def get_in2_text(self):
        in2 = ''
        in2 += ''.join(self.input_card)
        in2 += '\n'
        in2 += '   -1\n\n'
        return in2

    def save_as_in2(self, path):
        path = Path(path)
        with open(path.joinpath('in2'), 'w') as f:
            f.write(self.get_in2_text())
        print('保存')


if __name__ == '__main__':
    # a = In36('./../program/input/in36')
    # a.add_configuration('1s01 2p02')
    # a.print()
    b = In2('./../program/input/in2')
    print(b.__dict__)
    b.update_slater(80, 80, 80, 80, 80)
    print(b.__dict__)
