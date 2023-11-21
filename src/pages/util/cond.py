from mysql.connector import Error
from .functions import coneccion

def add_condena(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO condena VALUES (%s, %s, %s);",values)
            print('Warnings:',cursor.fetchwarnings())
            connection.commit()
    except Error as e:
        print("Error", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                print("MySQL cursor is closed")
                connection.close()
                print("MySQL connection is closed")
# Fecha, Sentencia, Id Arresto
# datos = ['2023-10-28','6 meses en carcel', 1]
# add_condena(datos)

def remove_condena(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM condena WHERE ocurrencia_de_arresto_id = %s;",(id,))
            print('Warnings:',cursor.fetchwarnings())
            connection.commit()
    except Error as e:
        print("Error", e)
    finally:
        if connection is not None :
            if connection.is_connected():
                cursor.close()
                print("MySQL cursor is closed")
                connection.close()
                print("MySQL connection is closed")
# remove_condena(1)

def get_condenas():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM condena ORDER BY fecha;")
            señas = cursor.fetchall()
            print(señas)
            return señas
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")       
# get_condenas()

def get_condena(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM condena WHERE ocurrencia_de_arresto_id = %s;",(id,))
            implicado = cursor.fetchall()
            print(implicado)
            return implicado
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
# get_condena(1)

def update_condena(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """UPDATE `condena` SET `fecha` = %s, `sentencia` = %s 
            WHERE `condena`.`ocurrencia_de_arresto_id` = %s;"""
            cursor.execute(sql,values)
            print('Warnings:',cursor.fetchwarnings())
            connection.commit()
    except Error as e:
        print("Error", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                print("MySQL cursor is closed")
                connection.close()
                print("MySQL connection is closed")
# datos = ['2023-11-07','Super Muerte', 3]
# update_condena(datos)