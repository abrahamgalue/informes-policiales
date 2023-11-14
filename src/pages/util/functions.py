import mysql.connector
from mysql.connector import Error

def coneccion(pswrd = '', prt = 3306):
    try:
        connection = mysql.connector.connect(host='localhost',port=prt,database='proyecto',
                                             user='root',password=pswrd)
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def id_arresto():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(id) FROM ocurrencia_de_arresto;")
            id = cursor.fetchall()[0][0] + 1
            print(id)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
            return id