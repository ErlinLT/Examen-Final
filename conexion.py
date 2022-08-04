import sqlite3
conn = None
 

def getConn():
    global conn
    if (conn is None):
        conn = sqlite3.connect('ExamnFinal.db')
    return conn
    #permite la conexion a la base de datos
