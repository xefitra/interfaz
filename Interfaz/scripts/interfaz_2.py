#-*- coding: utf-8 -*-
#!/usr/bin/python3
# By: Diego A. Rueda Q.

# Importando librerias
from sketch_3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3, sys, os

def funcionalidades(self, MainWindow):
    hoy = datetime.datetime.now()
    mes = hoy.month
    dia = hoy.day
    año = hoy.year

    self.dateEdit.setDate(QtCore.QDate(año, mes, dia))
    self.dateEdit_2.setDate(QtCore.QDate(año, mes, dia))
    final = hoy + datetime.timedelta(days=30)
    año = final.year
    mes = final.month
    dia = final.day
    self.dateEdit_3.setDate(QtCore.QDate(año, mes, dia))
    print(hoy)
    def index_1():
        self.stackedWidget.setCurrentIndex(1)
    def index_0():
        self.stackedWidget.setCurrentIndex(0)
    def search():
        if self.dockWidget_3.isVisible()==True:
            self.dockWidget_3.setHidden(True)
        else:
            self.dockWidget_3.setVisible(True)

    self.actionNuevo.triggered.connect(index_1)
    self.actionNuevo_2.triggered.connect(index_1)
    self.actionNuevo_registro_2.triggered.connect(index_0)
    self.actionBuscar_registro_2.triggered.connect(search)
    self.actionBuscar_registro_3.triggered.connect(search)

def addEntry(self, MainWindow):
    def guardar():
        import sqlite3, sys, os
        nombre = str(self.lineEdit.text())
        tipo = self.comboBox.currentText()
        id = str(self.lineEdit_2.text())
        edad = str(self.lineEdit_3.text())
        fecha = self.dateEdit.date().toString()

        if self.radioButton.isChecked()==True:
            genero = 'Femenino'
        else:
            genero = 'Masculino'

        ocupacion = str(self.lineEdit_5.text())
        observaciones = self.textEdit.toPlainText()

        conn = sqlite3.connect('../db/pacientes.db')
        c = conn.cursor()

        c.execute("SELECT * FROM pacientes WHERE id=?", (id,))
        selec = c.fetchall()

        if len(selec)>=1 or id=='':
            print('Ya existe una entrada con esta id o entrada no válida')
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO pacientes VALUES (?,?,?,?,?,?,?,?)", (nombre.upper(), fecha, tipo, id, edad, genero, ocupacion.upper(), observaciones.upper()))
            conn.commit()
            conn.close()
            print('Entrada creada')

            if os.path.isfile('../db/registros/'+str(id)+'.db'):
                print('Base de datos del paciente encontrada')
            else:
                conn = sqlite3.connect('../db/registros/'+str(id)+'.db')
                c = conn.cursor()
                print('Creando base de datos del paciente...')
                c.execute("""CREATE TABLE datos
                            (nombre text NOT NULL,fecha text NOT NULL, tipo text NOT NULL, id numeric NOT NULL, edad numeric NOT NULL, genero text NOT NULL, ocupacion text NOT NULL, observaciones text NOT NULL)""")
                c.execute("""INSERT INTO datos VALUES (?,?,?,?,?,?,?,?)""", (nombre.upper(),fecha, tipo,id,edad,genero,ocupacion.upper(), observaciones.upper()))

                conn.commit()
                conn.close()
                print('Base de datos creada...')
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.textEdit.clear()
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(False)

    self.commandLinkButton.clicked.connect(guardar)

    def addprogram():
        stotales = self.lineEdit_4.text()
        ssemanales = self.lineEdit_7.text()
        inicio = self.dateEdit_2.date().toString()
        final = self.dateEdit_3.date().toString()
        observaciones = self.textEdit_2.toPlainText()
        conn = sqlite3.connect()

    self.commandLinkButton_5.clicked.connect(addprogram)

def search(self, MainWindow):
    def search():
        tipo = self.comboBox_2.currentText()
        buscar = self.lineEdit_6.text()
        conn = sqlite3.connect('../db/pacientes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM pacientes WHERE id = "+ str(buscar) +"")
        selection = c.fetchall()
        print(selection)
        conn.commit()
        conn.close()

        self.tableWidget.setRowCount(len(selection))
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem(selection[0][0]))
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem(buscar))
        self.tableWidget.move(0,0)
        self.gridLayout_9.addWidget(self.tableWidget, 5, 0, 1, 1)
    self.commandLinkButton_3.clicked.connect(search)


    def select():
        index = self.tableWidget.currentItem().row()
        item = self.tableWidget.item(index,1).text()
        print(item)
        self.stackedWidget.setCurrentIndex(3)

        conn = sqlite3.connect('../db/pacientes.db')
        c = conn.cursor()

        c.execute("SELECT * FROM pacientes WHERE id=?",(item,))
        data = c.fetchone()
        print(data)
        self.lineEdit_9.setText(data[0])
        self.lineEdit_10.setText(str(data[3]))
        dict = {'CC':0,'TI':1,'Pasaporte':2}
        self.comboBox_3.setCurrentIndex(dict[data[2]])
        self.lineEdit_8.setText(str(data[4]))

        if data[5]=='Masculino':
            self.radioButton_4.setChecked(True)
            self.radioButton_3.setChecked(False)
        elif data[5]=='Femenino':
            self.radioButton_4.setChecked(True)
            self.radioButton_3.setChecked(False)

        fecha = QtCore.QDate.fromString(data[1])
        self.dateEdit_4.setDate(QtCore.QDate(fecha))
        self.lineEdit_11.setText(str(data[6]))
        self.textEdit_3.setText(str(data[7]))


    self.commandLinkButton_4.clicked.connect(select)
