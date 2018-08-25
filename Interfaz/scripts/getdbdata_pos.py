# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#Escrito por: Diego A. Rueda Q

import psycopg2
import sys
import pprint

def main():
    conn_string = "host='localhost' dbname='test' user='user' password='usercode'"
    print("Conectando a la base de datos \n ->%s" % (conn_string))

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT pasiva_theta FROM terapia_220818")
    records = cursor.fetchall()

if __name__ == "__main__":
    main()
