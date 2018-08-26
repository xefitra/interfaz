#-*- coding: utf-8 -*-
#!/usr/bin/python3
# By: Diego A. Rueda Q.

# Importando librerias
from sketch_1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sys, os

def funcionalidades(self, MainWindow):
    hoy = datetime.now()
    mes = hoy.month
    dia = hoy.day
    año = hoy.year
    self.dateEdit.setDate(QtCore.QDate(año, mes, dia))
    self.dateEdit_2.setDate(QtCore.QDate(año, mes, dia))
    print(hoy)
