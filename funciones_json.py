import json

def abrir_json_veterinarios():
    try:
        with open('tarjetas_veterinarios.json', 'r') as archivo_json:
            tarjetas_veterinarios = json.load(archivo_json)
    except FileNotFoundError:
        tarjetas_veterinarios = []
    return tarjetas_veterinarios

def verificar_tarjetas_veterinarios(tarjetas_veterinarios,tarjeta_profesional):

    tarjeta_switch = True
    for diccionario in tarjetas_veterinarios:
        if diccionario['tarjeta_profesional'] == tarjeta_profesional:
            tarjeta_switch = False
            break
    return tarjeta_switch


def actualizar_json_veterinarios(tarjetas_veterinarios):
    with open('tarjetas_veterinarios.json', 'w') as archivo_json:
        json.dump(tarjetas_veterinarios, archivo_json)