import datetime
import mysql.connector
from mysql.connector import Error

def get_implicado(ced):
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM implicado WHERE numero_de_identificacion = %s;",(ced,))
            implicado = cursor.fetchall()
            print(implicado)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return implicado

def get_implicados():
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM implicado;")
            implicados = cursor.fetchall()
            print(implicados)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        return implicados

#FORMATO PARA INGRESAR DATOS EN IMPLICADO
#datos = (112233,'Elba','Jito',datetime.date(1999,9,9),'Masculino','999-999-9999','No','Hell','El bajito')
#set_implicado(datos)
def set_implicado(values):
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO implicado VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",values)
            print('Warnings:',cursor.fetchwarnings())
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.commit()
            connection.close()
            print("MySQL connection is closed")
