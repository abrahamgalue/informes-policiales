from mysql.connector import Error
from .functions import coneccion

def add_persona(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO persona VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",values)
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
#FORMATO PARA INGRESAR DATOS EN PERSONAS
# datos = (12345678,'Elba','Jito','2000-02-02','Masculino','+58 9999999999','No','Hell','El bajito')
# add_persona(datos)

def remove_persona(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM persona WHERE numero_de_identificacion = %s;",(ced,))
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
# remove_persona(12345678)

def get_persona(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM persona WHERE numero_de_identificacion = %s;",(ced,))
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


def get_personas():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM persona ORDER BY nombre;")
            implicados = cursor.fetchall()
            print(implicados)
            return implicados
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")