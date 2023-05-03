# 原子信息
import matplotlib.pyplot as plt
import numpy as np

ATOM = {1: ['H', '氢'], 2: ['He', '氦'], 3: ['Li', '锂'], 4: ['Be', '铍'], 5: ['B', '硼'],
        6: ['C', '碳'], 7: ['N', '氮'], 8: ['O', '氧'], 9: ['F', '氟'], 10: ['Ne', '氖'],
        11: ['Na', '钠'], 12: ['Mg', '镁'], 13: ['Al', '铝'], 14: ['Si', '硅'], 15: ['Pi', '磷'],
        16: ['S', '硫'], 17: ['Cl', '氯'], 18: ['Ar', '氩'], 19: ['K', '钾'], 20: ['Ca', '钙'],
        21: ['Sc', '钪'], 22: ['Ti', '钛'], 23: ['V', '钒'], 24: ['Cr', '铬'], 25: ['Mn', '锰'],
        26: ['Fe', '铁'], 27: ['Co', '钴'], 28: ['Ni', '镍'], 29: ['Cu', '铜'], 30: ['Zn', '锌'],
        31: ['Ga', '镓'], 32: ['Ge', '锗'], 33: ['As', '砷'], 34: ['Se', '硒'], 35: ['Br', '溴'],
        36: ['Kr', '氪'], 37: ['Rb', '铷'], 38: ['Sr', '锶'], 39: ['Y', '钇'], 40: ['Zr', '锆'],
        41: ['Nb', '铌'], 42: ['Mo', '钼'], 43: ['Tc', '锝'], 44: ['Ru', '钌'], 45: ['Rh', '铑'],
        46: ['Pd', '钯'], 47: ['Ag', '银'], 48: ['Cd', '镉'], 49: ['In', '铟'], 50: ['Sn', '锡'],
        51: ['Sb', '锑'], 52: ['Te', '碲'], 53: ['I', '碘'], 54: ['Xe', '氙'], 55: ['Cs', '铯'],
        56: ['Ba', '钡'], 57: ['La', '镧'], 58: ['Ce', '铈'], 59: ['Pr', '镨'], 60: ['Nd', '钕'],
        61: ['Pm', '钷'], 62: ['Sm', '钐'], 63: ['Eu', '铕'], 64: ['Gd', '钆'], 65: ['Tb', '铽'],
        66: ['Dy', '镝'], 67: ['Ho', '钬'], 68: ['Er', '铒'], 69: ['Tm', '铥'], 70: ['Yb', '镱'],
        71: ['Lu', '镥'], 72: ['Hf', '铪'], 73: ['Ta', '钽'], 74: ['W', '钨'], 75: ['Re', '铼'],
        76: ['Os', '锇'], 77: ['Ir', '铱'], 78: ['Pt', '铂'], 79: ['Au', '金'], 80: ['Hg', '汞'],
        81: ['Tl', '铊'], 82: ['Pb', '铅'], 83: ['Bi', '铋'], 84: ['Po', '钋'], 85: ['At', '砹'],
        86: ['Rn', '氡'], 87: ['Fr', '钫'], 88: ['Ra', '镭'], 89: ['Ac', '锕'], 90: ['Th', '钍'],
        91: ['Pa', '镤'], 92: ['U', '铀'], 93: ['Np', '镎'], 94: ['Pu', '钚'], 95: ['Am', '镅*'],
        96: ['Cm', '锔*'], 97: ['Bk', '锫*'], 98: ['Cf', '锎*'], 99: ['Es', '锿*'], 100: ['Fm', '镄*']}
# 支壳层排布顺序
SUBSHELL_SEQUENCE = ['1s',
                     '2s', '2p',
                     '3s', '3p',
                     '4s', '3d', '4p',
                     '5s', '4d', '5p',
                     '6s', '4f', '5d', '6p',
                     '7s', '5f', '6d']
# 支壳层排布顺序
SUBSHELL_NAME = ['1s',
                 '2s', '2p',
                 '3s', '3p', '3d',
                 '4s', '4p', '4d', '4f',
                 '5s', '5p', '5d', '5f', '5g',
                 '6s', '6p', '6d', '6f', '6g', '6h',
                 '7s', '7p', '7d', '7f', '7g', '7h', '7i']
# 角量子数名称
ANGULAR_QUANTUM_NUM_NAME = ['s', 'p', 'd', 'f', 'g', 'h', 'i']
# 电离能
IONIZATION_ENERGY = {
    13: [5.985769, 18.82855, 28.447642, 119.9924, 153.8252, 190.49, 241.76, 284.64, 330.21, 398.65, 442.005, 2085.97702,
         2304.140359]

}


class Atomic:
    def __init__(self, num: int, ion: int):
        self.num = num  # 原子序数
        self.ion = ion  # 离化度
        self.symbol = ATOM[self.num][0]  # 元素符号
        self.name = ATOM[self.num][1]  # 元素名称
        self.electron_num = self.num - self.ion  # 实际的电子数量
        self.electron_arrangement = self.get_electron_base_arrangement()  # 电子排布情况
        self.base_configuration = ' '.join(self.get_configuration())  # 基组态

    def get_electron_base_arrangement(self):
        """根据当前现有电子数，获取电子基组态的核外排布情况
        Returns:
            返回一个字典，键为子壳层，值为子壳层的电子数
            例如 {
                '1s': 2,
                '2s': 2,
                '2p': 6,
                '3s': 2,
                '3p': 4,
            }

        """
        electron_arrangement = {}
        temp_electronic_num = self.electron_num
        for subshell in SUBSHELL_SEQUENCE:
            max_electronic_num = 4 * ANGULAR_QUANTUM_NUM_NAME.index(subshell[1]) + 2  # 子壳层的最大电子数
            if temp_electronic_num > max_electronic_num:
                electron_arrangement[subshell] = max_electronic_num
                temp_electronic_num -= max_electronic_num
            else:
                electron_arrangement[subshell] = temp_electronic_num
                break
        return electron_arrangement

    def revert_to_ground_state(self):
        """返回基态
        """
        self.electron_num = self.num - self.ion
        self.electron_arrangement = self.get_electron_base_arrangement()

    def get_configuration(self):
        """根据当前的电子排布情况，获取当前的电子组态
        Returns:
            返回一个列表
            例如 1. 基态：['3s02', '3p04']
                2. 激发态： ['3s02', '3p03', '4s01']
        """
        configuration = {}  # 按照子壳层的顺序排列的电子组态
        flag = False  # 是否开始写入
        for i, subshell_name in enumerate(SUBSHELL_NAME):
            if subshell_name in self.electron_arrangement.keys():
                l = ANGULAR_QUANTUM_NUM_NAME.index(subshell_name[1])
                if self.electron_arrangement[subshell_name] != 4 * l + 2 and not flag:  # 如果不是满子壳层
                    if i != 0:
                        configuration[SUBSHELL_NAME[i - 1]] = self.electron_arrangement[SUBSHELL_NAME[i - 1]]
                    flag = True
                if flag:
                    configuration[subshell_name] = self.electron_arrangement[subshell_name]
        if not flag:
            last_subshell_name = list(self.electron_arrangement.keys())[-1]
            for i, subshell_name in enumerate(SUBSHELL_NAME):
                if subshell_name in self.electron_arrangement.keys():
                    if last_subshell_name == subshell_name:
                        if i != 0:
                            configuration[SUBSHELL_NAME[i - 1]] = self.electron_arrangement[SUBSHELL_NAME[i - 1]]
                        flag = True
                    if flag:
                        configuration[subshell_name] = self.electron_arrangement[subshell_name]

        configuration_list = []
        for name, num in configuration.items():
            configuration_list.append('{}{:0>2}'.format(name, num))
        return configuration_list

    def arouse_electron(self, low_name, high_name):
        """ 激发电子，改变电子排布情况
        Args:
            low_name: 下态的支壳层名称
            high_name: 上态的支壳层名称
        """
        if low_name not in SUBSHELL_SEQUENCE:
            raise Exception(f'没有名为{low_name}的支壳层！')
        elif high_name not in SUBSHELL_SEQUENCE:
            raise Exception(f'没有名为{high_name}的支壳层!')
        elif low_name not in self.electron_arrangement.keys():
            raise Exception(f'没有处于{low_name}的电子！')
        elif self.electron_arrangement.get(high_name, 0) == 4 * ANGULAR_QUANTUM_NUM_NAME.index(high_name[1]) + 2:
            raise Exception(f'{high_name}的电子已经排满！')

        self.electron_arrangement[low_name] -= 1
        self.electron_arrangement[high_name] = self.electron_arrangement.get(high_name, 0) + 1
        if self.electron_arrangement[low_name] == 0:
            self.electron_arrangement.pop(low_name)

    def get_ion_abundance(self, temperature, electron_density):
        ion_num = np.array([i for i in range(self.num - 1)])
        ion_energy = np.array(IONIZATION_ENERGY[self.num][1:])
        electron_num = np.array([self.__get_outermost_num(i) for i in range(1, self.num)])

        S = (9 * 1e-6 * electron_num * np.sqrt(temperature / ion_energy) * np.exp(-ion_energy / temperature)) / (
                ion_energy ** 1.5 * (4.88 + temperature / ion_energy))
        Ar = 5.2 * 1e-14 * np.sqrt(ion_energy / temperature) * ion_num * (
                0.429 + 0.5 * np.log(ion_energy / temperature) + 0.469 * np.sqrt(temperature / ion_energy))
        A3r = 2.97 * 1e-27 * electron_num / (temperature * ion_energy ** 2 * (4.88 + temperature / ion_energy))

        ratio = S / (Ar + electron_density * A3r)
        abundance = self.__calculate_a_over_S(ratio)
        return abundance

    def __get_outermost_num(self, ion: int):
        temp_electron_num = self.num - ion
        for n in range(1, 7):
            if temp_electron_num > 2 * n ** 2:
                temp_electron_num -= 2 * n ** 2
            else:
                electron_num = temp_electron_num
                return electron_num

    @staticmethod
    def __calculate_a_over_S(a_ratios):
        # 计算a1, a2, ..., a_n
        a = np.zeros(len(a_ratios) + 1)
        a[0] = 1
        for i in range(1, len(a)):
            a[i] = a[i - 1] * a_ratios[i - 1]

        # 计算S
        S = np.sum(a)

        # 计算a1/S, a2/S, ..., a_n/S
        a_over_S = a / S

        return a_over_S

    #
    def __str__(self):
        """打印原子信息
        Returns:
            返回一个字符串，格式为：
            原子序数，元素符号，元素名称，电子组态
        """
        return '{: >3}  {:>2}  {:<2}   {}'.format(
            self.num, self.symbol, self.name, ' '.join(self.get_configuration()))