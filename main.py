import inspect
import sys
import shelve
from PySide6.QtWidgets import QAbstractItemView, QFileDialog, QDialog, QTextBrowser, QMessageBox

from modules import *


class VerticalLine(QWidget):
    def __init__(self, x, y, height):
        super().__init__()
        self.ui = Ui_reference_line_window()
        self.ui.setupUi(self)
        self.dragPos = None
        self.ui.label.setMouseTracking(True)
        self.setGeometry(x, y, 100, height)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + (event.globalPosition().toPoint() - self.dragPos))
            self.dragPos = event.globalPosition().toPoint()
            event.accept()


class MainWindow(QMainWindow):
    def __init__(self, path, load_project=False):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # 设置默认的项目路径
        self.PROJECT_PATH = path
        self.WORKING_PATH = Path.cwd()

        self.recorder = Recorder(self.PROJECT_PATH)
        self.atom: Atomic | None = None
        self.in36: In36 = In36()
        self.in2: In2 = In2()
        self.exp_data: ExpData | None = None
        self.run: Run | None = None
        self.cal_data: CalData | None = None
        self.widen: Widen | None = None
        self.spectra_add: SpectraAdd | None = None

        self.v_line: VerticalLine | None = None

        # 初始化
        self.init()
        self.bind_slot()

        # 更新以上信息
        if load_project:
            self.load_project()

    def init(self):
        self.get_in36_control_card()
        self.get_in2_control_card()
        # 给元素选择器设置初始值
        self.ui.atomic_num.addItems(list(map(str, ATOM.keys())))
        self.ui.atomic_symbol.addItems(list(zip(*ATOM.values()))[0])
        self.ui.atomic_name.addItems(list(zip(*ATOM.values()))[1])
        # in36组态表格相关设置
        self.ui.in36_configuration_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # 设置行选择模式
        self.ui.in36_configuration_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 设置表格不可编辑
        self.ui.in36_configuration_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)  # 设置表格列宽自适应
        self.ui.page2_grid_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # 设置表格不可编辑
        self.ui.page2_grid_list.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)  # 设置表格列宽自适应
        # 隐藏不必要的按钮
        # self.ui.page_up.hide()
        # self.ui.page_down.hide()

    def bind_slot(self):
        # 页面切换按钮
        self.ui.page_up.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.page_down.clicked.connect(lambda x: self.ui.stackedWidget.setCurrentIndex(1))

        # 菜单栏
        self.ui.save_project.triggered.connect(self.slot_save_project)
        self.ui.exit_project.triggered.connect(self.slot_exit_project)
        self.ui.load_exp_data.triggered.connect(self.slot_load_exp_data)  # 加载实验数据
        self.ui.show_guides.triggered.connect(self.slot_show_guides)  # 显示参考线
        # 元素选择 - 下拉框
        self.ui.atomic_num.activated.connect(self.slot_atomic_num)  # 原子序数
        self.ui.atomic_symbol.activated.connect(self.slot_atomic_symbol)  # 元素符号
        self.ui.atomic_name.activated.connect(self.slot_atomic_name)  # 元素名称
        self.ui.atomic_ion.activated.connect(self.slot_atomic_ion)  # 离化度
        # 按钮
        self.ui.add_configuration.clicked.connect(self.slot_add_configuration)  # 添加组态
        self.ui.run_cowan.clicked.connect(self.slot_run_cowan)  # 运行Cowan
        self.ui.load_in36.clicked.connect(self.slot_load_in36)  # 加载in36文件
        self.ui.load_in2.clicked.connect(self.slot_load_in2)  # 加载in2文件
        self.ui.preview_in36.clicked.connect(self.slot_preview_in36)  # 预览in36
        self.ui.preview_in2.clicked.connect(self.slot_preview_in2)  # 预览in2
        self.ui.configuration_move_up.clicked.connect(self.slot_configuration_move_up)  # 组态上移
        self.ui.configuration_move_down.clicked.connect(self.slot_configuration_move_down)  # 组态下移
        self.ui.del_configuration.clicked.connect(self.slot_del_configuration)  # 删除组态
        self.ui.clear_history.clicked.connect(self.slot_clear_history)  # 清空运行历史
        self.ui.add_to_selection.clicked.connect(self.slot_add_to_selection)  # 将该项目添加至库中
        self.ui.del_selection.clicked.connect(self.slot_del_selection)  # 将该项目从库中删除
        self.ui.run_history_list.itemDoubleClicked.connect(self.slot_load_history)  # 加载库中的项目
        # 单选框
        self.ui.auto_write_in36.clicked.connect(self.slot_auto_write_in36)  # 自动生成in36
        self.ui.manual_write_in36.clicked.connect(self.slot_manual_write_in36)  # 手动输入in36
        self.ui.gauss.clicked.connect(self.slot_gauss)  # 线状谱展宽成gauss
        self.ui.crossP.clicked.connect(self.slot_crossp)  # 线状谱展宽成crossP
        self.ui.crossNP.clicked.connect(self.slot_crossnp)  # 线状谱展宽成crossNP
        # 输入框
        self.ui.in2_11_e.valueChanged.connect(self.slot_in2_11_e_value_changed)  # in2 11 e

        # 第二页 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.ui.page2_plot_spectrum.clicked.connect(self.slot_page2_plot_spectrum)  # 绘制谱图
        self.ui.page2_cal_grid.clicked.connect(self.slot_page2_cal_grid)  # 计算网格
        self.ui.page2_grid_list.itemDoubleClicked.connect(self.slot_page2_grid_list_clicked)

    def slot_show_guides(self):
        if self.v_line is None:
            x, y = self.ui.exp_web.mapToGlobal(self.ui.exp_web.pos()).toTuple()
            self.v_line = VerticalLine(x, y - 100, self.window().height() - 100)
            self.v_line.show()
            self.ui.show_guides.setText('隐藏参考线')
        else:
            self.v_line.close()
            self.v_line = None
            self.ui.show_guides.setText('显示参考线')

    # page_1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def slot_load_exp_data(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择实验数据', self.PROJECT_PATH.as_posix(),
                                                  '数据文件(*.txt *.csv)')
        path = Path(path)
        # 将实验数据复制到项目路径下
        if 'csv' in path.name:
            new_path = self.PROJECT_PATH / f'exp_data.csv'
        elif 'txt' in path.name:
            new_path = self.PROJECT_PATH / f'exp_data.txt'
        else:
            raise Exception('文件格式错误')
        try:
            shutil.copyfile(path, new_path)
        except shutil.SameFileError:
            pass
        self.exp_data = ExpData(self.PROJECT_PATH, new_path)
        self.update_exp_data_obj_about()

        self.ui.load_exp_data.setText('重新加载实验数据')
        self.ui.statusbar.showMessage('已加载实验数据')

    def slot_atomic_num(self, index):
        self.atom = Atomic(index + 1, 0)
        self.update_atom_obj_about()

    def slot_atomic_symbol(self, index):
        self.atom = Atomic(index + 1, 0)
        self.update_atom_obj_about()

    def slot_atomic_name(self, index):
        self.atom = Atomic(index + 1, 0)
        self.update_atom_obj_about()

    def slot_atomic_ion(self, index):
        self.atom = Atomic(self.atom.num, index)
        self.update_atom_obj_about()

    def slot_auto_write_in36(self):
        self.ui.high_configuration.setEnabled(True)
        self.ui.configuration_edit.setEnabled(False)
        self.ui.low_configuration.setEnabled(True)

    def slot_manual_write_in36(self):
        self.ui.configuration_edit.setEnabled(True)
        self.ui.low_configuration.setEnabled(False)
        self.ui.high_configuration.setEnabled(False)

    def slot_in2_11_e_value_changed(self):
        value = self.ui.in2_11_e.value()
        self.ui.in2_11_a.setValue(value)
        self.ui.in2_11_c.setValue(value)
        self.ui.in2_11_d.setValue(value)

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

        self.update_in36_obj_about()

    def slot_run_cowan(self):
        # 如果没有加载实验数据
        if self.exp_data is None:
            self.ui.statusbar.showMessage('请先加载实验数据')
            return
        # 获取界面中的数据
        self.get_in36_control_card()
        self.get_in2_control_card()
        # 获取当前时间
        # current_time = datetime.datetime.now()
        # 创建运行对象
        self.run = Run(project_path=self.PROJECT_PATH,
                       # name='{:0>4d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}_{}_{}'.format(
                       #     current_time.year, current_time.month, current_time.day,
                       #     current_time.hour, current_time.minute, current_time.second,
                       #     self.atom.symbol, self.atom.ion),
                       name='{}_{}'.format(self.atom.symbol, self.atom.ion),
                       in36=self.in36,
                       in2=self.in2,
                       recorder=self.recorder,
                       coupling_mode=self.ui.coupling_mode.currentIndex() + 1)
        self.update_run_obj_about()
        # 创建计算数据对象
        self.cal_data = CalData(project_path=self.PROJECT_PATH,
                                exp_data=self.exp_data,
                                name=self.run.name)
        self.update_cal_data_obj_about()
        # 创建展宽对象
        self.widen = Widen(project_path=self.PROJECT_PATH,
                           exp_data=self.exp_data,
                           cal_data=self.cal_data,
                           delta_lambda=0.0,
                           n=500)
        self.widen.widen(temperature=self.ui.temperature_1.value())
        self.ui.gauss.setEnabled(True)
        self.ui.crossP.setEnabled(True)
        self.ui.crossNP.setEnabled(True)
        self.update_widen_obj_about()
        # 将此状态保存
        obj_info = shelve.open(self.PROJECT_PATH.joinpath(f'cal_result/{self.run.name}/obj_info').as_posix())
        obj_info['atom'] = self.atom
        obj_info['cal_data'] = self.cal_data
        obj_info['exp_data'] = self.exp_data
        obj_info['in36'] = self.in36
        obj_info['in2'] = self.in2
        obj_info['cal_data'] = self.cal_data
        obj_info['run'] = self.run
        obj_info['widen'] = self.widen
        obj_info.close()

    def slot_gauss(self):
        self.ui.web_cal_widen.load(QUrl.fromLocalFile(self.widen.plot_path_gauss))

    def slot_crossp(self):
        self.ui.web_cal_widen.load(QUrl.fromLocalFile(self.widen.plot_path_cross_P))

    def slot_crossnp(self):
        self.ui.web_cal_widen.load(QUrl.fromLocalFile(self.widen.plot_path_cross_NP))

    def slot_load_in36(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择in36文件', self.PROJECT_PATH.as_posix(), '')
        self.in36.read_from_file(path)
        self.atom = Atomic(self.in36.atomic_num, self.in36.atomic_ion)
        self.update_atom_obj_about()
        self.update_in36_obj_about()

    def slot_load_in2(self):
        path, types = QFileDialog.getOpenFileName(self, '请选择in2文件', self.PROJECT_PATH.as_posix(), '')
        # 更新in2对象
        self.in2.read_from_file(path)
        self.update_in2_obj_about()

    def slot_preview_in36(self):
        dialog = QDialog()
        dialog.resize(1000, 500)
        text_browser = QTextBrowser(dialog)
        dialog_layout = QVBoxLayout(dialog)

        dialog_layout.addWidget(text_browser)
        dialog.setLayout(dialog_layout)

        self.get_in36_control_card()
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

        self.get_in2_control_card()
        in2 = self.in2.get_in2_text()

        temp = '↓         ↓         ↓         ↓         ↓         ↓         ↓         ↓         \n'
        text_browser.setText(temp + in2)
        text_browser.setStyleSheet('font: 12pt "Consolas";')

        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

    def slot_configuration_move_up(self):
        index = self.ui.in36_configuration_view.currentIndex().row()
        if 1 <= index <= len(self.in36.configuration_card):
            self.in36.configuration_move(index, 'up')
            self.update_in36_obj_about()
            self.ui.in36_configuration_view.setCurrentIndex(self.ui.in36_configuration_view.model().index(index - 1, 0))

    def slot_configuration_move_down(self):
        index = self.ui.in36_configuration_view.currentIndex().row()
        if 0 <= index <= len(self.in36.configuration_card) - 2:
            self.in36.configuration_move(index, 'down')
            self.update_in36_obj_about()
            self.ui.in36_configuration_view.setCurrentIndex(self.ui.in36_configuration_view.model().index(index + 1, 0))

    def slot_del_configuration(self):
        index = self.ui.in36_configuration_view.currentIndex().row()
        if index < len(self.in36.configuration_card):
            self.in36.del_configuration(index)
        self.update_in36_obj_about()

    def slot_clear_history(self):
        self.recorder.clear_history()
        self.update_recorder_obj_about()

    def slot_add_to_selection(self):
        name = self.ui.run_history_list.currentIndex().data()
        self.recorder.add_selection(name)
        self.update_recorder_obj_about()

    def slot_del_selection(self):
        index = self.ui.selection_list.currentIndex().row()
        self.recorder.del_selection(index)
        self.update_recorder_obj_about()

    def slot_load_history(self, index):
        name = index.text()
        obj_info = shelve.open(self.PROJECT_PATH.joinpath(f'cal_result/{name}/obj_info').as_posix())
        self.atom = obj_info['atom']
        self.cal_data = obj_info['cal_data']
        self.exp_data = obj_info['exp_data']
        self.in36 = obj_info['in36']
        self.in2 = obj_info['in2']
        self.cal_data = obj_info['cal_data']
        self.run = obj_info['run']
        self.widen = obj_info['widen']
        obj_info.close()
        self.update_atom_obj_about()
        self.update_in36_obj_about()
        self.update_in2_obj_about()
        self.update_exp_data_obj_about()
        self.update_run_obj_about()
        self.update_cal_data_obj_about()
        self.update_widen_obj_about()

    def slot_save_project(self):
        obj_info = shelve.open(self.PROJECT_PATH.joinpath('.cowan/obj_info').as_posix())
        obj_info['atom'] = self.atom
        obj_info['cal_data'] = self.cal_data
        obj_info['exp_data'] = self.exp_data
        obj_info['in36'] = self.in36
        obj_info['in2'] = self.in2
        obj_info['cal_data'] = self.cal_data
        obj_info['recorder'] = self.recorder
        obj_info['run'] = self.run
        obj_info['widen'] = self.widen
        obj_info.close()
        self.ui.statusbar.showMessage('项目保存成功！')

    def slot_exit_project(self):
        self.slot_save_project()
        sys.exit()

    def slot_page2_plot_spectrum(self):
        temperature = self.ui.page2_temperature.value()
        density = self.ui.page2_density_base.value() * 10 ** self.ui.page2_density_index.value()
        add_name_list = self.recorder.selection
        cal_obj_list = [CalData(self.PROJECT_PATH, self.exp_data, name) for name in add_name_list]
        widen_obj_list = [Widen(self.PROJECT_PATH, self.exp_data, cal_obj) for cal_obj in cal_obj_list]

        if self.spectra_add:
            self.spectra_add.widen_list = widen_obj_list
        else:
            self.spectra_add = SpectraAdd(self.PROJECT_PATH, self.atom, self.exp_data, widen_obj_list)
        self.spectra_add.get_add_data(temperature, density)
        self.spectra_add.plot_html()
        self.update_spectra_add_obj_about()

    def slot_page2_cal_grid(self):
        add_name_list = self.recorder.selection
        cal_obj_list = [CalData(self.PROJECT_PATH, self.exp_data, name) for name in add_name_list]
        widen_obj_list = [Widen(self.PROJECT_PATH, self.exp_data, cal_obj) for cal_obj in cal_obj_list]

        t_num = self.ui.temperature_num.value()
        ne_num = self.ui.density_num.value()
        t_list = np.linspace(self.ui.temperature_min.value(), self.ui.temperature_max.value(), t_num)
        ne_list = np.power(10, np.linspace(
            np.log10(self.ui.density_min_base.value() * 10 ** self.ui.density_min_index.value()),
            np.log10(self.ui.density_max_base.value() * 10 ** self.ui.density_max_index.value()),
            ne_num))
        self.spectra_add = SpectraAdd(self.PROJECT_PATH, self.atom, self.exp_data, widen_obj_list)
        self.ui.page2_progressBar.setValue(0)
        self.spectra_add.get_cal_grid(ne_list, t_list, self.ui.page2_progressBar)
        self.update_spectra_add_obj_about()

    def slot_page2_grid_list_clicked(self, item):
        temperature = self.spectra_add.grid_data['temperature'][item.column()]
        density = self.spectra_add.grid_data['density'][item.row()]
        temp = '{:.4e}'.format(density).split('e+')
        self.ui.page2_temperature.setValue(temperature)
        self.ui.page2_density_base.setValue(eval(temp[0]))
        self.ui.page2_density_index.setValue(eval(temp[1]))
        self.slot_page2_plot_spectrum()

    def get_in36_control_card(self):
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

    def update_atom_obj_about(self):
        fun_name = list(map(lambda x: x[3], inspect.stack()))
        # 改变元素选择器
        self.ui.atomic_num.setCurrentIndex(self.atom.num - 1)
        self.ui.atomic_name.setCurrentIndex(self.atom.num - 1)
        self.ui.atomic_symbol.setCurrentIndex(self.atom.num - 1)
        # 改变离化度列表
        self.ui.atomic_ion.clear()
        self.ui.atomic_ion.addItems([str(i) for i in range(self.atom.num)])
        self.ui.atomic_ion.setCurrentIndex(self.atom.ion)
        # 改变基组态
        self.ui.base_configuration.setText(self.atom.base_configuration)
        # 改变激发时的两个组态列表
        self.ui.low_configuration.clear()
        self.ui.low_configuration.addItems(list(self.atom.electron_arrangement.keys()))
        self.ui.high_configuration.clear()
        temp_list = []
        for value in SUBSHELL_SEQUENCE:
            if value not in self.atom.electron_arrangement:
                temp_list.append(value)
        self.ui.high_configuration.addItems(temp_list)
        # 清空组态卡的数据
        self.ui.in36_configuration_view.clear()
        self.ui.in36_configuration_view.setRowCount(0)
        self.ui.in36_configuration_view.setColumnCount(3)
        self.ui.in36_configuration_view.setHorizontalHeaderLabels(['宇称', '原子状态', '组态'])
        # 更新in36对象的属性
        if 'slot_atomic_num' in fun_name or 'slot_atomic_ion' in fun_name or 'slot_atomic_symbol' in fun_name or \
                'slot_atomic_name' in fun_name:
            self.in36.configuration_card = []
        self.in36.atomic_num = self.atom.num
        self.in36.atomic_ion = self.atom.ion

    def update_in36_obj_about(self):
        # 更新左侧输入区
        for i in range(23):
            eval(f'self.ui.in36_{i + 1}').setText(self.in36.control_card[i].strip(' '))
        # 更新组态
        df = pd.DataFrame(self.in36.configuration_card, columns=['原子序数', '原子状态', '标识符', '空格', '组态'],
                          index=list(range(1, len(self.in36.configuration_card) + 1)))
        df['宇称'] = self.in36.parity
        df = df[['宇称', '原子状态', '组态']]
        # 更新表格
        self.ui.in36_configuration_view.clear()
        self.ui.in36_configuration_view.setRowCount(df.shape[0])
        self.ui.in36_configuration_view.setColumnCount(df.shape[1])
        self.ui.in36_configuration_view.setHorizontalHeaderLabels(df.columns)
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.in36_configuration_view.setItem(i, j, item)

    def update_in2_obj_about(self):
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

    def update_exp_data_obj_about(self):
        self.ui.exp_web.load(QUrl.fromLocalFile(self.exp_data.plot_path))

    def update_run_obj_about(self):
        self.update_recorder_obj_about()

    def update_cal_data_obj_about(self):
        self.ui.web_cal_line.load(QUrl.fromLocalFile(self.cal_data.plot_path))

    def update_widen_obj_about(self):
        self.widen.plot_widen()
        if self.ui.crossP.isChecked():
            self.slot_crossp()
        elif self.ui.crossNP.isChecked():
            self.slot_crossnp()
        elif self.ui.gauss.isChecked():
            self.slot_gauss()

    def update_recorder_obj_about(self):
        # 更新历史记录
        self.ui.run_history_list.clear()
        for value in self.recorder.run_history:
            self.ui.run_history_list.addItem(QListWidgetItem(value))
        # 更新元素选择 第一页
        self.ui.selection_list.clear()
        for value in self.recorder.selection:
            self.ui.selection_list.addItem(QListWidgetItem(value))
        # 更新元素选择 第二页
        self.ui.page2_selection_list.clear()
        for value in self.recorder.selection:
            self.ui.page2_selection_list.addItem(QListWidgetItem(value))

    def update_spectra_add_obj_about(self):
        fun_name = list(map(lambda x: x[3], inspect.stack()))
        # 如果是网格计算，就不绘图
        if 'slot_page2_cal_grid' not in fun_name:
            self.ui.page2_add_spectrum_web.load(QUrl.fromLocalFile(self.spectra_add.plot_path))
        # 绘制网格计算相关的东西
        if self.spectra_add.grid_data:
            self.ui.page2_grid_web.load(QUrl.fromLocalFile(self.spectra_add.grid_path))
            # 设置表格
            self.ui.page2_grid_list.clear()
            self.ui.page2_grid_list.setRowCount(self.spectra_add.similarity.shape[0])
            self.ui.page2_grid_list.setColumnCount(self.spectra_add.similarity.shape[1])
            self.ui.page2_grid_list.setHorizontalHeaderLabels(self.spectra_add.similarity.columns)
            self.ui.page2_grid_list.setVerticalHeaderLabels(self.spectra_add.similarity.index[::-1])
            sim_max = self.spectra_add.similarity.values.flatten().max()
            for i in range(self.spectra_add.similarity.shape[0]):
                for j in range(self.spectra_add.similarity.shape[1]):
                    item = QTableWidgetItem('{:.4f}'.format(self.spectra_add.similarity.iloc[i, j], ))
                    item.setBackground(QBrush(
                        QColor(*rainbow_color(self.spectra_add.similarity.iloc[i, j] / sim_max))))
                    self.ui.page2_grid_list.setItem(self.spectra_add.similarity.shape[0] - i - 1, j, item)

    def update_first_page(self):
        pass

    def update_second_page(self):
        pass

    def load_project(self):
        obj_info = shelve.open(self.PROJECT_PATH.joinpath('.cowan/obj_info').as_posix())
        self.atom = obj_info['atom']
        self.cal_data = obj_info['cal_data']
        self.exp_data = obj_info['exp_data']
        self.in36 = obj_info['in36']
        self.in2 = obj_info['in2']
        self.cal_data = obj_info['cal_data']
        self.recorder = obj_info['recorder']
        self.run = obj_info['run']
        self.widen = obj_info['widen']
        obj_info.close()
        self.update_atom_obj_about()
        self.update_in36_obj_about()
        self.update_in2_obj_about()
        self.update_exp_data_obj_about()
        self.update_run_obj_about()
        self.update_cal_data_obj_about()
        self.update_widen_obj_about()
        self.update_recorder_obj_about()

    def closeEvent(self, event):
        self.slot_save_project()
        sys.exit()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.WORKING_PATH = Path.cwd()

        self.project_data: dict = {}
        self.temp_path: str = ''
        self.main_window: MainWindow | None = None

        self.init_UI()

    def init_UI(self):
        # 打开并读取文件
        file_path = self.WORKING_PATH / 'projects.json'
        self.project_data = json.loads(file_path.read_text())

        # 设置列表
        self.update_project_list()
        self.bind_slot()

    def bind_slot(self):
        self.ui.create_project.clicked.connect(self.slot_create_project)
        self.ui.delete_project.clicked.connect(self.slot_delete_project)
        self.ui.back.clicked.connect(self.slot_back)
        self.ui.new_project.clicked.connect(self.slot_new_project)
        self.ui.select_path.clicked.connect(self.slot_select_path)
        self.ui.project_path.textChanged.connect(self.slot_project_path_changed)
        self.ui.project_list.itemDoubleClicked.connect(self.slot_project_path_item_double_clicked)

    def slot_create_project(self):
        name = self.ui.project_name.text()
        path = self.ui.project_path.text()
        if name == '' or path == '':
            QMessageBox.critical(self, '错误', '项目名称和路径不能为空！')
            return
        if name in self.project_data.keys():
            QMessageBox.critical(self, '错误', '项目名称已存在！')
            return
        # 获取项目名称和路径
        path = path.replace('/', '\\')
        self.project_data[name] = {'path': path}
        self.update_project_list()

        # 如果目录不存在，就创建
        path = Path(path)
        old_path = self.WORKING_PATH / 'init_file'
        shutil.copytree(old_path, path)

        self.hide()
        self.main_window = MainWindow(path)
        self.main_window.show()

    def slot_delete_project(self):
        key = self.ui.project_list.currentIndex().data()
        path = Path(self.project_data[key]['path'])
        shutil.rmtree(path)
        self.project_data.pop(key)
        self.update_project_list()

    def slot_back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def slot_new_project(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def slot_select_path(self):
        self.temp_path = QFileDialog.getExistingDirectory(self, '选择项目路径', './')
        self.ui.project_path.setText(self.temp_path)

    def slot_project_path_changed(self):
        name = self.ui.project_path.text().split('/')[-1]
        if name == '':
            name = self.ui.project_path.text().split('/')[-2]
        self.ui.project_name.setText(name)

    def slot_project_path_item_double_clicked(self, index):
        name = index.text()
        path = self.project_data[name]['path']
        path = Path(path)
        self.hide()
        self.main_window = MainWindow(path, True)
        self.main_window.show()

    def update_project_list(self):
        self.ui.project_list.clear()
        self.ui.project_list.addItems(self.project_data.keys())

        # 写入json文件
        file_path = self.WORKING_PATH / 'projects.json'
        file_path.write_text(json.dumps(self.project_data), encoding='utf-8')


if __name__ == '__main__':
    app = QApplication([])
    window = LoginWindow()  # 启动登陆页面
    # window = MainWindow(Path('F:/Cowan/Al'), True)  # 启动主界面
    window.show()
    app.exec()
