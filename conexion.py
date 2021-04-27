from logger_base import logger
from psycopg2 import pool
import sys

class Conexion():
    __DATABASE = 'testdb'
    __USERNAME = 'postgres'
    __PASSWORD = 'root'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __POOL = None

    @classmethod
    def obtenerPool(cls):
        if cls.__POOL == None:
            try:
                cls.__POOL = pool.SimpleConnectionPool(
                                                        cls.__MIN_CON,
                                                        cls.__MAX_CON,
                                                        user = cls.__USERNAME,
                                                        password = cls.__PASSWORD,
                                                        host = cls.__HOST,
                                                        port = cls.__DB_PORT,
                                                        database = cls.__DATABASE)
                logger.debug(f'Creacion de pool exitosa: {cls.__POOL}')
                return cls.__POOL
            except Exception as error:
                logger.error(f'Error al crear el pool de conexiones: {error}')
                sys.exit()
        else:
            return cls.__POOL

    @classmethod
    def obtenerConexion(cls):
        conexion = Conexion.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__POOL}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__POOL}')

#if __name__ == "__main__":
    #Obetener conexion con pool
#    conexion1 = Conexion.obtenerConexion()
#    conexion2 = Conexion.obtenerConexion()
#    conexion3 = Conexion.obtenerConexion()
    
    #Liberar conexiones
#    Conexion.liberarConexion(conexion1)
#    Conexion.liberarConexion(conexion3)

    #Cerrar conexiones
#    Conexion.cerrarConexiones()
