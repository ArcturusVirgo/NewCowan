import subprocess

subprocess.run('../venv/Scripts/pyside6-designer.exe ./main_window_ui.ui')
subprocess.run('../venv/Scripts/pyside6-uic.exe ./main_window_ui.ui -o ./main_window_ui.py')
