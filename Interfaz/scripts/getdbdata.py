# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#Escrito por: Diego A. Rueda Q
# Script para obtener datos especificos de una base de datos, graficarlos y guardar
# la grafica como una figura en formato png

import sqlite3

conn = sqlite3.connect('ruedadiego.db')

c = conn.cursor()

c.execute("SELECT pasiva_theta FROM terapia_220818")

lista = []
ejex = []

for i in c.fetchall():
    lista.append(i)

for i in range(len(lista)):
    ejex.append(i)


import matplotlib.pyplot as plt
plt.plot(ejex, lista)
plt.savefig('image.png')
#print(ejex)
#print(lista)
