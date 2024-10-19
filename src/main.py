import time
from imports import importar_csv
from db import crear_tabla, cargar_datos_certificados
from config import esquema
from logger import manejar_excepcion

def main():
    try:
        print("\n##### Inicio de creación de las tablas SQL #####\n")
        time.sleep(3)
        for nombre_tabla, columnas in esquema.items():
              crear_tabla(nombre_tabla, columnas)
        print("\n##### Creación de las tablas SQL finalizado #####\n")

        print("\n##### Inicio de importación de datos de archivos CSV #####")
        time.sleep(3)
        datos_csv = importar_csv("../data/registro_mipyme_parte_1.csv")
        print("##### Importación de datos finalizada #####\n")

        print("\n##### Carga de datos en SQLite #####\n")
        time.sleep(3)
        cargar_datos_certificados(datos_csv)
        print("\n##### Carga de datos finalizada #####\n")

    except Exception as e:
        manejar_excepcion(e)


if __name__ == "__main__":
    main()