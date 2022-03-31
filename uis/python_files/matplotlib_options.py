# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlib_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matplot_options(object):
    def setupUi(self, matplot_options):
        matplot_options.setObjectName("matplot_options")
        matplot_options.resize(1185, 636)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(matplot_options)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.canvas_widget = OptionCanvasWidget(matplot_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_widget.sizePolicy().hasHeightForWidth())
        self.canvas_widget.setSizePolicy(sizePolicy)
        self.canvas_widget.setObjectName("canvas_widget")
        self.horizontalLayout_2.addWidget(self.canvas_widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(matplot_options)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.velx_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velx_label.sizePolicy().hasHeightForWidth())
        self.velx_label.setSizePolicy(sizePolicy)
        self.velx_label.setObjectName("velx_label")
        self.gridLayout.addWidget(self.velx_label, 0, 0, 1, 1)
        self.vely_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vely_lineEdit.sizePolicy().hasHeightForWidth())
        self.vely_lineEdit.setSizePolicy(sizePolicy)
        self.vely_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.vely_lineEdit.setObjectName("vely_lineEdit")
        self.gridLayout.addWidget(self.vely_lineEdit, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.vely_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vely_label.sizePolicy().hasHeightForWidth())
        self.vely_label.setSizePolicy(sizePolicy)
        self.vely_label.setObjectName("vely_label")
        self.gridLayout.addWidget(self.vely_label, 1, 0, 1, 1)
        self.velx_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velx_lineEdit.sizePolicy().hasHeightForWidth())
        self.velx_lineEdit.setSizePolicy(sizePolicy)
        self.velx_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.velx_lineEdit.setObjectName("velx_lineEdit")
        self.gridLayout.addWidget(self.velx_lineEdit, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(17, 262, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.save_pushButton = QtWidgets.QPushButton(matplot_options)
        self.save_pushButton.setObjectName("save_pushButton")
        self.horizontalLayout.addWidget(self.save_pushButton)
        self.reset_pushButton = QtWidgets.QPushButton(matplot_options)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout.addWidget(self.reset_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(matplot_options)
        QtCore.QMetaObject.connectSlotsByName(matplot_options)

    def retranslateUi(self, matplot_options):
        _translate = QtCore.QCoreApplication.translate
        matplot_options.setWindowTitle(_translate("matplot_options", "Form"))
        self.groupBox.setTitle(_translate("matplot_options", "Optionen"))
        self.velx_label.setText(_translate("matplot_options", "<html><head/><body><p>Geschwindigkeit <br>in x-Richtung</p></body></html>"))
        self.vely_label.setText(_translate("matplot_options", "<html><head/><body><p>Geschwindigkeit <br>in y-Richtung</p></body></html>"))
        self.save_pushButton.setText(_translate("matplot_options", "Save"))
        self.reset_pushButton.setText(_translate("matplot_options", "Reset"))
from canvaswidget import OptionCanvasWidget
