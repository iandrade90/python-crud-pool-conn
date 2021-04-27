from conexion import Conexion
from logger_base import logger

class CursorDelPool():
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    #Inicio de with
    def __enter__(self):
        logger.debug('Inicio de metodo with')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    #Fin del bloque with

    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta metodo exit')
        #Se pueden colocar cualquiera de las dos sintaxis
        #if exception_value is not None:
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una execepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit de la transaccion')
        #Cerramos el cursor
        self.__cursor.close()
        #Regresar la conexion al pool
        Conexion.liberarConexion(self.__conn)

#if __name__ == "__main__":
    #Obtenemos un cursor a partir de la conexion del pool
    #with se ejecuta __enter__ y termina con __exit__
#    with CursorDelPool() as cursor:
#        pass
