#-*- coding: utf-8 -*-
#!/usr/bin/python3
import os
import sqlite3

patient = input('Name of the person you want to search: ' + str())

conn = sqlite3.connect('../db/pacientes.db')

try:
    c = conn.cursor()
    c.execute('SELECT id FROM pacientes WHERE nombre = ?', (str(patient),))
    namedb = str(c.fetchone()[0]) + '.db'
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
        print('No records founded')

except TypeError:
    print('No records founded')
