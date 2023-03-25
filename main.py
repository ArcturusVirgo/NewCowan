import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QTextBrowser, QVBoxLayout

from ui.main_window_ui import Ui_MainWindow
from cowan.constant import *
from cowan.run import *
from cowan.atom import *
from cowan.data import *


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.project_path: Path = Path.cwd()
        self.atom = Atomic(1, 0)
        self.exp_data: ExpData = None
        self.in36: In36 = In36(1, 0)
        self.in2 = In2()
        self.run: Run = None

        # 初始化
        self.init_UI()

    def init_UI(self):
        # 给元素选择器设置初始值
        self.ui.atomic_num.addItems(list(map(str, ATOM.keys())))
        self.ui.atomic_symbol.addItems(list(zip(*ATOM.values()))[0])
        self.ui.atomic_name.addItems(list(zip(*ATOM.values()))[1])
        # 设置高能级的组态名称
        self.ui.high_configuration.addItems(SUBSHELL_SEQUENCE[1:])

        # 信号槽的连接
        self.ui.atomic_num.activated.connect(self.slot_atomic_num)
        self.ui.atomic_symbol.activated.connect(self.slot_atomic_symbol)
        self.ui.atomic_name.activated.connect(self.slot_atomic_name)
        self.ui.atomic_ion.activated.connect(self.atomic_changed)
        self.ui.load_exp_data.triggered.connect(self.slot_load_exp_data)
        self.ui.choose_project_path.triggered.connect(self.slot_choose_project_path)
        self.ui.plot_exp.clicked.connect(self.slot_plot_exp)
        self.ui.auto_write_in36.clicked.connect(self.slot_auto_write_in36)
        self.ui.manual_write_in36.clicked.connect(self.slot_manual_write_in36)
        self.ui.add_configuration.clicked.connect(self.slot_add_configuration)
        self.ui.run_cowan.clicked.connect(self.slot_run_cowan)
        self.ui.load_in36.clicked.connect(self.slot_load_in36)
        self.ui.load_in2.clicked.connect(self.slot_load_in2)
        self.ui.preview_in36.clicked.connect(self.slot_preview_in36)
        self.ui.preview_in2.clicked.connect(self.slot_preview_in2)

    def slot_choose_project_path(self):
        path = QFileDialog.getExistingDirectory(self, '请选择项目路径')
        self.project_path = Path(path)
        self.ui.centralwidget.setEnabled(True)

    def slot_atomic_num(self, index):
        # 改变其他的两个元素标识
        self.ui.atomic_name.setCurrentIndex(index)
        self.ui.atomic_symbol.setCurrentIndex(index)
        # 改变离化度列表
        self.ui.atomic_ion.clear()
        self.ui.atomic_ion.addItems([str(i) for i in range(0, index + 1)])
        self.ui.atomic_ion.setCurrentIndex(0)
        # Atomic 对象改变
        self.atomic_changed()

    def slot_atomic_symbol(self, index):
        # 改变其他的两个元素标识
        self.ui.atomic_num.setCurrentIndex(index)
        self.ui.atomic_name.setCurrentIndex(index)
        # 改变离化度列表
        self.ui.atomic_ion.clear()
        self.ui.atomic_ion.addItems([str(i) for i in range(0, index + 1)])
        self.ui.atomic_ion.setCurrentIndex(0)
        # Atomic 对象改变
        self.atomic_changed()

    def slot_atomic_name(self, index):
        # 改变其他的两个元素标识
        self.ui.atomic_num.setCurrentIndex(index)
        self.ui.atomic_symbol.setCurrentIndex(index)
        # 改变离化度列表
        self.ui.atomic_ion.clear()
        self.ui.atomic_ion.addItems([str(i) for i in range(0, index + 1)])
        self.ui.atomic_ion.setCurrentIndex(0)
        # Atomic 对象改变
        self.atomic_changed()

    def slot_load_exp_data(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择实验数据', Path.cwd().__str__(), '文本文件(*.txt)')
        self.exp_data = ExpData(path)
        self.ui.load_exp_data.setText('重新加载实验数据')
        self.ui.plot_exp.setEnabled(True)
        self.slot_plot_exp()

        self.ui.statusbar.showMessage('已加载实验数据')

    def slot_plot_exp(self):
        self.exp_data.plot_html()
        self.ui.exp_web.load(QUrl.fromLocalFile(self.exp_data.plot_path))

    def slot_auto_write_in36(self):
        self.ui.high_configuration.setEnabled(True)
        self.ui.configuration_edit.setEnabled(False)
        self.ui.low_configuration.setEnabled(True)

    def slot_manual_write_in36(self):
        self.ui.configuration_edit.setEnabled(True)
        self.ui.low_configuration.setEnabled(False)
        self.ui.high_configuration.setEnabled(False)

    def slot_add_configuration(self):
        # 如果是自动添加
        if self.ui.auto_write_in36.isChecked():
            # 获取基组态
            low_configuration = ' '.join(self.atom.get_configuration())
            # 获取激发组态
            self.atom.arouse_electron(self.ui.low_configuration.currentText(),
                                      self.ui.high_configuration.currentText())
            high_configuration = ' '.join(self.atom.get_configuration())
            self.atom.revert_to_ground_state()

            # 添加组态
            self.in36.add_configuration(low_configuration)
            self.in36.add_configuration(high_configuration)
        # 如果是手动添加
        elif self.ui.manual_write_in36.isChecked():
            self.in36.add_configuration(self.ui.configuration_edit.text())

        self.update_in36_configuration_view()

    def slot_run_cowan(self):
        self.get_in36_control_card()
        self.get_in2_control_card()
        # self.in36.save_as_in36('./program/input')
        # self.in2.save_as_in2('./program/input')
        self.run = Run(f'{self.atom.atomic_symbol}_{self.atom.ionization}', self.in36, self.in2,
                       self.ui.coupling_mode.currentIndex() + 1)
        self.run.run()

    def slot_load_in36(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择in36文件', Path.cwd().__str__(), '')
        self.atomic_changed(path)
        # 改变元素选择
        self.ui.atomic_num.setCurrentIndex(self.atom.atomic_num - 1)
        self.ui.atomic_name.setCurrentIndex(self.atom.atomic_num - 1)
        self.ui.atomic_symbol.setCurrentIndex(self.atom.atomic_num - 1)
        # 改变离化度列表
        self.ui.atomic_ion.clear()
        self.ui.atomic_ion.addItems([str(i) for i in range(0, self.atom.atomic_num)])
        self.ui.atomic_ion.setCurrentIndex(self.atom.ionization)

        # 配置卡
        for i in range(23):
            eval(f'self.ui.in36_{i + 1}').setText(self.in36.control_card[i].strip(' '))
            self.in2 = In2(path)

    def slot_load_in2(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择in2文件', Path.cwd().__str__(), '')
        self.in2 = In2(path)
        in2_input_name = ['in2_1', 'in2_2', 'in2_3', 'in2_4', 'in2_5', 'in2_6', 'in2_7', 'in2_8',
                          'in2_9_a', 'in2_9_b', 'in2_9_c', 'in2_9_d',
                          'in2_10',
                          'in2_11_a', 'in2_11_b', 'in2_11_c', 'in2_11_d', 'in2_11_e',
                          'in2_12', 'in2_13', 'in2_14', 'in2_15', 'in2_16', 'in2_17', 'in2_18', 'in2_19', ]
        for i, n in enumerate(in2_input_name):
            if '11' in n:
                eval(f'self.ui.{n}').setValue(int(self.in2.input_card[i].strip(' ')))
            else:
                eval(f'self.ui.{n}').setText(self.in2.input_card[i].strip(' '))

    def slot_preview_in36(self):
        dialog = QDialog()
        dialog.resize(1000, 500)
        text_browser = QTextBrowser(dialog)
        dialog_layout = QVBoxLayout(dialog)

        dialog_layout.addWidget(text_browser)
        dialog.setLayout(dialog_layout)

        in36 = self.in36.get_in36_text()

        temp = '↓         ↓         ↓         ↓         ↓         ↓         ↓         ↓         \n'
        text_browser.setText(temp + in36)
        text_browser.setStyleSheet('font: 12pt "Consolas";')

        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

    def slot_preview_in2(self):
        dialog = QDialog()
        dialog.resize(1000, 500)
        text_browser = QTextBrowser(dialog)
        dialog_layout = QVBoxLayout(dialog)

        dialog_layout.addWidget(text_browser)
        dialog.setLayout(dialog_layout)

        in36 = self.in2.get_in2_text()

        temp = '↓         ↓         ↓         ↓         ↓         ↓         ↓         ↓         \n'
        text_browser.setText(temp + in36)
        text_browser.setStyleSheet('font: 12pt "Consolas";')

        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

    def update_in36_configuration_view(self):
        df = pd.DataFrame(self.in36.configuration_card, columns=['原子序数', '原子状态', '标识符', '空格', '组态'],
                          index=list(range(1, len(self.in36.configuration_card) + 1)))
        df = df[['原子序数', '原子状态', '标识符', '组态']]
        model = TableModel(df)
        self.ui.in36_configuration_view.setModel(model)

    def get_in36_control_card(self):
        """
        二级函数
        """
        v0 = '{:>1}'.format(self.ui.in36_1.text())
        v1 = '{:>1}'.format(self.ui.in36_2.text())
        v2 = '{:>1}'.format(self.ui.in36_3.text())
        v3 = '{:>2}'.format(self.ui.in36_4.text())
        v4 = '{:>1}'.format(self.ui.in36_5.text())
        v5 = '{:>2}'.format(self.ui.in36_6.text())
        v6 = '{:>2}'.format(self.ui.in36_7.text())
        v7 = '{:>3}'.format(self.ui.in36_8.text())
        v8 = '{:>2}'.format(self.ui.in36_9.text())
        v9 = '{:>5}'.format(self.ui.in36_10.text())
        v10 = '{:>10}'.format(self.ui.in36_11.text())
        v11 = '{:>10}'.format(self.ui.in36_12.text())
        v12 = '{:>2}'.format(self.ui.in36_13.text())
        v13 = '{:>2}'.format(self.ui.in36_14.text())
        v14 = '{:>1}'.format(self.ui.in36_15.text())
        v15 = '{:>1}'.format(self.ui.in36_16.text())
        v16 = '{:>2}'.format(self.ui.in36_17.text())
        v17 = '{:>2}'.format(self.ui.in36_18.text())
        v18 = '{:>5}'.format(self.ui.in36_19.text())
        v19 = '{:>5}'.format(self.ui.in36_20.text())
        v20 = '{:>5}'.format(self.ui.in36_21.text())
        v21 = '{:>5}'.format(self.ui.in36_22.text())
        v22 = '{:>5}'.format(self.ui.in36_23.text())
        temp = []
        for i in range(23):
            temp.append(eval(f'v{i}'))
        self.in36.control_card = temp

    def get_in2_control_card(self):
        v0 = '{:>5}'.format(self.ui.in2_1.text())
        v1 = '{:>2}'.format(self.ui.in2_2.text())
        v2 = '{:>1}'.format(self.ui.in2_3.text())
        v3 = '{:>2}'.format(self.ui.in2_4.text())
        v4 = '{:>1}'.format(self.ui.in2_5.text())
        v5 = '{:>2}'.format(self.ui.in2_6.text())
        v6 = '{:>7}'.format(self.ui.in2_7.text())
        v7 = '{:>1}'.format(self.ui.in2_8.text())

        v8 = '{:>8}'.format(self.ui.in2_9_a.text())
        v9 = '{:>8}'.format(self.ui.in2_9_b.text())
        v10 = '{:>8}'.format(self.ui.in2_9_c.text())
        v11 = '{:>4}'.format(self.ui.in2_9_d.text())

        v12 = '{:>1}'.format(self.ui.in2_10.text())

        v13 = '{:>2}'.format(self.ui.in2_11_a.text())
        v14 = '{:>2}'.format(self.ui.in2_11_b.text())
        v15 = '{:>2}'.format(self.ui.in2_11_c.text())
        v16 = '{:>2}'.format(self.ui.in2_11_d.text())
        v17 = '{:>2}'.format(self.ui.in2_11_e.text())

        v18 = '{:>5}'.format(self.ui.in2_12.text())
        v19 = '{:>5}'.format(self.ui.in2_13.text())
        v20 = '{:>1}'.format(self.ui.in2_14.text())
        v21 = '{:>1}'.format(self.ui.in2_15.text())
        v22 = '{:>1}'.format(self.ui.in2_16.text())
        v23 = '{:>1}'.format(self.ui.in2_17.text())
        v24 = '{:>1}'.format(self.ui.in2_18.text())
        v25 = '{:>5}'.format(self.ui.in2_19.text())
        temp = []
        for i in range(26):
            temp.append(eval(f'v{i}'))
        self.in2.input_card = temp

    def atomic_changed(self, in36_path=None):
        if type(in36_path) != str:
            # 获取原子序数和离化度
            atomic_num = int(self.ui.atomic_num.currentText())
            atomic_ion = int(self.ui.atomic_ion.currentText())
            # 创建 In36 对象
            self.in36 = In36(atomic_num, atomic_ion)
        else:
            self.in36 = In36(-1, -1, in36_path)
            # 获取原子序数和离化度
            atomic_num = self.in36.atomic_num
            atomic_ion = self.in36.atomic_ion
        # 更新 Atomic 对象
        self.atom = Atomic(atomic_num, atomic_ion)
        # 设置基组态
        self.ui.base_configuration.setText(self.atom.base_configuration)
        # 更新低能级的组态
        self.ui.low_configuration.clear()
        self.ui.high_configuration.clear()
        self.ui.low_configuration.addItems(list(self.atom.electronic_arrangement.keys()))
        temp_list = []
        for v in SUBSHELL_SEQUENCE:
            if v not in self.atom.electronic_arrangement:
                temp_list.append(v)
        self.ui.high_configuration.addItems(temp_list)
        # 更新 in36 组态的表格
        self.update_in36_configuration_view()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
