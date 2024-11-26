import funciones_json
from  ClaseConexion import Conexion_MySQL

conexion = Conexion_MySQL()

cursor = conexion.cursor()

tarjetas_veterinarios = []
identificaciones = []


def agregar_veterinarios(cursor, conexion):
    tarjetas_veterinarios = funciones_json.abrir_json_veterinarios()
    tarjeta_profesional = int(input("Ingrese el numero de la tarjeta profesional: ").strip())

    tarjeta_switch = funciones_json.verificar_identificadores_unicos(tarjetas_veterinarios,tarjeta_profesional)

    if tarjeta_switch:
        
        identificacion = int(input("Ingrese la identificación: "))
        if identificacion != tarjeta_profesional:
            id_switch = funciones_json.verificar_identificadores_unicos(tarjetas_veterinarios, identificacion)

            if id_switch:
                print("Todo correcto, ahora llenado de datos...")
                nombre = input("Ingrese el nombre: ")
                direccion = input("Ingrese la direccion: ")
                telefono = input("Ingrese el telefono: ")
                correo = input("Ingrese el correo: ")

                sql = "INSERT INTO veterinarios (tarjeta_profesional, id_veterinario, nombre_veterinario, direccion_veterinario, telefono_veterinario, correo_veterinario) VALUES (%s, %s, %s, %s, %s, %s)"

                valores = (tarjeta_profesional,identificacion, nombre, direccion, telefono, correo)
                # Se procede a hacer el llenado de los datos al veterinario y registrarlos a la base de datos

                cursor.execute(sql, valores)
                conexion.commit()

                tarjetas_veterinarios.append({'tarjeta_profesional':tarjeta_profesional,'identificacion':identificacion})
                funciones_json.actualizar_json_veterinarios(tarjetas_veterinarios)
            else:
                print("Numero de Identificacion incorrecto! corresponde a un ID o Tarjeta profesional existente!")
        else:
            print("La identificacion tiene que ser diferente a la tarjeta profesional!")
    else:
        print("Numero de Tarjeta profesional incorrecto!, corresponde a un ID o Tarjeta profesional existente!")

agregar_veterinarios(cursor, conexion)

