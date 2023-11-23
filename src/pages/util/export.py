# Pip commands necessary:
# pip install pandas
# pip install openpyxl
# pip install XlsxWriter
import pandas as pd
from .persona import get_personas,get_persona
from .senas_de_identificacion import get_señas
from .ocurrencia_de_arresto import get_arrestos
from .cond import get_condenas
 
# creating the DataFrame
def export_personas():
    p = get_personas()
    ced = [p[i][0] for i in range(len(p))]
    nom = [p[i][1] for i in range(len(p))]
    ap = [p[i][2] for i in range(len(p))]
    dob = [p[i][3].strftime("%Y-%m-%d") for i in range(len(p))]
    sex= [p[i][4] for i in range(len(p))]
    telf = [str(p[i][5]) for i in range(len(p))]
    dir = [p[i][6] for i in range(len(p))]
    nac = [p[i][7] for i in range(len(p))]
    ali = [p[i][8] for i in range(len(p))]

    personas = pd.DataFrame({
        'Identificación': ced,
        'Nombre': nom,
        'Apellido': ap,
        'Fecha de Nacimiento':dob,
        'Sexo': sex,
        'Teléfono': telf,
        'Dirección': dir,
        'Nacionalidad': nac,
        'Alias': ali
    })
    s = get_señas()
    pes = [s[i][0] for i in range(len(s))]
    al = [s[i][1] for i in range(len(s))]
    colp = [s[i][2] for i in range(len(s))]
    cab = [s[i][3] for i in range(len(s))]
    ccab = [s[i][4] for i in range(len(s))]
    oj = [s[i][5] for i in range(len(s))]
    otr = [s[i][6] for i in range(len(s))]
    sced = [s[i][7] for i in range(len(s))]

    senas = pd.DataFrame({
        'Identificación Persona': sced,
        'Peso': pes,
        'Altura': al,
        'Color de piel': colp,
        'Cabello': cab,
        'Color de Cabello': ccab,
        'Ojos': oj,
        'Otra Característica': otr
    })
    # determining the name of the file
    file_name = 'Personas'
    sheets = [('Personas', personas), ('Personas', senas)]
    sc = 0
    with pd.ExcelWriter(f"..\informes-policiales\exports\{file_name}.xlsx") as writer:
        for sheetname, df in sheets: # loop through `dict` of dataframes
            df.to_excel(writer, sheet_name=sheetname,index=False,startcol=sc)
            worksheet = writer.sheets[sheetname] # pull worksheet object
            for idx, col in enumerate(df.columns): # loop through all columns
                series = df[col]
                max_len = max((
                    series.astype(str).str.len().max(), # len of largest item
                    len(str(series.name)) # len of column name/header
                    )) + 1 # adding a little extra space
                worksheet.set_column(idx+sc, idx+sc, max_len) # set column width
            sc +=10
def export_arrestos():
    a=get_arrestos()
    c=get_condenas()
    p = [a[i][7] for i in range(len(a))]
    pa = list()
    for ced in p:
        info = get_persona(ced)
        pa.append((info[0][1],info[0][2]))

    id= [a[i][0] for i in range(len(a))]
    fecha= [a[i][1].strftime("%Y-%m-%d") for i in range(len(a))]
    hora= [a[i][2] for i in range(len(a))]
    lugar= [a[i][3] for i in range(len(a))]
    delito= [a[i][4] for i in range(len(a))]
    Tdelito= [a[i][5] for i in range(len(a))]
    descripcion= [a[i][6] for i in range(len(a))]
    implicado= [a[i][7] for i in range(len(a))]
    nom = [pa[i][0] for i in range(len(p))]
    ap = [pa[i][1] for i in range(len(p))]
    
    arresto = pd.DataFrame({
        'Id': id,
        'Fecha': fecha,
        'Hora': hora,
        'Lugar':lugar,
        'Delito': delito,
        'Tipo de Delito': Tdelito,
        'Descripción': descripcion,
        'Identificación Implicado': implicado,
        'Nombre Implicado': nom,
        'Apellido Implicado': ap
    })
    #condena
    fechaC = [c[i][0].strftime("%Y-%m-%d") for i in range(len(c))]
    sentencia= [c[i][1] for i in range(len(c))]
    id_a= [c[i][2] for i in range(len(c))]
    condena = pd.DataFrame({
        'Fecha Condena': fechaC,
        'Sentencia': sentencia,
        'Id Arresto': id_a,
       
    })
    
    file_name = 'Arrestos'
    sheets = [('Arresto', arresto), ('Arresto', condena)]
    sc = 0
    with pd.ExcelWriter(f"..\informes-policiales\exports\{file_name}.xlsx") as writer:
        for sheetname, df in sheets: # loop through `dict` of dataframes
            df.to_excel(writer, sheet_name=sheetname,index=False,startcol=sc)
            worksheet = writer.sheets[sheetname] # pull worksheet object
            for idx, col in enumerate(df.columns): # loop through all columns
                series = df[col]
                max_len = max((
                    series.astype(str).str.len().max(), # len of largest item
                    len(str(series.name)) # len of column name/header
                    )) + 1 # adding a little extra space
                worksheet.set_column(idx+sc, idx+sc, max_len) # set column width
            sc+=10
            