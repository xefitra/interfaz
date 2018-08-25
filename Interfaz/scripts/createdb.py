#-*- coding: utf-8 -*-
#!/usr/bin/python3

# by: Diego Rueda
# Script para crear base de datos de los pacientes, se crea inicialmente la tablas
# de datos con los datos biometricos de cada paciente.

import sqlite3
import sys
import os

conn = sqlite3.connect('../db/pacientes.db')

c = conn.cursor()
c.execute("SELECT * FROM pacientes")
datos = c.fetchall()
#print(datos)
c.execute("SELECT nombre FROM pacientes")

lista = []
id = []

for i in c.fetchall():
 lista.append(i[0])
#print(lista)
for i in lista:
    c.execute("SELECT nombre,id FROM pacientes WHERE nombre = ?", (i,))
    ident = c.fetchone()
    id.append(str(ident[1]))
dbname = []

for i in range(len(lista)):
    dbname.append(''.join((str(id[i]) + '.db').split()))
#print(dbname)

conn.commit()
conn.close()

for i in range(len(dbname)):
    newpath = r'../db/registros/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if os.path.isfile('../db/registros/'+dbname[i]):
        print(dbname[i]+' Registro encontrado')
    else:
        conn = sqlite3.connect('../db/registros/'+dbname[i])
        c = conn.cursor()
        try:
            c.execute("""CREATE TABLE datos
                        (nombre text NOT NULL, tipo id text NOT NULL, id numeric NOT NULL, edad numeric NOT NULL, genero text NOT NULL, ocupacion text NOT NULL)""")
            c.execute("""INSERT INTO datos VALUES (?,?,?,?,?,?)""", datos[i])
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
            print('Ha ocurrido un error...')
            print('Saliendo de la base de datos sin realizar cambios')
