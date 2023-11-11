from mysql.connector import Error
from .functions import coneccion

def add_arresto(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """INSERT INTO ocurrencia_de_arresto (fecha, hora, lugar, delito, 
            tipo_de_delito, descripcion, implicado_numero_de_identificacion)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
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
#FORMATO PARA INGRESAR DATOS EN ARRESTO
# datos = ('2000-02-02','18:00:00','No se','Ser Feo','Delito de Belleza','Esta muy feo','30557711')
# add_arresto(datos)

def remove_arresto(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM ocurrencia_de_arresto WHERE id = %s;",(id,))
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
# remove_arresto(2)

def get_arresto(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ocurrencia_de_arresto WHERE id = %s;",(id,))
            implicado = cursor.fetchall()
            print(implicado)
            return implicado
    except Error as e:
        print("Error", e)
    finally:
        if connection is not None :
            if connection.is_connected():
                cursor.close()
                print("MySQL cursor is closed")
                connection.close()
                print("MySQL connection is closed")
# get_persona(12345678)

def get_arrestos():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ocurrencia_de_arresto ORDER BY id;")
            implicados = cursor.fetchall()
            print(implicados)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
            return implicados