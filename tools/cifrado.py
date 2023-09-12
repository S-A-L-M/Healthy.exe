from cryptography.fernet import Fernet
import json

# Genera una clave de cifrado basada en la contraseña proporcionada
def generar_clave(contraseña):
    return Fernet.generate_key()

# Guarda la clave de cifrado en un archivo
def guardar_clave(clave, nombre_archivo='clave.key'):
    with open(nombre_archivo, 'wb') as archivo_clave:
        archivo_clave.write(clave)

# Carga la clave de cifrado desde un archivo
def cargar_clave(nombre_archivo='clave.key'):
    return open(nombre_archivo, 'rb').read()

# Encripta el contenido de un archivo
def encriptar_archivo(clave, nombre_archivo_entrada, nombre_archivo_salida):
    fernet = Fernet(clave)
    with open(nombre_archivo_entrada, 'rb') as archivo_entrada:
        contenido = archivo_entrada.read()
        contenido_cifrado = fernet.encrypt(contenido)
    with open(nombre_archivo_salida, 'wb') as archivo_salida:
        archivo_salida.write(contenido_cifrado)

# Desencripta el contenido de un archivo
def desencriptar_archivo(clave, nombre_archivo_entrada, nombre_archivo_salida):
    fernet = Fernet(clave)
    with open(nombre_archivo_entrada, 'rb') as archivo_entrada:
        contenido_cifrado = archivo_entrada.read()
        contenido_descifrado = fernet.decrypt(contenido_cifrado)
    with open(nombre_archivo_salida, 'wb') as archivo_salida:
        archivo_salida.write(contenido_descifrado)

# Pregunta al usuario si desea cifrar o descifrar el archivo
def main():
    opcion = input("¿Deseas encriptar (E) o desencriptar (D) el archivo? ").upper()
    if opcion == 'E':
        contraseña = input("Ingresa la contraseña para encriptar el archivo: ")
        clave = generar_clave(contraseña.encode())
        guardar_clave(clave)
        encriptar_archivo(clave, 'Hexe.py', 'Hexe_encriptado.py')
        print("Archivo encriptado exitosamente como 'Hexe_encriptado.py'")
    elif opcion == 'D':
        contraseña = input("Ingresa la contraseña para desencriptar el archivo: ")
        clave = cargar_clave()
        desencriptar_archivo(clave, 'Hexe_encriptado.py', 'Hexe_desencriptado.py')
        print("Archivo desencriptado exitosamente como 'Hexe_desencriptado.py'")
    else:
        print("Opción inválida. Ingresa 'E' para encriptar o 'D' para desencriptar....")

if __name__ == "__main__":
    main()
