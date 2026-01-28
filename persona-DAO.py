from DATOS.conexion import Conexion
from DOMINIO.persona import Persona


class PersonaDAO:
    _INSERT = ("INSERT INTO Personas (nombres, apellidos, cedula, sexo, email)"
               "VALUES (?, ?, ?, ?, null)")

    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula, persona.sexo,)
                cursor.execute(cls._INSERT, datos)
                respuesta = cursor.rowcount
                if respuesta ==1:
                    return{'ejecuto':True, 'mensaje':'se guardo con exito'}
        except bd.IntegrityError as e_bb:
                print(f'Error en la cedula: {e_bb}')
                return {'ejecuto': False, 'mensaje': 'cedula ya existe'}

            'except Exception as e:'
            'print(f'Error general:{e}')'
            'print(type(e)))'
            'returnreturn {'ejecuto':false, 'mensaje'}'


if __name__ == '__main__':
    p1 = Persona(cedula="0954556688", nombre="Genesis", apellido="Garboa", sexo="Femenino")
    PersonaDAO().insertar_persona(p1)
