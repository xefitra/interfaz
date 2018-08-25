#-*- coding: utf-8 -*-
#!/usr/bin/python3

# Script para crear un nuevo registro de paciente, se ingresan los datos necesarios
# y se almacenan en la base de datos de todos los pacientes.

import sqlite3, sys, os, pprint
import pandas as pd

def buscar(registration):
    busqueda = input("Con que campo desea realizar la busqueda (nombre, id)?: ")
    entrada = input('Ingrese el '+ str(busqueda) +' del paciente: ')
    conn = sqlite3.connect('../db/pacientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pacientes WHERE " + str(busqueda) + "=?", (entrada,))
    data = c.fetchall()
    if len(data)==0:
        registratrion = False
        name = ""
        print("No entries")
    else:
        registration = True
        name = data[0]
        print(data)


    return registration, name, id

def ingresar(name, id):
    name = input("Ingrese el nombre del paciente: ")
    type_id = input("Please type the patient's id type: ")
    id = input("Please type the patient's id number: ")
    age = input("Please type the patient's age: ")
    gender = input("Please type the patient's gender: ")
    ocupation = input("Please type the patient's actual ocupation: ")

    conn = sqlite3.connect('../db/pacientes.db')
    c = conn.cursor()
    print('Creando registro en base de datos central...')
    c.execute("INSERT INTO pacientes VALUES (?,?,?,?,?,?)", (name, type_id, id, age, gender, ocupation))
    conn.commit()
    conn.close()

    conn = sqlite3.connect('../db/registros/'+str(id)+'.db')
    c = conn.cursor()
    print('Creando base de datos del paciente...')
    c.execute("""CREATE TABLE datos
                (nombre text NOT NULL, tipo id text NOT NULL, id numeric NOT NULL, edad numeric NOT NULL, genero text NOT NULL, ocupacion text NOT NULL)""")
    c.execute("""INSERT INTO datos VALUES (?,?,?,?,?,?)""", (name,type_id,id,age,gender,ocupation))

    conn.commit()
    conn.close()
    print('Base de datos creada con éxito')


def modificar():
    name = input("Please type the patient's name: ")
    conn = sqlite3.connect('../db/pacientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pacientes WHERE nombre=?", (name,))
    pprint.pprint(c.fetchall())
    field = input("Cúal campo quiere modificar?: ")
    c.execute("UPDATE field FROM pacientes WHERE nomber=?", (name,))
    c.execute("SELECT * FROM pacientes WHERE nombre=?", (name,))
    print(pd.read_sql_query(c.fetchall(), conn))
    save = input("Desea guardar los cambios?  y/n")
    if save == 'y':
        conn.commit()
        conn.close()
    elif save == 'n':
        pass

    else:
        pass

if __name__ == '__main__':
    registration = 0
    r,name,id = buscar(registration)
    if r ==False:
        q = input("Paciente no registrado, desea registrar este paciente? y/n: ")
        if q == 'y':
            ingresar(name, id)
        elif q == 'n':
            pass
        else:
            print('Caractér no válido')
    else:
        print('The patient is registered')

    mod = input("Desea modificar alguna entrada? y/n: ")
    if mod == 'y':
        modificar()
    elif mod == 'n':
        pass
    else:
        pass
