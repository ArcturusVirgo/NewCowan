# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 740)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action.setPriority(QAction.NormalPriority)
        self.actionjiazai = QAction(MainWindow)
        self.actionjiazai.setObjectName(u"actionjiazai")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(818, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(200, 0))
        self.tabWidget.setMaximumSize(QSize(200, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 0))
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_10.addWidget(self.pushButton_11)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_10.addWidget(self.pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_10.addWidget(self.pushButton_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy4)
        self.comboBox_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.widget)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)
        self.comboBox_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_4, 1, 3, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.horizontalSpacer_4 = QSpacerItem(32, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.comboBox_7 = QComboBox(self.widget)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.comboBox_7)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.widget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.widget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.widget)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(99)
        self.spinBox_4.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_4)

        self.spinBox_5 = QSpinBox(self.widget)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.comboBox_5 = QComboBox(self.widget)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.widget)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_6)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_5.addWidget(self.radioButton_4)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_6.addWidget(self.progressBar)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_7.addWidget(self.listView)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label)

        self.webEngineView = QWebEngineView(self.widget_2)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy5)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.webEngineView_2 = QWebEngineView(self.widget_2)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        sizePolicy5.setHeightForWidth(self.webEngineView_2.sizePolicy().hasHeightForWidth())
        self.webEngineView_2.setSizePolicy(sizePolicy5)
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy6)
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.webEngineView_3 = QWebEngineView(self.widget_2)
        self.webEngineView_3.setObjectName(u"webEngineView_3")
        sizePolicy5.setHeightForWidth(self.webEngineView_3.sizePolicy().hasHeightForWidth())
        self.webEngineView_3.setSizePolicy(sizePolicy5)
        self.webEngineView_3.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView_3)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(2, 4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1197, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionjiazai.setText(QCoreApplication.translate("MainWindow", u"jiazai ", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u9879\u76ee", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u5b9e\u9a8c\u6570\u636e", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4e3a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"in36\u7f16\u8f91", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"in2\u7f16\u8f91", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u79fb", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u79fb", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6392\u5e8f", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u6570", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7b26\u53f7", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u5316\u5ea6", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"100", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5609*", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"GG+", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"99+", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7ec4\u6001", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1s02 2s02 2p01", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8026\u5408\u65b9\u5f0f", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"L-S", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"j-j", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u65af\u83b1\u7279\u7cfb\u6570", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u652f\u58f3\u5c42", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"4f", None))

        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.lineEdit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u7ec4\u6001", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u8ba1\u7b97....", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c\u8c31", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u8c31", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f6e\u5ed3", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"cross-P", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"cross-NP", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
    # retranslateUi

