# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'I3Demen7_remove1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1147, 673)
        icon = QIcon()
        icon.addFile(u"kyungwon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:rgba(16,30,41,240);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_17 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgba(255,255,255,255);\n"
"padding-top:2px;\n"
"padding-bottom:2px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)

        self.BOARD_LED_1 = QLabel(self.centralwidget)
        self.BOARD_LED_1.setObjectName(u"BOARD_LED_1")
        self.BOARD_LED_1.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_19.addWidget(self.BOARD_LED_1)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.DSP_LED_1 = QLabel(self.centralwidget)
        self.DSP_LED_1.setObjectName(u"DSP_LED_1")
        self.DSP_LED_1.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_18.addWidget(self.DSP_LED_1)


        self.horizontalLayout_21.addLayout(self.verticalLayout_18)


        self.verticalLayout_17.addLayout(self.horizontalLayout_21)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: Red;")

        self.verticalLayout_17.addWidget(self.label_7)


        self.horizontalLayout_20.addLayout(self.verticalLayout_17)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgba(255,255,255,255);\n"
"padding-top:2px;\n"
"padding-bottom:2px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_20)

        self.BOARD_LED_2 = QLabel(self.centralwidget)
        self.BOARD_LED_2.setObjectName(u"BOARD_LED_2")
        self.BOARD_LED_2.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_22.addWidget(self.BOARD_LED_2)


        self.horizontalLayout_22.addLayout(self.verticalLayout_22)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_21)

        self.DSP_LED_2 = QLabel(self.centralwidget)
        self.DSP_LED_2.setObjectName(u"DSP_LED_2")
        self.DSP_LED_2.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_21.addWidget(self.DSP_LED_2)


        self.horizontalLayout_22.addLayout(self.verticalLayout_21)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: Red;")

        self.verticalLayout_16.addWidget(self.label_9)


        self.horizontalLayout_20.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgba(255,255,255,255);\n"
"padding-top:2px;\n"
"padding-bottom:2px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_4)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_25)

        self.BOARD_LED_3 = QLabel(self.centralwidget)
        self.BOARD_LED_3.setObjectName(u"BOARD_LED_3")
        self.BOARD_LED_3.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_25.addWidget(self.BOARD_LED_3)


        self.horizontalLayout_23.addLayout(self.verticalLayout_25)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_26)

        self.DSP_LED_3 = QLabel(self.centralwidget)
        self.DSP_LED_3.setObjectName(u"DSP_LED_3")
        self.DSP_LED_3.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_24.addWidget(self.DSP_LED_3)


        self.horizontalLayout_23.addLayout(self.verticalLayout_24)


        self.verticalLayout_15.addLayout(self.horizontalLayout_23)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: Red;")

        self.verticalLayout_15.addWidget(self.label_10)


        self.horizontalLayout_20.addLayout(self.verticalLayout_15)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgba(255,255,255,255);\n"
"padding-top:2px;\n"
"padding-bottom:2px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_29)

        self.BOARD_LED_4 = QLabel(self.centralwidget)
        self.BOARD_LED_4.setObjectName(u"BOARD_LED_4")
        self.BOARD_LED_4.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_28.addWidget(self.BOARD_LED_4)


        self.horizontalLayout_24.addLayout(self.verticalLayout_28)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_30)

        self.DSP_LED_4 = QLabel(self.centralwidget)
        self.DSP_LED_4.setObjectName(u"DSP_LED_4")
        self.DSP_LED_4.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_27.addWidget(self.DSP_LED_4)


        self.horizontalLayout_24.addLayout(self.verticalLayout_27)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: Red;")

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_20.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgba(255,255,255,255);\n"
"padding-top:2px;\n"
"padding-bottom:2px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_34)

        self.BOARD_LED_5 = QLabel(self.centralwidget)
        self.BOARD_LED_5.setObjectName(u"BOARD_LED_5")
        self.BOARD_LED_5.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_31.addWidget(self.BOARD_LED_5)


        self.horizontalLayout_25.addLayout(self.verticalLayout_31)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_35)

        self.DSP_LED_5 = QLabel(self.centralwidget)
        self.DSP_LED_5.setObjectName(u"DSP_LED_5")
        self.DSP_LED_5.setStyleSheet(u"background-color: Lime;")

        self.verticalLayout_30.addWidget(self.DSP_LED_5)


        self.horizontalLayout_25.addLayout(self.verticalLayout_30)


        self.verticalLayout_11.addLayout(self.horizontalLayout_25)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: Red;")

        self.verticalLayout_11.addWidget(self.label_12)


        self.horizontalLayout_20.addLayout(self.verticalLayout_11)


        self.gridLayout.addLayout(self.horizontalLayout_20, 2, 1, 1, 2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.layoutWidget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(650, 0))
        self.tabWidget.setStyleSheet(u"QTabBar::tab{\n"
"background-color: rgb(97, 97, 97);\n"
"border-color: rgb(97, 97, 97);\n"
"min-height: 20px; \n"
"border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"padding : 2px 12px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-color: rgb(97, 97, 97);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:!selected{\n"
"	color: gray;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"	color: white;\n"
"	background-color: rgb(97, 97, 97);\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QTabWidget::pane{\n"
"border-width: 1px;\n"
"border-style : solid;\n"
"border-color :rgb(0, 0, 0);\n"
"}")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.splitter.addWidget(self.layoutWidget_2)
        self.layoutWidget_3 = QWidget(self.splitter)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_15.setContentsMargins(-1, 2, 2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);")

        self.horizontalLayout_13.addWidget(self.label_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.textBrowser = QTextBrowser(self.layoutWidget_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setStyleSheet(u"background-color:rgb(255,255,255);")

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.splitter.addWidget(self.layoutWidget_3)

        self.gridLayout.addWidget(self.splitter, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setMaximumSize(QSize(204, 16777215))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"color:white;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy4.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy4)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy5)
        self.pushButton_4.setMinimumSize(QSize(0, 25))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy6)
        self.label_28.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);")

        self.horizontalLayout_18.addWidget(self.label_28)

        self.comboBox_5 = QComboBox(self.groupBox_3)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.comboBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMaximumSize(QSize(204, 16777215))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"color:white;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.comboBox_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy7)
        self.pushButton_3.setMinimumSize(QSize(0, 25))
        self.pushButton_3.setBaseSize(QSize(0, 0))
        self.pushButton_3.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout_7.addWidget(self.label_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setMaximumSize(QSize(204, 16777215))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"color:white;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"	min-height:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_9)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-color: white;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)


        self.horizontalLayout_17.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.MessageBox = QMessageBox()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KW 3Dimension", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"STATION 1 ALERT LED", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"BOARD", None))
        self.BOARD_LED_1.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DSP", None))
        self.DSP_LED_1.setText("")
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"STATION 2 ALERT LED", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"BOARD", None))
        self.BOARD_LED_2.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"DSP", None))
        self.DSP_LED_2.setText("")
        self.label_9.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"STATION 3 ALERT LED", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"BOARD", None))
        self.BOARD_LED_3.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"DSP", None))
        self.DSP_LED_3.setText("")
        self.label_10.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"STATION 4 ALERT LED", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"BOARD", None))
        self.BOARD_LED_4.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"DSP", None))
        self.DSP_LED_4.setText("")
        self.label_11.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"STATION 5 ALERT LED", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"BOARD", None))
        self.BOARD_LED_5.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"DSP", None))
        self.DSP_LED_5.setText("")
        self.label_12.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"ALL", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data Log", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Schedule Control", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HOUR", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MINUTE", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INTERVAL", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"LOCATION SET", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Time Set", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"12 Order", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INFO STATE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Longtitude Latitude", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Distance Data Setting", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Menual Start", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Temperature and Depth", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Map", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">3\ucc28\uc6d0 \ud574\uc218\uc720\ub3d9 GUI</span></p></body></html>", None))
    # retranslateUi

