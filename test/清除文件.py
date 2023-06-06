import os
import shutil

names = os.listdir('F:/Project/Fortran/CLion/Cowan_F/working_directory/')
for name in names:
    if 'result' in name:
        os.remove(f'F:/Project/Fortran/CLion/Cowan_F/working_directory/{name}')
