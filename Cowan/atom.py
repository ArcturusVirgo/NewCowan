from .constant import *


class Atomic:
    def __init__(self, atomic_num: int, ionization: int):
        self.atomic_num = atomic_num  # 原子序数
        self.ionization = ionization  # 离化度
        self.atomic_symbol = ATOM[self.atomic_num][0]
        self.atomic_name = ATOM[self.atomic_num][1]
        self.electronic_num = self.atomic_num - self.ionization  # 实际的电子数量
        self.electronic_arrangement = self.get_electronic_arrangement()  # 电子排布情况
        self.base_configuration = ' '.join(self.get_configuration())

    def get_electronic_arrangement(self):
        """
        获取电子排布
        Returns:

        """
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
        """
        返回基态
        Returns:

        """
        self.electronic_num = self.atomic_num - self.ionization
        self.electronic_arrangement = self.get_electronic_arrangement()

    def get_configuration(self):
        """
        获取当前的电子组态
        Returns:
            返回一个列表
        """
        configuration = {}  # 按照子壳层的顺序排列的电子组态
        flag = False  # 是否开始写入
        for i, subshell_name in enumerate(SUBSHELL_NAME):
            if subshell_name in self.electronic_arrangement.keys():
                l = ANGULAR_QUANTUM_NUM_NAME.index(subshell_name[1])
                if self.electronic_arrangement[subshell_name] != 4 * l + 2 and not flag:  # 如果不是满子壳层
                    if i != 0:
                        configuration[SUBSHELL_NAME[i - 1]] = self.electronic_arrangement[SUBSHELL_NAME[i - 1]]
                    flag = True
                if flag:
                    configuration[subshell_name] = self.electronic_arrangement[subshell_name]
        if not flag:
            last_subshell_name = list(self.electronic_arrangement.keys())[-1]
            for i, subshell_name in enumerate(SUBSHELL_NAME):
                if subshell_name in self.electronic_arrangement.keys():
                    if last_subshell_name == subshell_name:
                        if i != 0:
                            configuration[SUBSHELL_NAME[i - 1]] = self.electronic_arrangement[SUBSHELL_NAME[i - 1]]
                        flag = True
                    if flag:
                        configuration[subshell_name] = self.electronic_arrangement[subshell_name]

        configuration_list = []
        for name, num in configuration.items():
            configuration_list.append('{}{:0>2}'.format(name, num))
        return configuration_list

    def arouse_electron(self, low_name, high_name):
        """
        激发电子
        Args:
            low_name:
            high_name:

        Returns:

        """
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
            self.electronic_arrangement.pop(low_name)

    def __str__(self):
        return '{: >3}  {:>2}  {:<2}   {}'.format(
            self.atomic_num, self.atomic_symbol, self.atomic_name, ' '.join(self.get_configuration()))
