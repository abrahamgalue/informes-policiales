import datetime
import mysql.connector
from mysql.connector import Error

def get_persona(ced):
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM persona WHERE numero_de_identificacion = %s;",(ced,))
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
#get_persona(112233)

def get_personas():
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM persona;")
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
#get_personas()

def set_persona(values):
    try:
        connection = mysql.connector.connect(host='localhost',database='proyecto',user='root',password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO persona VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",values)
            print('Warnings:',cursor.fetchwarnings())
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.commit()
            connection.close()
            print("MySQL connection is closed")        
#FORMATO PARA INGRESAR DATOS EN PERSONAS
# datos = (112233,'Elba','Jito',datetime.date(1999,9,9),'Masculino','999-999-9999','No','Hell','El bajito')
# set_persona(datos)