# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tp1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget
import pyqtgraph as pg
import time

class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [time.strftime("%H:%M:%S", time.localtime(local_time)) for local_time in values]


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(604, 441)
        icon = QIcon()
        icon.addFile(u"kyungwon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setStyleSheet(u"color: rgb(217, 145, 0);\n"
"background-color: rgb(209, 209, 209);\n"
"font: 20pt ;\n"
"font-weight:bold;\n"
"border-color : rgb(209, 209, 209);\n"
"alternate-background-color: rgb(255, 170, 0);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(3)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setStyleSheet(u"color: rgb(0, 170, 255);\n"
"background-color: rgb(209, 209, 209);\n"
"font: 20pt ;\n"
"font-weight:bold;\n"
"border-color : rgb(209, 209, 209);\n"
"alternate-background-color: rgb(255, 170, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(3)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(250, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 25))
        self.pushButton.setMaximumSize(QSize(40, 16777215))
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

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = PlotWidget(Dialog,axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"TEMPERATURE AND DEPTH", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"0\u2103", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"0m", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"SET", None))
    # retranslateUi

