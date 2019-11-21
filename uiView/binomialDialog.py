# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'binomialDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QDoubleValidator

from uiView.utils import load_style, button_style


class BinomialDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1081, 780)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 731, 741))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(766, 66, 263, 615))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_n = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_n.setFont(font)
        self.label_n.setObjectName("label_n")
        self.horizontalLayout.addWidget(self.label_n)
        spacerItem = QtWidgets.QSpacerItem(13, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_n = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_n.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.horizontalLayout.addWidget(self.lineEdit_n)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(100, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_p = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_p.setFont(font)
        self.label_p.setObjectName("label_p")
        self.horizontalLayout_2.addWidget(self.label_p)
        spacerItem2 = QtWidgets.QSpacerItem(13, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEdit_p = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_p.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.horizontalLayout_2.addWidget(self.lineEdit_p)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(232, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_style = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_style.setFont(font)
        self.label_style.setObjectName("label_style")
        self.horizontalLayout_4.addWidget(self.label_style)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.comboBox_style = QtWidgets.QComboBox(self.widget)
        self.comboBox_style.setObjectName("comboBox_style")
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_style)
        spacerItem6 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(251, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_area = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_area.setFont(font)
        self.label_area.setObjectName("label_area")
        self.horizontalLayout_5.addWidget(self.label_area)
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.comboBox_area = QtWidgets.QComboBox(self.widget)
        self.comboBox_area.setObjectName("comboBox_area")
        self.comboBox_area.addItem("")
        self.comboBox_area.addItem("")
        self.comboBox_area.addItem("")
        self.comboBox_area.addItem("")
        self.comboBox_area.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_area)
        spacerItem9 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_a = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_a.setFont(font)
        self.label_a.setObjectName("label_a")
        self.horizontalLayout_6.addWidget(self.label_a)
        spacerItem11 = QtWidgets.QSpacerItem(13, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.lineEdit_a = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_a.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.horizontalLayout_6.addWidget(self.lineEdit_a)
        spacerItem12 = QtWidgets.QSpacerItem(13, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.label_b = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_b.setFont(font)
        self.label_b.setObjectName("label_b")
        self.horizontalLayout_6.addWidget(self.label_b)
        spacerItem13 = QtWidgets.QSpacerItem(13, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.lineEdit_b = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_b.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.horizontalLayout_6.addWidget(self.lineEdit_b)
        spacerItem14 = QtWidgets.QSpacerItem(13, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(234, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem15)
        self.label_area_result = QtWidgets.QLabel(self.widget)
        self.label_area_result.setText("")
        self.label_area_result.setObjectName("label_area_result")
        self.verticalLayout_7.addWidget(self.label_area_result)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem16 = QtWidgets.QSpacerItem(259, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_point = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_point.setFont(font)
        self.label_point.setObjectName("label_point")
        self.horizontalLayout_10.addWidget(self.label_point)
        spacerItem17 = QtWidgets.QSpacerItem(13, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.lineEdit_point = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_point.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_point.setObjectName("lineEdit_point")
        self.horizontalLayout_10.addWidget(self.lineEdit_point)
        spacerItem18 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        spacerItem19 = QtWidgets.QSpacerItem(261, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem19)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem20 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.pushButton_drawing = QtWidgets.QPushButton(self.widget)
        self.pushButton_drawing.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_drawing.setObjectName("pushButton_drawing")
        self.horizontalLayout_7.addWidget(self.pushButton_drawing)
        spacerItem21 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem22 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem22)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem23 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_8.addWidget(self.pushButton_clear)
        spacerItem24 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem24)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem25 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem25)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem26 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem26)
        self.pushButton_return = QtWidgets.QPushButton(self.widget)
        self.pushButton_return.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_return.setObjectName("pushButton_return")
        self.horizontalLayout_9.addWidget(self.pushButton_return)
        spacerItem27 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem27)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        nIntvalidator = QIntValidator(self)
        nIntvalidator.setRange(0, 99999)
        self.lineEdit_n.setValidator(nIntvalidator)
        self.lineEdit_b.setValidator(nIntvalidator)
        self.lineEdit_a.setValidator(nIntvalidator)
        self.lineEdit_point.setValidator(nIntvalidator)

        rx = QRegExp("^[0-1]{1}([.]([0-9]){2})?$")
        pRegExpValidator = QRegExpValidator(rx)
        self.lineEdit_p.setValidator(pRegExpValidator)

        pDoublevalidator = QDoubleValidator(self)
        pDoublevalidator.setRange(-99999, 99999)
        pDoublevalidator.setNotation(QDoubleValidator.StandardNotation)
        pDoublevalidator.setDecimals(2)
        self.lineEdit_a.setValidator(pDoublevalidator)
        self.lineEdit_b.setValidator(pDoublevalidator)

        self.label_a.setHidden(True)
        self.label_b.setHidden(True)
        self.lineEdit_a.setHidden(True)
        self.lineEdit_b.setHidden(True)
        self.label_area.setHidden(True)
        self.comboBox_area.setHidden(True)
        self.label_point.setHidden(True)
        self.lineEdit_point.setHidden(True)

        load_style(self.pushButton_drawing)
        button_style(self.pushButton_drawing, "DarkGray")
        load_style(self.pushButton_return)
        button_style(self.pushButton_return, "BlueJeans")
        load_style(self.pushButton_clear)
        button_style(self.pushButton_clear, "Mint")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Graph"))
        self.label_n.setText(_translate("Dialog", "n"))
        self.label_p.setText(_translate("Dialog", "p"))
        self.label_style.setText(_translate("Dialog", "Style"))
        self.comboBox_style.setItemText(0, _translate("Dialog", "pdf"))
        self.comboBox_style.setItemText(1, _translate("Dialog", "cdf"))
        self.label_area.setText(_translate("Dialog", "Area"))
        self.comboBox_area.setItemText(0, _translate("Dialog", "None"))
        self.comboBox_area.setItemText(1, _translate("Dialog", "x=a"))
        self.comboBox_area.setItemText(2, _translate("Dialog", "x<=a"))
        self.comboBox_area.setItemText(3, _translate("Dialog", "a<=x<=b"))
        self.comboBox_area.setItemText(4, _translate("Dialog", "x>=b"))
        self.label_a.setText(_translate("Dialog", "a"))
        self.label_b.setText(_translate("Dialog", "b"))
        self.label_point.setText(_translate("Dialog", "Point"))
        self.pushButton_drawing.setText(_translate("Dialog", "Drawing"))
        self.pushButton_clear.setText(_translate("Dialog", " Clear "))
        self.pushButton_return.setText(_translate("Dialog", " Return"))
