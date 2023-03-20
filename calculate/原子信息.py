# 原子信息
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
# 角量子数名称
ANGULAR_QUANTUM_NUM_NAME = ['s', 'p', 'd', 'f', 'g', 'h', 'i']


class Atomic:
    def __init__(self, atomic_num, ionization):
        self.atomic_num = atomic_num  # 原子序数
        self.ionization = ionization  # 离化度
        self.atomic_symbol = ATOM[self.atomic_num][0]
        self.atomic_name = ATOM[self.atomic_num][1]
        self.electronic_num = self.atomic_num - self.ionization + 1  # 实际的电子数量
        self.electronic_arrangement = self.get_electronic_arrangement()  # 电子排布情况

    def get_electronic_arrangement(self):
        electronic_arrangement = {}
        temp_electronic_num = self.electronic_num
        for subshell in SUBSHELL_SEQUENCE:
            max_electronic_num = 4 * ANGULAR_QUANTUM_NUM_NAME.index(subshell[1]) + 2  # 子壳层的最大电子数
            if temp_electronic_num > max_electronic_num:
                electronic_arrangement[subshell] = max_electronic_num
                temp_electronic_num -= max_electronic_num
            else:
                electronic_arrangement[subshell] = temp_electronic_num
                break
        return electronic_arrangement

    def revert_to_ground_state(self):
        self.electronic_arrangement = self.get_electronic_arrangement()

    def get_configuration(self):
        configuration = {}
        flag = False
        for n in range(1, 8):
            for l in range(0, n):
                subshell_name = f'{n}{ANGULAR_QUANTUM_NUM_NAME[l]}'
                if subshell_name in self.electronic_arrangement.keys():
                    if self.electronic_arrangement[subshell_name] != 4 * l + 2:
                        flag = True
                    if flag:
                        configuration[subshell_name] = self.electronic_arrangement[subshell_name]
        if not flag:
            last_subshell_name = list(self.electronic_arrangement.keys())[-1]
            for n in range(1, 8):
                for l in range(0, n):
                    subshell_name = f'{n}{ANGULAR_QUANTUM_NUM_NAME[l]}'
                    if subshell_name in self.electronic_arrangement.keys():
                        if last_subshell_name == subshell_name:
                            flag = True
                        if flag:
                            configuration[subshell_name] = self.electronic_arrangement[subshell_name]

        configuration_list = []
        for name, num in configuration.items():
            configuration_list.append('{}{:0>2}'.format(name, num))
        return configuration_list

    def arouse_electron(self, low_name, high_name):
        if low_name not in SUBSHELL_SEQUENCE:
            raise Exception(f'没有名为{low_name}的支壳层！')
        elif high_name not in SUBSHELL_SEQUENCE:
            raise Exception(f'没有名为{high_name}的支壳层!')
        elif low_name not in self.electronic_arrangement.keys():
            raise Exception(f'没有处于{low_name}的电子！')
        elif self.electronic_arrangement.get(high_name, 0) == 4 * ANGULAR_QUANTUM_NUM_NAME.index(high_name[1]) + 2:
            raise Exception(f'{high_name}的电子已经排满！')

        self.electronic_arrangement[low_name] -= 1
        self.electronic_arrangement[high_name] = self.electronic_arrangement.get(high_name, 0) + 1
        if self.electronic_arrangement[low_name] == 0:
            self.electronic_arrangement = self.electronic_arrangement.pop(low_name)

    def __str__(self):
        return '{: >3}  {:>2}  {:<2}   {}'.format(
            self.atomic_num, self.atomic_symbol, self.atomic_name, ' '.join(self.get_configuration()))


if __name__ == '__main__':
    for i in range(1, 101):
        element = Atomic(i, 1)
        print(element)
    # element = Atomic(20, 1)
    # element.arouse_electron('2s', '6p')
    # print(element)
    # element.revert_to_ground_state()
    # element.arouse_electron('2s', '4p')
    # print(element)
    # element.revert_to_ground_state()
