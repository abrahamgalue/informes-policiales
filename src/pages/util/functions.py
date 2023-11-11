import datetime
import mysql.connector
from mysql.connector import Error

def conneccion(pswrd = '', prt = 3306):
    try:
        connection = mysql.connector.connect(host='localhost',port=prt,database='proyecto',
                                             user='root',password=pswrd)
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
