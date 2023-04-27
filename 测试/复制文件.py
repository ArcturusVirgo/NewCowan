import pandas as pd
import shutil
datas = []
for i in range(3, 7):
    shutil.copy(f'../program/result/Al_{i}/spectra.dat', f'../program/result/spectra_Al{i}.dat')
