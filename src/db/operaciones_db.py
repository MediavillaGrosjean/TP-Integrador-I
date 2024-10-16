from conexion_db import obtener_conexion
from excepciones import manejar_excepcion
from src.logger import registrar_actividad

def insertar_datos(tabla, datos):
    if not datos:
        raise ValueError("No hay datos para insertar.")
    
    columnas = list(datos[0].keys())
    columnas_formateadas = ', '.join(columnas)
    placeholders = ', '.join('?' * len(columnas))
    
    query = f"INSERT INTO {tabla} ({columnas_formateadas}) VALUES ({placeholders})"
    
    try:
        with obtener_conexion() as conexion:
            for fila in datos:
                valores = tuple(fila[columna] for columna in columnas)
                conexion.execute(query, valores)
        registrar_actividad(f"Datos insertados en la tabla {tabla}.", datos)
    except Exception as e:
        manejar_excepcion(e)
