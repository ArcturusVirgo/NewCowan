import subprocess

subprocess.run('../venv/Scripts/pyside6-designer.exe ./vertical_line.ui')
subprocess.run('../venv/Scripts/pyside6-uic.exe ./vertical_line.ui -o ./vertical_line.py')

