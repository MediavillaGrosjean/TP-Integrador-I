import json

def importar_json(ruta_archivo):
    try:
        with open(ruta_archivo) as jsonfile:
            datos = json.load(jsonfile)
        return datos
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta_archivo} no fue encontrado.")
    except PermissionError:
        raise PermissionError(f"No tienes permisos para acceder a este archivo ({ruta_archivo}).")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error de formato en el archivo JSON: {e}")
    except TypeError as e:
        raise TypeError(f"Error de tipo al serializar JSON: {e}")
    except Exception as e:
        raise e
