from .conexion_db import obtener_conexion
from logger import registrar_actividad, manejar_excepcion

def insertar_provincia(datos):
    filas_insertadas = 0
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            for row in datos:
                if 'ID_provincia' in row and 'Provincia' in row:
                    cursor.execute(
                        '''
                        INSERT OR IGNORE INTO Provincia (ID, Nombre_provincia) VALUES (?, ?)
                        ''',
                        (row['ID_provincia'], row['Provincia']))
                    if cursor.rowcount > 0:
                        filas_insertadas += 1
                        registrar_actividad(f"Datos insertados en la tabla Provincia.", {'ID_provincia': row['ID_provincia'], 'Provincia': row['Provincia']})
            conexion.commit()
            if filas_insertadas == 0:
                print("No se efectuó ningún cambio: no se insertaron nuevos elementos en la tabla Provincia.")
    except Exception as e:
        manejar_excepcion(e)

def obtener_regimen_ids(datos):
    regimenes = {}
    filas_insertadas = 0
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            for row in datos:
                if 'Regimen_Tributario' in row:
                    regimen = row['Regimen_Tributario']
                    if regimen not in regimenes:
                        cursor.execute(
                            '''
                            INSERT OR IGNORE INTO Regimen_Tributario (Nombre_regimen) VALUES (?)
                            ''', (regimen,))
                        cursor.execute('SELECT ID FROM Regimen_Tributario WHERE Nombre_regimen = ?', (regimen,))
                        regimenes[regimen] = cursor.fetchone()[0]
                        if cursor.rowcount > 0:
                            filas_insertadas += 1
                            registrar_actividad(f"Datos insertados en la tabla Regimen_Tributario.", {'ID': regimenes[regimen], 'Nombre_regimen': row['Regimen_Tributario']})
            conexion.commit()
            if filas_insertadas == 0:
                print("No se efectuó ningún cambio: no se insertaron nuevos elementos en la tabla Regimen_Tributario.")
    except Exception as e:
        manejar_excepcion(e)
    return regimenes

def obtener_categoria_ids(datos):
    categorias = {}
    filas_insertadas = 0
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            for row in datos:
                if 'Categoria' in row:
                    categoria = row['Categoria']
                    if categoria not in categorias:
                        cursor.execute(
                            '''
                            INSERT OR IGNORE INTO Categoria (Nombre_categoria) VALUES (?)
                            ''', (categoria,))
                        cursor.execute('SELECT ID FROM Categoria WHERE Nombre_categoria = ?', (categoria,))
                        categorias[categoria] = cursor.fetchone()[0]
                        if cursor.rowcount > 0:
                            filas_insertadas += 1
                            registrar_actividad(f"Datos insertados en la tabla Categoria.", {'ID': categorias[categoria], 'Nombre_categoria': row['Categoria']})
            conexion.commit()
            if filas_insertadas == 0:
                print("No se efectuó ningún cambio: no se insertaron nuevos elementos en la tabla Categoria.")
    except Exception as e:
        manejar_excepcion(e)
    return categorias

def obtener_sector_ids(datos):
    sectores = {}
    filas_insertadas = 0
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            for row in datos:
                if 'Sector' in row:
                    sector = row['Sector']
                    if sector not in sectores:
                        cursor.execute(
                            '''
                            INSERT OR IGNORE INTO Sector (Nombre_sector) VALUES (?)
                            ''', (sector,))
                        cursor.execute('SELECT ID FROM Sector WHERE Nombre_sector = ?', (sector,))
                        sectores[sector] = cursor.fetchone()[0]
                        if cursor.rowcount > 0:
                            filas_insertadas += 1
                            registrar_actividad(f"Datos insertados en la tabla Sector.", {'ID': sectores[sector], 'Nombre_sector': row['Sector']})
            conexion.commit()
            if filas_insertadas == 0:
                print("No se efectuó ningún cambio: no se insertaron nuevos elementos en la tabla Sector.")
    except Exception as e:
        manejar_excepcion(e)
    return sectores

def insertar_certificados(datos, regimenes, categorias, sectores):
    filas_insertadas = 0
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            for row in datos:
                if 'ID' in row and 'Emision_certificado' in row and 'Vencimiento_certificado' in row:
                    regimen_id = regimenes.get(row['Regimen_Tributario'], None)
                    categoria_id = categorias.get(row['Categoria'], None)
                    sector_id = sectores.get(row['Sector'], None)

                    if regimen_id and categoria_id and sector_id and 'ID_provincia' in row:
                        cursor.execute(
                            '''
                            INSERT OR IGNORE INTO Certificados_MiPyME (ID, Regimen_Tributario_ID, Emision_certificado, Vencimiento_certificado, Categoria_ID, Sector_ID, Provincia_ID, CLAE6, Vigente) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''',
                            (
                                row['ID'],
                                regimen_id,
                                row['Emision_certificado'],
                                row['Vencimiento_certificado'],
                                categoria_id,
                                sector_id,
                                row['ID_provincia'],
                                row['CLAE6'],
                                row['Vigente']
                            ))
                        if cursor.rowcount > 0:
                            filas_insertadas += 1
                            registrar_actividad(f"Datos insertados en la tabla Certificados_MiPyME.", {'ID': row['ID'], 'Regimen_Tributario_ID': regimen_id, 'Emision_certificado': row['Emision_certificado'], 'Vencimiento_certificado': row['Vencimiento_certificado'], 'Categoria_ID': categoria_id, 'Sector_ID': sector_id, 'Provincia_ID': row['ID_provincia'], 'CLAE6': row['CLAE6'], 'Vigente': row['Vigente']})
            conexion.commit()
            if filas_insertadas == 0:
                print("No se efectuó ningún cambio: no se insertaron nuevos elementos en la tabla Certificados_MiPyME.")
    except Exception as e:
        manejar_excepcion(e)

def cargar_datos_certificados(datos):
    try:
            insertar_provincia(datos)
            regimenes = obtener_regimen_ids(datos)
            categorias = obtener_categoria_ids(datos)
            sectores = obtener_sector_ids(datos)
            insertar_certificados(datos, regimenes, categorias, sectores)
    except Exception as e:
        manejar_excepcion(e)
