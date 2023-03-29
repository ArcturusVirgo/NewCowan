# from cowan.input_files import *
#
# in36 = In36(13, 0)
# in36.add_configuration('1s01 2s02')
# in36.add_configuration('1s01 2s02')
# print(list(zip(*in36.configuration_card))[-1])
# import pandas as pd
#
# # print('cowan'.split(' '))
# # a = {1: 2, 2: 3, 3: 4}
# # a.pop(1)
# # print(a)
#
# df = pd.DataFrame({
#     '1': [1, 2, 3, 4, 5],
#     '2': [1, 2, 3, 4, 5]
# })
# for x, y in zip(df['1'], df['2']):
#     print(x, y)
from pathlib import Path

from cowan.atom import Atomic
from cowan.run import Run

# from pathlib import Path
#
# import shutil
#
# p = Path('./123/222').joinpath('213')
# p.mkdir(parents=False)
#
# shutil.rmtree(p)

#
# l = [1, 2, 3]


# l.pop(0)
# print(l)

element = Atomic(13, 3)
# element.arouse_electron('2p', '3d')
print(element.get_configuration())