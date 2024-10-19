import sqlite3
from config import DB_NAME

def obtener_conexion():
    try:
        conexion = sqlite3.connect(DB_NAME)
        return conexion
    except sqlite3.Error as e:
        raise e
