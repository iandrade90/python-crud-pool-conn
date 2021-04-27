from persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import logger

class PersonaDao():

    #Data Access Object

    __SELECCIONAR = 'SELECT * FROM persona ORDER BY persona_id'
    __INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    __BORRAR = 'DELETE FROM persona WHERE persona_id = %s'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE persona_id=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Datos a ingresar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Datos a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_personaid())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def borrar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__BORRAR))
            logger.debug(f'Datos a borrar: {persona}')
            valor = (persona.get_personaid(),)
            cursor.execute(cls.__BORRAR, valor)
            return cursor.rowcount

if __name__ == "__main__":
    #Codigo para LEER la base de datos
    personas = PersonaDao.seleccionar()
    for persona in personas:
       logger.debug(persona)

    #Codigo para CREAR nuevo registro en la base de datos
    #persona = Persona(nombre='Florecia', apellido='Andrade', email='floandrade@mail.com')
    #nuevoRegistro = PersonaDao.insertar(persona)
    #logger.debug(f'Registros insertados: {nuevoRegistro}')

    #Codigo para ACTUALIZAR registro
    #persona = Persona(36, 'Flore', 'Andrade', 'flore@mail.com')
    #registroActualizado = PersonaDao.actualizar(persona)
    #logger.debug(f'Registro actualizado: {registroActualizado}')

    #Codigo para BORRAR registro
    #persona = Persona(id_persona=7)
    #registroBorrar = PersonaDao.borrar(persona)
    #logger.debug(f'Registro borrado: {registroBorrar}')
