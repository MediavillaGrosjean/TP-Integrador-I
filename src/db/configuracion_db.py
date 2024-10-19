from .conexion_db import obtener_conexion
from logger import registrar_actividad, manejar_excepcion

def crear_tabla(nombre_tabla, columnas):
    foreign_keys = columnas.pop('FOREIGN_KEYS', {})
    columnas_def = ', '.join([f"{col} {tipo}" for col, tipo in columnas.items()])

    if foreign_keys:
        foreign_def = ', '.join([f"FOREIGN KEY ({col}) {ref}" for col, ref in foreign_keys.items()])
        columnas_def = f"{columnas_def}, {foreign_def}"

    query = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({columnas_def})"
    verificar_tabla = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nombre_tabla}'"

    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()

            cursor.execute(verificar_tabla)
            existe_tabla = cursor.fetchone()

            if existe_tabla is None:
                cursor.execute(query)
                conexion.commit()
                registrar_actividad(f"Tabla '{nombre_tabla}' creada correctamente.", query)
            else:
                print(f"La tabla '{nombre_tabla}' ya existe. No se registró la actividad.")
    except Exception as e:
        manejar_excepcion(e)
