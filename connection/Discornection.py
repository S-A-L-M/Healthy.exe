import requests
import json

def obtener_key_desde_config():
    # Lee el archivo config.json y obtiene la key almacenada en él
    try:
        with open('config.json') as config_file:
            config_data = json.load(config_file)
            return config_data.get("Key", "")
    except FileNotFoundError:
        print("Archivo config.json no encontrado.")
        return ""
    except json.JSONDecodeError:
        print("Error al leer el archivo config.json.")
        return ""

def obtener_keys_desde_github(token):
    url = "https://raw.githubusercontent.com/S-A-L-M/Key-H.exe/main/KeysH-exe.json"
    headers = {"Authorization": f"token {token}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            keys_en_github = response.json()["keys"]  # Acceder a la lista de keys dentro del objeto JSON
            return keys_en_github
        else:
            print("Error al obtener las keys desde el Servidor Externo.")
            return []
    except requests.exceptions.RequestException:
        print("Error al hacer la petición al Servidor Externo.")
        return []

def validar_key(key, keys_en_github):
    return key in keys_en_github
