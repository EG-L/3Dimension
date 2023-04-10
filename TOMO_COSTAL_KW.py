# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'I3Demen7_remove.ui'
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
        MainWindow.resize(1147, 644)
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
        self.comboBox_5.addItem("")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"ALL", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data Log", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Schedule Control", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HOUR", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MINUTE", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INTERVAL", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"LOCATION SET", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Time Set", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"8 Order", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"10 Order", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"12 Order", None))

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

