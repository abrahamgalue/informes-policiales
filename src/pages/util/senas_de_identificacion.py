from mysql.connector import Error
from .functions import coneccion

def add_seña(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO señas_de_identificacion VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",values)
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
# datos = [80,145,'Morena','Ondulado','Carmesí','Marron Oscuro','Pelo Teñido',3000555]
# add_seña(datos)

def remove_seña(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM señas_de_identificacion WHERE persona_numero_de_identificacion = %s;",(ced,))
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
# remove_seña(3000555)

def get_señas():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """SELECT * FROM señas_de_identificacion JOIN persona 
            ON persona.numero_de_identificacion = señas_de_identificacion.persona_numero_de_identificacion 
            ORDER BY persona.nombre ASC,persona.apellido ASC"""
            cursor.execute(sql)
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
# get_señas()

def get_seña(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM señas_de_identificacion WHERE persona_numero_de_identificacion = %s;",(ced,))
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
# get_seña(3000555)

def update_seña(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ UPDATE señas_de_identificacion SET peso = %s, 
            altura = %s, color_de_piel = %s, cabello = %s,
            color_de_cabello = %s, ojos = %s, 
            otra_caracteristica = %s 
            WHERE señas_de_identificacion.persona_numero_de_identificacion = %s """
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
# datos = [101.02,101.02,'prueba 1','prueba 1','prueba 1','prueba 1','prueba 1',1010101]
# update_seña(datos)