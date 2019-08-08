# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:06:59 2019

@author: Pavel
"""

import random
import numpy as np
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QDoubleSpinBox, QLineEdit
import ui_form

def calc_task_1(left_matrix, right_matrix):
    ''' Функция, непосредственно реализующая нужные вычисления '''

    # !!! Замените на свое задание и по аналогии создайте функции calc_task_2 и calc_task_3    
    return left_matrix + 2 * right_matrix

class FormController(QtWidgets.QWidget, ui_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_task_labels()
        self.setup_fill_input_tables()
        self.setup_connection() # установка соединений между сигналами и слотами вынесена в отдельную функцию
        
    def set_task_labels(self):
        
        # !!! Замените текст на текст своих заданий 
        self.label_1.setText('C = L + 2 R')
        self.label_2.setText('Поэлементное умножение матриц')
        self.label_3.setText('C = dot(L, R)')

    def setup_connection(self):
        self.push_button_create.clicked.connect(self.setup_fill_input_tables)
        
        # Здесь использованы элементы функционального программирования:
        # * лямбда-функция - короткая функция, которая не имеет названия и записывается прямо в коде другой функции;
        # * функция run_task получает в качестве аргумента функцию и затем исопользует ее.
        self.push_button_calc_1.clicked.connect(lambda : self.run_task(calc_task_1))
        # !!! Соедините две оставшиеся кнопки с вызовом self.run_task и передачей нужных функций
        
    def setup_fill_input_tables(self):
        rows = self.spin_box_rows.value()
        cols = self.spin_box_cols.value()
        self.setup_fill_input_table(self.table_widget_input_1, rows, cols)
        self.setup_fill_input_table(self.table_widget_input_2, rows, cols)   
        		
    def setup_fill_input_table(self, table, rows = 1, cols = 1):
        ''' Создание таблиц нужного размера и заполнение их случайными числами '''        
        table.setRowCount(rows)   
        table.setColumnCount(cols)
        
        for r in range(rows):
            table.setVerticalHeaderItem(r, QTableWidgetItem(str(r)))
            for c in range(cols):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, random.randint(-100, 100) / 10.)
                table.setItem(r, c, item)
        
        for c in range(cols):
            table.setHorizontalHeaderItem(c, QTableWidgetItem(str(c)))    
        
    def run_task(self, calc_function):
        rows = self.spin_box_rows.value()
        cols = self.spin_box_cols.value()
        input_left = np.full((rows, cols), 0.)
        input_right = np.full((rows, cols), 0.)
        
        for r in range(rows):
            for c in range(cols):
                input_left[r, c]  = float(self.table_widget_input_1.item(r, c).text())
                input_right[r, c] = float(self.table_widget_input_2.item(r, c).text())
                
        output = calc_function(input_left, input_right)

        self.table_widget_output.setRowCount(rows)
        self.table_widget_output.setColumnCount(cols)
        
        for r in range(output.shape[0]):
            self.table_widget_output.setVerticalHeaderItem(r, QTableWidgetItem(str(r)))
            for c in range(output.shape[1]):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, float(output[r, c]))
                self.table_widget_output.setItem(r, c, item)
                
        for c in range(output.shape[1]):
            self.table_widget_output.setHorizontalHeaderItem(c, QTableWidgetItem(str(c)))  
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form_controller = FormController()
    form_controller.show()
    app.exec()

if __name__ == '__main__':
    main()
