#-*- coding: utf-8 -*-
#!/usr/bin/python3
# Script para buscar entradas en las bases de datos según el nombre ingresado
#   - Faltaria agregar busqueda por numero de cedula - Agregado!
#   - El script imprime los datos de la persona que se busca
import os
import sqlite3

busqueda = input('Desea buscar por (nombre, id): ')
patient = input('Digite el '+ str(busqueda) + ' del paciente: ')

conn = sqlite3.connect('../db/pacientes.db')

try:
    c = conn.cursor()
    c.execute('SELECT id FROM pacientes WHERE '+ str(busqueda) + ' = ?',(str(patient),))
    id = c.fetchone()
    namedb = ''.join((str(id[0])).split())
    namedb = namedb + '.db'
    conn.commit()
    conn.close()
    if os.path.isfile('../db/registros/'+namedb):
        conn = sqlite3.connect('../db/registros/'+namedb)

        c = conn.cursor()

        c.execute('SELECT * FROM datos')

        print(c.fetchall())

        conn.commit()
        conn.close()
    else:
        print('No se encontraron registros con este nombre')

except TypeError:
    print('No se encontraron registros con este nombre')
