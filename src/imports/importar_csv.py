import csv

def importar_csv(ruta_archivo):
    try:
        with open(ruta_archivo, newline='') as csvfile:
            lector = csv.DictReader(csvfile)
            datos = [fila for fila in lector]
        return datos
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta_archivo} no fue encontrado.")
    except PermissionError:
        raise PermissionError(f"No tienes permisos para acceder a este archivo ({ruta_archivo}).")
    except Exception as e:
        raise e
