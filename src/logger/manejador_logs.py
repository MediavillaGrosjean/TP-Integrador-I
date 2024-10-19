import logging

logger = logging.getLogger('actividad')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('../logs/actividad.txt')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def registrar_actividad(mensaje, resultado=None):
    if resultado:
        mensaje_completo = f"{mensaje} Resultado: {resultado}"
    else:
        mensaje_completo = mensaje
    logger.info(mensaje_completo)
    print(f"Actividad registrada: {mensaje_completo}")
