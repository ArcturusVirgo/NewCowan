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
        MainWindow.resize(1197, 750)
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
        self.pushButton_13 = QPushButton(self.tab)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(85, 598, 100, 20))
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(14, 4, 178, 580))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.in36_text_1 = QLabel(self.widget)
        self.in36_text_1.setObjectName(u"in36_text_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in36_text_1.sizePolicy().hasHeightForWidth())
        self.in36_text_1.setSizePolicy(sizePolicy)
        self.in36_text_1.setMinimumSize(QSize(70, 0))
        self.in36_text_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_1, 0, 0, 1, 1)

        self.in36_1 = QLineEdit(self.widget)
        self.in36_1.setObjectName(u"in36_1")
        self.in36_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_1, 0, 1, 1, 1)

        self.in36_text_2 = QLabel(self.widget)
        self.in36_text_2.setObjectName(u"in36_text_2")
        sizePolicy.setHeightForWidth(self.in36_text_2.sizePolicy().hasHeightForWidth())
        self.in36_text_2.setSizePolicy(sizePolicy)
        self.in36_text_2.setMinimumSize(QSize(70, 0))
        self.in36_text_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_2, 1, 0, 1, 1)

        self.in36_2 = QLineEdit(self.widget)
        self.in36_2.setObjectName(u"in36_2")
        self.in36_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_2, 1, 1, 1, 1)

        self.in36_text_3 = QLabel(self.widget)
        self.in36_text_3.setObjectName(u"in36_text_3")
        sizePolicy.setHeightForWidth(self.in36_text_3.sizePolicy().hasHeightForWidth())
        self.in36_text_3.setSizePolicy(sizePolicy)
        self.in36_text_3.setMinimumSize(QSize(70, 0))
        self.in36_text_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_3, 2, 0, 1, 1)

        self.in36_3 = QLineEdit(self.widget)
        self.in36_3.setObjectName(u"in36_3")
        self.in36_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_3, 2, 1, 1, 1)

        self.in36_text_4 = QLabel(self.widget)
        self.in36_text_4.setObjectName(u"in36_text_4")
        sizePolicy.setHeightForWidth(self.in36_text_4.sizePolicy().hasHeightForWidth())
        self.in36_text_4.setSizePolicy(sizePolicy)
        self.in36_text_4.setMinimumSize(QSize(70, 0))
        self.in36_text_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_4, 3, 0, 1, 1)

        self.in36_4 = QLineEdit(self.widget)
        self.in36_4.setObjectName(u"in36_4")
        self.in36_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_4, 3, 1, 1, 1)

        self.in36_text_5 = QLabel(self.widget)
        self.in36_text_5.setObjectName(u"in36_text_5")
        sizePolicy.setHeightForWidth(self.in36_text_5.sizePolicy().hasHeightForWidth())
        self.in36_text_5.setSizePolicy(sizePolicy)
        self.in36_text_5.setMinimumSize(QSize(70, 0))
        self.in36_text_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_5, 4, 0, 1, 1)

        self.in36_5 = QLineEdit(self.widget)
        self.in36_5.setObjectName(u"in36_5")
        self.in36_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_5, 4, 1, 1, 1)

        self.in36_text_6 = QLabel(self.widget)
        self.in36_text_6.setObjectName(u"in36_text_6")
        sizePolicy.setHeightForWidth(self.in36_text_6.sizePolicy().hasHeightForWidth())
        self.in36_text_6.setSizePolicy(sizePolicy)
        self.in36_text_6.setMinimumSize(QSize(70, 0))
        self.in36_text_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_6, 5, 0, 1, 1)

        self.in36_6 = QLineEdit(self.widget)
        self.in36_6.setObjectName(u"in36_6")
        self.in36_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_6, 5, 1, 1, 1)

        self.in36_text_7 = QLabel(self.widget)
        self.in36_text_7.setObjectName(u"in36_text_7")
        sizePolicy.setHeightForWidth(self.in36_text_7.sizePolicy().hasHeightForWidth())
        self.in36_text_7.setSizePolicy(sizePolicy)
        self.in36_text_7.setMinimumSize(QSize(70, 0))
        self.in36_text_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_7, 6, 0, 1, 1)

        self.in36_7 = QLineEdit(self.widget)
        self.in36_7.setObjectName(u"in36_7")
        self.in36_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_7, 6, 1, 1, 1)

        self.in36_text_8 = QLabel(self.widget)
        self.in36_text_8.setObjectName(u"in36_text_8")
        sizePolicy.setHeightForWidth(self.in36_text_8.sizePolicy().hasHeightForWidth())
        self.in36_text_8.setSizePolicy(sizePolicy)
        self.in36_text_8.setMinimumSize(QSize(70, 0))
        self.in36_text_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_8, 7, 0, 1, 1)

        self.in36_8 = QLineEdit(self.widget)
        self.in36_8.setObjectName(u"in36_8")
        self.in36_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_8, 7, 1, 1, 1)

        self.in36_text_9 = QLabel(self.widget)
        self.in36_text_9.setObjectName(u"in36_text_9")
        sizePolicy.setHeightForWidth(self.in36_text_9.sizePolicy().hasHeightForWidth())
        self.in36_text_9.setSizePolicy(sizePolicy)
        self.in36_text_9.setMinimumSize(QSize(70, 0))
        self.in36_text_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_9, 8, 0, 1, 1)

        self.in36_9 = QLineEdit(self.widget)
        self.in36_9.setObjectName(u"in36_9")
        self.in36_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_9, 8, 1, 1, 1)

        self.in36_text_10 = QLabel(self.widget)
        self.in36_text_10.setObjectName(u"in36_text_10")
        sizePolicy.setHeightForWidth(self.in36_text_10.sizePolicy().hasHeightForWidth())
        self.in36_text_10.setSizePolicy(sizePolicy)
        self.in36_text_10.setMinimumSize(QSize(70, 0))
        self.in36_text_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_10, 9, 0, 1, 1)

        self.in36_10 = QLineEdit(self.widget)
        self.in36_10.setObjectName(u"in36_10")
        self.in36_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_10, 9, 1, 1, 1)

        self.in36_text_11 = QLabel(self.widget)
        self.in36_text_11.setObjectName(u"in36_text_11")
        sizePolicy.setHeightForWidth(self.in36_text_11.sizePolicy().hasHeightForWidth())
        self.in36_text_11.setSizePolicy(sizePolicy)
        self.in36_text_11.setMinimumSize(QSize(70, 0))
        self.in36_text_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_11, 10, 0, 1, 1)

        self.in36_11 = QLineEdit(self.widget)
        self.in36_11.setObjectName(u"in36_11")
        self.in36_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_11, 10, 1, 1, 1)

        self.in36_text_12 = QLabel(self.widget)
        self.in36_text_12.setObjectName(u"in36_text_12")
        sizePolicy.setHeightForWidth(self.in36_text_12.sizePolicy().hasHeightForWidth())
        self.in36_text_12.setSizePolicy(sizePolicy)
        self.in36_text_12.setMinimumSize(QSize(70, 0))
        self.in36_text_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_12, 11, 0, 1, 1)

        self.in36_12 = QLineEdit(self.widget)
        self.in36_12.setObjectName(u"in36_12")
        self.in36_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_12, 11, 1, 1, 1)

        self.in36_text_13 = QLabel(self.widget)
        self.in36_text_13.setObjectName(u"in36_text_13")
        sizePolicy.setHeightForWidth(self.in36_text_13.sizePolicy().hasHeightForWidth())
        self.in36_text_13.setSizePolicy(sizePolicy)
        self.in36_text_13.setMinimumSize(QSize(70, 0))
        self.in36_text_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_13, 12, 0, 1, 1)

        self.in36_13 = QLineEdit(self.widget)
        self.in36_13.setObjectName(u"in36_13")
        self.in36_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_13, 12, 1, 1, 1)

        self.in36_text_14 = QLabel(self.widget)
        self.in36_text_14.setObjectName(u"in36_text_14")
        sizePolicy.setHeightForWidth(self.in36_text_14.sizePolicy().hasHeightForWidth())
        self.in36_text_14.setSizePolicy(sizePolicy)
        self.in36_text_14.setMinimumSize(QSize(70, 0))
        self.in36_text_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_14, 13, 0, 1, 1)

        self.in36_14 = QLineEdit(self.widget)
        self.in36_14.setObjectName(u"in36_14")
        self.in36_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_14, 13, 1, 1, 1)

        self.in36_text_15 = QLabel(self.widget)
        self.in36_text_15.setObjectName(u"in36_text_15")
        sizePolicy.setHeightForWidth(self.in36_text_15.sizePolicy().hasHeightForWidth())
        self.in36_text_15.setSizePolicy(sizePolicy)
        self.in36_text_15.setMinimumSize(QSize(70, 0))
        self.in36_text_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_15, 14, 0, 1, 1)

        self.in36_15 = QLineEdit(self.widget)
        self.in36_15.setObjectName(u"in36_15")
        self.in36_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_15, 14, 1, 1, 1)

        self.in36_text_16 = QLabel(self.widget)
        self.in36_text_16.setObjectName(u"in36_text_16")
        sizePolicy.setHeightForWidth(self.in36_text_16.sizePolicy().hasHeightForWidth())
        self.in36_text_16.setSizePolicy(sizePolicy)
        self.in36_text_16.setMinimumSize(QSize(70, 0))
        self.in36_text_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_16, 15, 0, 1, 1)

        self.in36_16 = QLineEdit(self.widget)
        self.in36_16.setObjectName(u"in36_16")
        self.in36_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_16, 15, 1, 1, 1)

        self.in36_text_17 = QLabel(self.widget)
        self.in36_text_17.setObjectName(u"in36_text_17")
        sizePolicy.setHeightForWidth(self.in36_text_17.sizePolicy().hasHeightForWidth())
        self.in36_text_17.setSizePolicy(sizePolicy)
        self.in36_text_17.setMinimumSize(QSize(70, 0))
        self.in36_text_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_17, 16, 0, 1, 1)

        self.in36_17 = QLineEdit(self.widget)
        self.in36_17.setObjectName(u"in36_17")
        self.in36_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_17, 16, 1, 1, 1)

        self.in36_text_18 = QLabel(self.widget)
        self.in36_text_18.setObjectName(u"in36_text_18")
        sizePolicy.setHeightForWidth(self.in36_text_18.sizePolicy().hasHeightForWidth())
        self.in36_text_18.setSizePolicy(sizePolicy)
        self.in36_text_18.setMinimumSize(QSize(70, 0))
        self.in36_text_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_18, 17, 0, 1, 1)

        self.in36_18 = QLineEdit(self.widget)
        self.in36_18.setObjectName(u"in36_18")
        self.in36_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_18, 17, 1, 1, 1)

        self.in36_text_19 = QLabel(self.widget)
        self.in36_text_19.setObjectName(u"in36_text_19")
        sizePolicy.setHeightForWidth(self.in36_text_19.sizePolicy().hasHeightForWidth())
        self.in36_text_19.setSizePolicy(sizePolicy)
        self.in36_text_19.setMinimumSize(QSize(70, 0))
        self.in36_text_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_19, 18, 0, 1, 1)

        self.in36_19 = QLineEdit(self.widget)
        self.in36_19.setObjectName(u"in36_19")
        self.in36_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_19, 18, 1, 1, 1)

        self.in36_text_20 = QLabel(self.widget)
        self.in36_text_20.setObjectName(u"in36_text_20")
        sizePolicy.setHeightForWidth(self.in36_text_20.sizePolicy().hasHeightForWidth())
        self.in36_text_20.setSizePolicy(sizePolicy)
        self.in36_text_20.setMinimumSize(QSize(70, 0))
        self.in36_text_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_20, 19, 0, 1, 1)

        self.in36_20 = QLineEdit(self.widget)
        self.in36_20.setObjectName(u"in36_20")
        self.in36_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_20, 19, 1, 1, 1)

        self.in36_text_21 = QLabel(self.widget)
        self.in36_text_21.setObjectName(u"in36_text_21")
        sizePolicy.setHeightForWidth(self.in36_text_21.sizePolicy().hasHeightForWidth())
        self.in36_text_21.setSizePolicy(sizePolicy)
        self.in36_text_21.setMinimumSize(QSize(70, 0))
        self.in36_text_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_21, 20, 0, 1, 1)

        self.in36_21 = QLineEdit(self.widget)
        self.in36_21.setObjectName(u"in36_21")
        self.in36_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_21, 20, 1, 1, 1)

        self.in36_text_22 = QLabel(self.widget)
        self.in36_text_22.setObjectName(u"in36_text_22")
        sizePolicy.setHeightForWidth(self.in36_text_22.sizePolicy().hasHeightForWidth())
        self.in36_text_22.setSizePolicy(sizePolicy)
        self.in36_text_22.setMinimumSize(QSize(70, 0))
        self.in36_text_22.setAlignment(Qt.AlignCenter)
        self.in36_text_22.setWordWrap(False)
        self.in36_text_22.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_2.addWidget(self.in36_text_22, 21, 0, 1, 1)

        self.in36_22 = QLineEdit(self.widget)
        self.in36_22.setObjectName(u"in36_22")
        self.in36_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_22, 21, 1, 1, 1)

        self.in36_text_23 = QLabel(self.widget)
        self.in36_text_23.setObjectName(u"in36_text_23")
        sizePolicy.setHeightForWidth(self.in36_text_23.sizePolicy().hasHeightForWidth())
        self.in36_text_23.setSizePolicy(sizePolicy)
        self.in36_text_23.setMinimumSize(QSize(70, 0))
        self.in36_text_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_text_23, 22, 0, 1, 1)

        self.in36_23 = QLineEdit(self.widget)
        self.in36_23.setObjectName(u"in36_23")
        self.in36_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.in36_23, 22, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(113, 582, 75, 24))
        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(9, 6, 182, 563))
        self.gridLayout_3 = QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.in2_text_1 = QLabel(self.widget1)
        self.in2_text_1.setObjectName(u"in2_text_1")
        self.in2_text_1.setMinimumSize(QSize(100, 0))
        self.in2_text_1.setMaximumSize(QSize(120, 16777215))
        self.in2_text_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_1, 0, 0, 1, 1)

        self.in2_1 = QLineEdit(self.widget1)
        self.in2_1.setObjectName(u"in2_1")
        self.in2_1.setMinimumSize(QSize(0, 0))
        self.in2_1.setMaximumSize(QSize(100, 30))
        self.in2_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_1, 0, 1, 1, 1)

        self.in2_text_2 = QLabel(self.widget1)
        self.in2_text_2.setObjectName(u"in2_text_2")
        self.in2_text_2.setMinimumSize(QSize(100, 0))
        self.in2_text_2.setMaximumSize(QSize(120, 16777215))
        self.in2_text_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_2, 1, 0, 1, 1)

        self.in2_2 = QLineEdit(self.widget1)
        self.in2_2.setObjectName(u"in2_2")
        self.in2_2.setMinimumSize(QSize(0, 0))
        self.in2_2.setMaximumSize(QSize(100, 30))
        self.in2_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_2, 1, 1, 1, 1)

        self.in2_text_3 = QLabel(self.widget1)
        self.in2_text_3.setObjectName(u"in2_text_3")
        self.in2_text_3.setMinimumSize(QSize(100, 0))
        self.in2_text_3.setMaximumSize(QSize(120, 16777215))
        self.in2_text_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_3, 2, 0, 1, 1)

        self.in2_3 = QLineEdit(self.widget1)
        self.in2_3.setObjectName(u"in2_3")
        self.in2_3.setMinimumSize(QSize(0, 0))
        self.in2_3.setMaximumSize(QSize(100, 30))
        self.in2_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_3, 2, 1, 1, 1)

        self.in2_text_4 = QLabel(self.widget1)
        self.in2_text_4.setObjectName(u"in2_text_4")
        self.in2_text_4.setMinimumSize(QSize(100, 0))
        self.in2_text_4.setMaximumSize(QSize(120, 16777215))
        self.in2_text_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_4, 3, 0, 1, 1)

        self.in2_4 = QLineEdit(self.widget1)
        self.in2_4.setObjectName(u"in2_4")
        self.in2_4.setMinimumSize(QSize(0, 0))
        self.in2_4.setMaximumSize(QSize(100, 30))
        self.in2_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_4, 3, 1, 1, 1)

        self.in2_text_5 = QLabel(self.widget1)
        self.in2_text_5.setObjectName(u"in2_text_5")
        self.in2_text_5.setMinimumSize(QSize(100, 0))
        self.in2_text_5.setMaximumSize(QSize(120, 16777215))
        self.in2_text_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_5, 4, 0, 1, 1)

        self.in2_5 = QLineEdit(self.widget1)
        self.in2_5.setObjectName(u"in2_5")
        self.in2_5.setMinimumSize(QSize(0, 0))
        self.in2_5.setMaximumSize(QSize(100, 30))
        self.in2_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_5, 4, 1, 1, 1)

        self.in2_text_6 = QLabel(self.widget1)
        self.in2_text_6.setObjectName(u"in2_text_6")
        self.in2_text_6.setMinimumSize(QSize(100, 0))
        self.in2_text_6.setMaximumSize(QSize(120, 16777215))
        self.in2_text_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_6, 5, 0, 1, 1)

        self.in2_6 = QLineEdit(self.widget1)
        self.in2_6.setObjectName(u"in2_6")
        self.in2_6.setMinimumSize(QSize(0, 0))
        self.in2_6.setMaximumSize(QSize(100, 30))
        self.in2_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_6, 5, 1, 1, 1)

        self.in2_text_7 = QLabel(self.widget1)
        self.in2_text_7.setObjectName(u"in2_text_7")
        self.in2_text_7.setMinimumSize(QSize(100, 0))
        self.in2_text_7.setMaximumSize(QSize(120, 16777215))
        self.in2_text_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_7, 6, 0, 1, 1)

        self.in2_7 = QLineEdit(self.widget1)
        self.in2_7.setObjectName(u"in2_7")
        self.in2_7.setMinimumSize(QSize(0, 0))
        self.in2_7.setMaximumSize(QSize(100, 30))
        self.in2_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_7, 6, 1, 1, 1)

        self.in2_text_8 = QLabel(self.widget1)
        self.in2_text_8.setObjectName(u"in2_text_8")
        self.in2_text_8.setMinimumSize(QSize(100, 0))
        self.in2_text_8.setMaximumSize(QSize(120, 16777215))
        self.in2_text_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_8, 7, 0, 1, 1)

        self.in2_8 = QLineEdit(self.widget1)
        self.in2_8.setObjectName(u"in2_8")
        self.in2_8.setMinimumSize(QSize(0, 0))
        self.in2_8.setMaximumSize(QSize(100, 30))
        self.in2_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_8, 7, 1, 1, 1)

        self.in2_text_9 = QLabel(self.widget1)
        self.in2_text_9.setObjectName(u"in2_text_9")
        self.in2_text_9.setMinimumSize(QSize(80, 0))
        self.in2_text_9.setMaximumSize(QSize(120, 16777215))
        self.in2_text_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_9, 8, 0, 1, 1)

        self.in2_9_a = QLineEdit(self.widget1)
        self.in2_9_a.setObjectName(u"in2_9_a")
        self.in2_9_a.setMaximumSize(QSize(100, 30))
        self.in2_9_a.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_9_a, 8, 1, 1, 1)

        self.in2_9_b = QLineEdit(self.widget1)
        self.in2_9_b.setObjectName(u"in2_9_b")
        self.in2_9_b.setMaximumSize(QSize(100, 30))
        self.in2_9_b.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_9_b, 9, 1, 1, 1)

        self.in2_9_c = QLineEdit(self.widget1)
        self.in2_9_c.setObjectName(u"in2_9_c")
        self.in2_9_c.setMaximumSize(QSize(100, 30))
        self.in2_9_c.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_9_c, 10, 1, 1, 1)

        self.in2_9_d = QLineEdit(self.widget1)
        self.in2_9_d.setObjectName(u"in2_9_d")
        self.in2_9_d.setMaximumSize(QSize(100, 30))
        self.in2_9_d.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_9_d, 11, 1, 1, 1)

        self.in2_text_10 = QLabel(self.widget1)
        self.in2_text_10.setObjectName(u"in2_text_10")
        self.in2_text_10.setMinimumSize(QSize(100, 0))
        self.in2_text_10.setMaximumSize(QSize(120, 16777215))
        self.in2_text_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_10, 12, 0, 1, 1)

        self.in2_10 = QLineEdit(self.widget1)
        self.in2_10.setObjectName(u"in2_10")
        self.in2_10.setMinimumSize(QSize(0, 0))
        self.in2_10.setMaximumSize(QSize(100, 30))
        self.in2_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_10, 12, 1, 1, 1)

        self.in2_text_12 = QLabel(self.widget1)
        self.in2_text_12.setObjectName(u"in2_text_12")
        self.in2_text_12.setMinimumSize(QSize(100, 0))
        self.in2_text_12.setMaximumSize(QSize(120, 16777215))
        self.in2_text_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_12, 13, 0, 1, 1)

        self.in2_12 = QLineEdit(self.widget1)
        self.in2_12.setObjectName(u"in2_12")
        self.in2_12.setMinimumSize(QSize(0, 0))
        self.in2_12.setMaximumSize(QSize(100, 30))
        self.in2_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_12, 13, 1, 1, 1)

        self.in2_text_13 = QLabel(self.widget1)
        self.in2_text_13.setObjectName(u"in2_text_13")
        self.in2_text_13.setMinimumSize(QSize(100, 0))
        self.in2_text_13.setMaximumSize(QSize(120, 16777215))
        self.in2_text_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_13, 14, 0, 1, 1)

        self.in2_13 = QLineEdit(self.widget1)
        self.in2_13.setObjectName(u"in2_13")
        self.in2_13.setMinimumSize(QSize(0, 0))
        self.in2_13.setMaximumSize(QSize(100, 30))
        self.in2_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_13, 14, 1, 1, 1)

        self.in2_text_14 = QLabel(self.widget1)
        self.in2_text_14.setObjectName(u"in2_text_14")
        self.in2_text_14.setMinimumSize(QSize(100, 0))
        self.in2_text_14.setMaximumSize(QSize(120, 16777215))
        self.in2_text_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_14, 15, 0, 1, 1)

        self.in2_14 = QLineEdit(self.widget1)
        self.in2_14.setObjectName(u"in2_14")
        self.in2_14.setMinimumSize(QSize(0, 0))
        self.in2_14.setMaximumSize(QSize(100, 30))
        self.in2_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_14, 15, 1, 1, 1)

        self.in2_text_15 = QLabel(self.widget1)
        self.in2_text_15.setObjectName(u"in2_text_15")
        self.in2_text_15.setMinimumSize(QSize(100, 0))
        self.in2_text_15.setMaximumSize(QSize(120, 16777215))
        self.in2_text_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_15, 16, 0, 1, 1)

        self.in2_15 = QLineEdit(self.widget1)
        self.in2_15.setObjectName(u"in2_15")
        self.in2_15.setMinimumSize(QSize(0, 0))
        self.in2_15.setMaximumSize(QSize(100, 30))
        self.in2_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_15, 16, 1, 1, 1)

        self.in2_text_16 = QLabel(self.widget1)
        self.in2_text_16.setObjectName(u"in2_text_16")
        self.in2_text_16.setMinimumSize(QSize(100, 0))
        self.in2_text_16.setMaximumSize(QSize(120, 16777215))
        self.in2_text_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_16, 17, 0, 1, 1)

        self.in2_16 = QLineEdit(self.widget1)
        self.in2_16.setObjectName(u"in2_16")
        self.in2_16.setMinimumSize(QSize(0, 0))
        self.in2_16.setMaximumSize(QSize(100, 30))
        self.in2_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_16, 17, 1, 1, 1)

        self.in2_text_17 = QLabel(self.widget1)
        self.in2_text_17.setObjectName(u"in2_text_17")
        self.in2_text_17.setMinimumSize(QSize(100, 0))
        self.in2_text_17.setMaximumSize(QSize(120, 16777215))
        self.in2_text_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_17, 18, 0, 1, 1)

        self.in2_17 = QLineEdit(self.widget1)
        self.in2_17.setObjectName(u"in2_17")
        self.in2_17.setMinimumSize(QSize(0, 0))
        self.in2_17.setMaximumSize(QSize(100, 30))
        self.in2_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_17, 18, 1, 1, 1)

        self.in2_text_18 = QLabel(self.widget1)
        self.in2_text_18.setObjectName(u"in2_text_18")
        self.in2_text_18.setMinimumSize(QSize(100, 0))
        self.in2_text_18.setMaximumSize(QSize(120, 16777215))
        self.in2_text_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_18, 19, 0, 1, 1)

        self.in2_18 = QLineEdit(self.widget1)
        self.in2_18.setObjectName(u"in2_18")
        self.in2_18.setMinimumSize(QSize(0, 0))
        self.in2_18.setMaximumSize(QSize(100, 30))
        self.in2_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_18, 19, 1, 1, 1)

        self.in2_text_19 = QLabel(self.widget1)
        self.in2_text_19.setObjectName(u"in2_text_19")
        self.in2_text_19.setMinimumSize(QSize(100, 0))
        self.in2_text_19.setMaximumSize(QSize(120, 16777215))
        self.in2_text_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_text_19, 20, 0, 1, 1)

        self.in2_19 = QLineEdit(self.widget1)
        self.in2_19.setObjectName(u"in2_19")
        self.in2_19.setMinimumSize(QSize(0, 0))
        self.in2_19.setMaximumSize(QSize(100, 30))
        self.in2_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.in2_19, 20, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.widget2 = QWidget(self.page)
        self.widget2.setObjectName(u"widget2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy1)
        self.widget2.setMinimumSize(QSize(500, 0))
        self.widget2.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.widget2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_10 = QPushButton(self.widget2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_10.addWidget(self.pushButton_11)

        self.pushButton_3 = QPushButton(self.widget2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_10.addWidget(self.pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.pushButton_12 = QPushButton(self.widget2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_10.addWidget(self.pushButton_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line = QFrame(self.widget2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.widget2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy4)
        self.comboBox.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widget2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy5)
        self.comboBox_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.widget2)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.widget2)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy3.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy3)
        self.comboBox_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.comboBox_4, 1, 3, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.horizontalSpacer_4 = QSpacerItem(32, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_2 = QFrame(self.widget2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.comboBox_7 = QComboBox(self.widget2)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.comboBox_7)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_14 = QLabel(self.widget2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.spinBox = QSpinBox(self.widget2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.widget2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.widget2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.widget2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(99)
        self.spinBox_4.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_4)

        self.spinBox_5 = QSpinBox(self.widget2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setValue(85)

        self.horizontalLayout_4.addWidget(self.spinBox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.widget2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.comboBox_5 = QComboBox(self.widget2)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(50, 0))
        self.comboBox_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.widget2)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(50, 0))
        self.comboBox_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_6)

        self.radioButton_3 = QRadioButton(self.widget2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_5.addWidget(self.radioButton_4)

        self.lineEdit = QLineEdit(self.widget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.widget2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.line_4 = QFrame(self.widget2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.progressBar = QProgressBar(self.widget2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_6.addWidget(self.progressBar)

        self.pushButton_5 = QPushButton(self.widget2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.line_5 = QFrame(self.widget2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listView = QListView(self.widget2)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_7.addWidget(self.listView)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.widget2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_4 = QPushButton(self.widget2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4, 0, Qt.AlignBottom)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_2.addWidget(self.widget2)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.label)

        self.webEngineView = QWebEngineView(self.widget_2)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy6)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.webEngineView_2 = QWebEngineView(self.widget_2)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        sizePolicy6.setHeightForWidth(self.webEngineView_2.sizePolicy().hasHeightForWidth())
        self.webEngineView_2.setSizePolicy(sizePolicy6)
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.webEngineView_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy7)
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.webEngineView_3 = QWebEngineView(self.widget_2)
        self.webEngineView_3.setObjectName(u"webEngineView_3")
        sizePolicy6.setHeightForWidth(self.webEngineView_3.sizePolicy().hasHeightForWidth())
        self.webEngineView_3.setSizePolicy(sizePolicy6)
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

        self.tabWidget.setCurrentIndex(1)


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
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
#if QT_CONFIG(tooltip)
        self.in36_text_1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.in36_text_1.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.in36_text_1.setText(QCoreApplication.translate("MainWindow", u"ITPOW", None))
        self.in36_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in36_text_2.setText(QCoreApplication.translate("MainWindow", u"IPTVU", None))
        self.in36_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in36_text_3.setText(QCoreApplication.translate("MainWindow", u"IPTEB", None))
        self.in36_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
#if QT_CONFIG(tooltip)
        self.in36_text_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&lt; 0\uff0c<span style=\" font-family:'\u5b8b\u4f53';\">\u4e0d\u6253\u5370\u6ce2\u51fd\u6570</span></p><p>&gt;0<span style=\" font-family:'\u5b8b\u4f53';\">\uff0c\u5728\u6bcf\u7b2c\u4e94\u4e2a\u7f51\u683c\u70b9\u6253\u5370\u524d\u4e24\u4e2a\u548c\u6700\u540e\u4e00\u4e2a</span> NORBPT <span style=\" font-family:'\u5b8b\u4f53';\">\u6ce2\u51fd\u6570</span></p><p>&gt;5<span style=\" font-family:'\u5b8b\u4f53';\">\uff0c\u5728\u6bcf\u4e2a\u7f51\u683c\u70b9\u6253\u5370\u8fde\u7eed\u6ce2\u51fd\u6570</span></p><p>=-9<span style=\" font-family:'\u5b8b\u4f53';\">\uff0c\u8f93\u51fa\u6240\u6709\u6ce2\u51fd\u6570</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.in36_text_4.setText(QCoreApplication.translate("MainWindow", u"NORBPT", None))
#if QT_CONFIG(tooltip)
        self.in36_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">|NORBPT &lt; 0| ==&gt; \u4e0d\u6253\u5370\u6ce2\u51fd\u6570</span></p><p><span style=\" font-size:12pt;\">|NORBPT &gt; 0| ==&gt; \u5728\u6bcf\u7b2c\u4e94\u4e2a\u7f51\u683c\u70b9\u6253\u5370\u524d\u4e24\u4e2a\u548c\u6700\u540e\u4e00\u4e2a -NORBPT- \u6ce2\u51fd\u6570</span></p><p><span style=\" font-size:12pt;\">|NORBPT &gt; 5| ==&gt; \u5728\u6bcf\u4e2a\u7f51\u683c\u70b9\u6253\u5370\u8fde\u7eed\u4ecb\u8d28\u6ce2\u51fd\u6570\uff0c\u5728tape2 \u6216 tape7\u4e0a\u5199\u5165\u6700\u540e\u7684 -NORBPT- \u4e2a\u6ce2\u51fd\u6570\uff08\u81f3\u5c11\u4e3a2\uff1b\u5982\u679c -NORBPT- = 9\uff0c\u5199\u5165\u6240\u6709\u6ce2\u51fd\u6570\uff09</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.in36_4.setText(QCoreApplication.translate("MainWindow", u"-9", None))
        self.in36_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_5.setText(QCoreApplication.translate("MainWindow", u"IZHXBW", None))
        self.in36_5.setText("")
        self.in36_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in36_text_6.setText(QCoreApplication.translate("MainWindow", u"IPHFWF", None))
        self.in36_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_7.setText(QCoreApplication.translate("MainWindow", u"IHF", None))
        self.in36_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.in36_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_8.setText(QCoreApplication.translate("MainWindow", u"IBB", None))
        self.in36_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I3", None))
        self.in36_text_9.setText(QCoreApplication.translate("MainWindow", u"TOLSTB", None))
        self.in36_9.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.in36_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F2.1", None))
        self.in36_text_10.setText(QCoreApplication.translate("MainWindow", u"TOLKM2", None))
        self.in36_10.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.in36_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E5.1", None))
        self.in36_text_11.setText(QCoreApplication.translate("MainWindow", u"TOLEND", None))
        self.in36_11.setText(QCoreApplication.translate("MainWindow", u"5.e-08", None))
        self.in36_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E10.1", None))
        self.in36_text_12.setText(QCoreApplication.translate("MainWindow", u"THRESH", None))
        self.in36_12.setText(QCoreApplication.translate("MainWindow", u"1.e-11", None))
        self.in36_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E10.1", None))
        self.in36_text_13.setText(QCoreApplication.translate("MainWindow", u"KUTD", None))
#if QT_CONFIG(tooltip)
        self.in36_13.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.in36_13.setText(QCoreApplication.translate("MainWindow", u"-2", None))
        self.in36_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_14.setText(QCoreApplication.translate("MainWindow", u"KUT1", None))
        self.in36_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_15.setText(QCoreApplication.translate("MainWindow", u"IVINTI", None))
        self.in36_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in36_text_16.setText(QCoreApplication.translate("MainWindow", u"IRELb", None))
        self.in36_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.in36_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in36_text_17.setText(QCoreApplication.translate("MainWindow", u"MAXIT", None))
        self.in36_17.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.in36_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_18.setText(QCoreApplication.translate("MainWindow", u"NPR", None))
        self.in36_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in36_text_19.setText(QCoreApplication.translate("MainWindow", u"EXF10", None))
        self.in36_19.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.in36_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F5.5", None))
        self.in36_text_20.setText(QCoreApplication.translate("MainWindow", u"EXFM1", None))
        self.in36_20.setText(QCoreApplication.translate("MainWindow", u"0.65", None))
        self.in36_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F5.5", None))
        self.in36_text_21.setText(QCoreApplication.translate("MainWindow", u"EMXc", None))
        self.in36_21.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.in36_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F5.5", None))
        self.in36_text_22.setText(QCoreApplication.translate("MainWindow", u"CORRFd", None))
        self.in36_22.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.in36_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F5.5", None))
        self.in36_text_23.setText(QCoreApplication.translate("MainWindow", u"IW6e", None))
        self.in36_23.setText("")
        self.in36_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"in36\u7f16\u8f91", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.in2_text_1.setText(QCoreApplication.translate("MainWindow", u"\u5b50\u7a0b\u5e8f", None))
        self.in2_1.setText(QCoreApplication.translate("MainWindow", u"g5inp", None))
        self.in2_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A3,2X", None))
        self.in2_text_2.setText(QCoreApplication.translate("MainWindow", u"NCK", None))
        self.in2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.in2_text_3.setText(QCoreApplication.translate("MainWindow", u"IOVF ACT", None))
        self.in2_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.in2_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_4.setText(QCoreApplication.translate("MainWindow", u"NOCET ", None))
        self.in2_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.in2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in2_text_5.setText(QCoreApplication.translate("MainWindow", u"NSCONF(3,1)", None))
        self.in2_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.in2_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_6.setText(QCoreApplication.translate("MainWindow", u"NSCONF(3,2) ", None))
        self.in2_6.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.in2_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.in2_text_7.setText(QCoreApplication.translate("MainWindow", u"EA V11 ", None))
        self.in2_7.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.in2_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F7.4", None))
        self.in2_text_8.setText(QCoreApplication.translate("MainWindow", u"IABG ", None))
        self.in2_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_9.setText(QCoreApplication.translate("MainWindow", u"OPTION", None))
        self.in2_9_a.setText(QCoreApplication.translate("MainWindow", u"00000000", None))
        self.in2_9_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A8", None))
        self.in2_9_b.setText(QCoreApplication.translate("MainWindow", u"0000000", None))
        self.in2_9_b.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A8", None))
        self.in2_9_c.setText(QCoreApplication.translate("MainWindow", u"00000", None))
        self.in2_9_c.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A8", None))
        self.in2_9_d.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.in2_9_d.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.in2_text_10.setText(QCoreApplication.translate("MainWindow", u"IQUAD", None))
        self.in2_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.in2_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_12.setText(QCoreApplication.translate("MainWindow", u"DMIN ", None))
        self.in2_12.setText(QCoreApplication.translate("MainWindow", u".0000", None))
        self.in2_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A5", None))
        self.in2_text_13.setText(QCoreApplication.translate("MainWindow", u"IPRINT", None))
        self.in2_13.setText("")
        self.in2_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A5", None))
        self.in2_text_14.setText(QCoreApplication.translate("MainWindow", u"IENGYD", None))
        self.in2_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.in2_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.in2_text_15.setText(QCoreApplication.translate("MainWindow", u"ISPECC", None))
        self.in2_15.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.in2_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.in2_text_16.setText(QCoreApplication.translate("MainWindow", u"ICON", None))
        self.in2_16.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.in2_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_17.setText(QCoreApplication.translate("MainWindow", u"ISLI", None))
        self.in2_17.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.in2_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_18.setText(QCoreApplication.translate("MainWindow", u"IDIP", None))
        self.in2_18.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.in2_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.in2_text_19.setText(QCoreApplication.translate("MainWindow", u"ALF", None))
        self.in2_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"F5.0", None))
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

