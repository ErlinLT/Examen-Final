from glob import escape
from conexion import getConn
#from datetime import datetime
conn = None
cursor = None

    
def crear():
    sqlcreate = "CREATE TABLE IF NOT EXISTS FRASES (id INTEGER PRIMARY KEY AUTOINCREMENT, idioma TEXT, frase TEXT,autor TEXT);"
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sqlcreate)
    conn.commit()

def añadir(idioma,frase,autor):
    sqlinsert = "INSERT INTO FRASES(idioma,frase,autor) values (?,?, ?);"
    conn = getConn()
    cursor = conn.cursor()
    #timestamp = int(round(datetime.now().timestamp()))
    cursor.execute(sqlinsert,(idioma,frase,autor))
    conn.commit()

def mostar():
    sqlselect = "SELECT * from FRASES"
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sqlselect)
    return cursor.fetchall()
#-----------------------------------------
    # return{ 
    #     "idData":row[0],
    #     "idQuery":row[1],
    #     "confirmados":row[2],
    #     "activos":row[3],
    #     "provincia":row[4]
    # }
