import logging

logger = logging.getLogger('errores')
logger.setLevel(logging.ERROR)

handler = logging.FileHandler('../logs/errores.txt')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def manejar_excepcion(excepcion):
    logger.error(f"Se produjo un error: {str(excepcion)}", exc_info=True)
    print(f"Se ha producido un error: {str(excepcion)}")
