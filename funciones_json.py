import json

def abrir_json_veterinarios():
    try:
        with open('tarjetas_veterinarios.json', 'r') as archivo_json:
            tarjetas_veterinarios = json.load(archivo_json)
    except FileNotFoundError:
        tarjetas_veterinarios = []
    return tarjetas_veterinarios

def verificar_identificadores_unicos(json_lista, identificador):
    switch = True
    for diccionario in json_lista:
        if diccionario['tarjeta_profesional'] == identificador or diccionario['identificacion'] == identificador:
            switch = False
            break
    return switch

def actualizar_json_veterinarios(tarjetas_veterinarios):
    with open('tarjetas_veterinarios.json', 'w') as archivo_json:
        json.dump(tarjetas_veterinarios, archivo_json)

