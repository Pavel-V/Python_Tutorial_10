# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1025, 640)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_widget_input_1 = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_widget_input_1.sizePolicy().hasHeightForWidth())
        self.table_widget_input_1.setSizePolicy(sizePolicy)
        self.table_widget_input_1.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_widget_input_1.setObjectName("table_widget_input_1")
        self.table_widget_input_1.setColumnCount(0)
        self.table_widget_input_1.setRowCount(0)
        self.table_widget_input_1.horizontalHeader().setDefaultSectionSize(50)
        self.gridLayout_2.addWidget(self.table_widget_input_1, 0, 0, 1, 1)
        self.table_widget_input_2 = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_widget_input_2.sizePolicy().hasHeightForWidth())
        self.table_widget_input_2.setSizePolicy(sizePolicy)
        self.table_widget_input_2.setObjectName("table_widget_input_2")
        self.table_widget_input_2.setColumnCount(0)
        self.table_widget_input_2.setRowCount(0)
        self.table_widget_input_2.horizontalHeader().setDefaultSectionSize(50)
        self.gridLayout_2.addWidget(self.table_widget_input_2, 0, 1, 1, 1)
        self.table_widget_output = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_widget_output.sizePolicy().hasHeightForWidth())
        self.table_widget_output.setSizePolicy(sizePolicy)
        self.table_widget_output.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget_output.setObjectName("table_widget_output")
        self.table_widget_output.setColumnCount(0)
        self.table_widget_output.setRowCount(0)
        self.table_widget_output.horizontalHeader().setDefaultSectionSize(50)
        self.gridLayout_2.addWidget(self.table_widget_output, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push_button_create = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_create.sizePolicy().hasHeightForWidth())
        self.push_button_create.setSizePolicy(sizePolicy)
        self.push_button_create.setObjectName("push_button_create")
        self.horizontalLayout.addWidget(self.push_button_create)
        self.spin_box_rows = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_box_rows.sizePolicy().hasHeightForWidth())
        self.spin_box_rows.setSizePolicy(sizePolicy)
        self.spin_box_rows.setMinimum(1)
        self.spin_box_rows.setMaximum(20)
        self.spin_box_rows.setProperty("value", 5)
        self.spin_box_rows.setObjectName("spin_box_rows")
        self.horizontalLayout.addWidget(self.spin_box_rows)
        self.spin_box_cols = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_box_cols.sizePolicy().hasHeightForWidth())
        self.spin_box_cols.setSizePolicy(sizePolicy)
        self.spin_box_cols.setMinimum(1)
        self.spin_box_cols.setMaximum(20)
        self.spin_box_cols.setProperty("value", 5)
        self.spin_box_cols.setObjectName("spin_box_cols")
        self.horizontalLayout.addWidget(self.spin_box_cols)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_button_calc_3 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_calc_3.sizePolicy().hasHeightForWidth())
        self.push_button_calc_3.setSizePolicy(sizePolicy)
        self.push_button_calc_3.setObjectName("push_button_calc_3")
        self.gridLayout.addWidget(self.push_button_calc_3, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.push_button_calc_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_calc_2.sizePolicy().hasHeightForWidth())
        self.push_button_calc_2.setSizePolicy(sizePolicy)
        self.push_button_calc_2.setObjectName("push_button_calc_2")
        self.gridLayout.addWidget(self.push_button_calc_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.push_button_calc_1 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_calc_1.sizePolicy().hasHeightForWidth())
        self.push_button_calc_1.setSizePolicy(sizePolicy)
        self.push_button_calc_1.setObjectName("push_button_calc_1")
        self.gridLayout.addWidget(self.push_button_calc_1, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Матрицы"))
        self.push_button_create.setText(_translate("Form", "Создать"))
        self.spin_box_rows.setToolTip(_translate("Form", "число строк"))
        self.spin_box_cols.setToolTip(_translate("Form", "число столбцов"))
        self.push_button_calc_3.setText(_translate("Form", "Задание 3"))
        self.label_3.setText(_translate("Form", "краткий текст задания 3..."))
        self.push_button_calc_2.setText(_translate("Form", "Задание 2"))
        self.label_2.setText(_translate("Form", "краткий текст задания 2..."))
        self.push_button_calc_1.setText(_translate("Form", "Задание 1"))
        self.label_1.setText(_translate("Form", "краткий текст задания 1..."))


