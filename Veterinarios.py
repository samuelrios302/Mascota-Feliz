import funciones_json
from  ClaseConexion import Conexion_MySQL

conexion = Conexion_MySQL()

cursor = conexion.cursor()

tarjetas_veterinarios = []


def agregar_veterinarios(cursor, conexion):
    tarjetas_veterinarios = funciones_json.abrir_json_veterinarios()
    tarjeta_profesional = int(input("Ingrese el numero de la tarjeta profesional: ").strip())

    tarjeta_switch = funciones_json.verificar_tarjetas_veterinarios(tarjetas_veterinarios,tarjeta_profesional)

    if tarjeta_switch:
        print("Se agrego la tarjeta")
    else:
        print("tarjeta ya existente")

agregar_veterinarios(cursor, conexion)