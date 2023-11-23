from mysql.connector import Error
from .functions import coneccion
from .senas_de_identificacion import remove_seña
from .ocurrencia_de_arresto import get_arrestos_persona, delete_arresto

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

def delete_arrestos_complice(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ DELETE FROM complice WHERE complice.persona_numero_de_identificacion = (%s);"""
            cursor.execute(sql,(ced,))
            print('Warnings:',cursor.fetchwarnings())
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                
def delete_persona(ced):
    delete_arrestos_complice(ced)
    remove_seña(ced)
    arrestos = get_arrestos_persona(ced)
    for i in range(len(arrestos)):
        delete_arresto(arrestos[i][0])
    remove_persona(ced)
    
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
            cursor.execute("SELECT * FROM persona ORDER BY nombre ASC, apellido ASC;")
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

def update_persona(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ UPDATE persona SET nombre = %s, apellido = %s, 
            fecha_de_nacimiento = %s, sexo = %s, telefono = %s,
            direccion = %s, nacionalidad = %s, alias = %s 
            WHERE persona.numero_de_identificacion = %s """
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
# datos = ('prueba 1','prueba 1','1010-01-02','Masculino','+1 0101010011','Prueba','Hell','prueba',1010101)
# update_persona(datos)

def get_implicados():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ SELECT persona.numero_de_identificacion, persona.nombre, persona.apellido, 
            persona.fecha_de_nacimiento, COUNT(ocurrencia_de_arresto.implicado_numero_de_identificacion) 
            FROM persona LEFT JOIN ocurrencia_de_arresto ON persona.numero_de_identificacion = ocurrencia_de_arresto.implicado_numero_de_identificacion 
            GROUP BY persona.numero_de_identificacion ORDER BY `COUNT(ocurrencia_de_arresto.implicado_numero_de_identificacion)` DESC, 
            persona.nombre ASC, persona.apellido ASC;"""
            cursor.execute(sql)
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
                
def get_complices():
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ SELECT persona.numero_de_identificacion, persona.nombre, persona.apellido, persona.fecha_de_nacimiento, 
            COUNT(complice.ocurrencia_de_arresto_id) FROM persona LEFT JOIN complice 
            ON persona.numero_de_identificacion = complice.persona_numero_de_identificacion
            GROUP BY persona.numero_de_identificacion ORDER BY COUNT(complice.ocurrencia_de_arresto_id) DESC, 
            persona.nombre DESC;"""
            cursor.execute(sql)
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
                
def add_complice(values):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO complice VALUES (%s, %s);",values)
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
                
def get_complices_arresto(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ SELECT * FROM persona JOIN complice 
            ON persona.numero_de_identificacion = complice.persona_numero_de_identificacion 
            WHERE complice.ocurrencia_de_arresto_id = (%s) ORDER BY persona.nombre ASC, persona.apellido ASC;"""
            cursor.execute(sql,(id,))
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
# get_complices_arresto(9)

def get_arrestos_complice(ced):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ SELECT complice.ocurrencia_de_arresto_id, ocurrencia_de_arresto.fecha FROM `complice` JOIN ocurrencia_de_arresto ON complice.ocurrencia_de_arresto_id = ocurrencia_de_arresto.id 
            WHERE persona_numero_de_identificacion = %s;"""
            cursor.execute(sql,(ced,))
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
              
def delete_complices_arresto(id):
    try:
        connection = coneccion()
        if connection is not None:
            cursor = connection.cursor()
            sql = """ DELETE FROM complice WHERE complice.ocurrencia_de_arresto_id = (%s);"""
            cursor.execute(sql,(id,))
            print('Warnings:',cursor.fetchwarnings())
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
# delete_complices_arresto(3)

