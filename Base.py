import os
import ipaddress

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            filas = archivo.readlines()
            for fila in filas:
                print(fila.strip())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def validar_direccion_ip(direccion_ip):
    try:
        ipaddress.ip_address(direccion_ip)
        return True
    except ValueError:
        return False

def generar_lista():
    lista = []
    zona = input("Ingrese nombre de la zona en que operan los dispositivos: ")
    dispositivo = input("Ingrese dispositivo que pertenece a la zona: ")
    interfaz = input("Ingrese la interfaz conectada: ")
    direccion_ip = input("Ingrese la dirección IP de la interfaz: ")
    while not validar_direccion_ip(direccion_ip):
        print("Dirección IP inválida. Por favor, ingrese una dirección IP válida.")
        direccion_ip = input("Ingrese la dirección IP de la interfaz: ")
    mascara = input("Ingrese la máscara de red en la que trabaja la interfaz: ")
    destino = input("Ingrese nombre del dispositivo de destino: ")
    capa_jerarquica = input("Ingrese la capa jerárquica perteneciente al equipo: ")
    protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: ")
    servicios_de_red = input("Ingrese los servicios de red disponibles en el dispositivo: ")

    lista.append(
        f"{zona}\t{dispositivo}\t{interfaz}\t{direccion_ip}\t{mascara}\t{destino}\t{capa_jerarquica}\t{protocolos_de_red}\t{servicios_de_red}\n"
    )

    return lista

def agregar_al_archivo(nombre_archivo):
    lista = generar_lista()

    with open(nombre_archivo, 'a') as archivo:
        for elemento in lista:
            archivo.write(elemento)

def reemplazar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

        print("Contenido del archivo:")
        for i, linea in enumerate(contenido):
            print(f"{i+1}. {linea.strip()}")

        num_linea = int(input("Ingrese el número de línea en el que desea realizar el reemplazo: ")) - 1
        texto_actual = contenido[num_linea].strip()
        nuevo_texto = input("Ingrese el nuevo texto: ")

        contenido[num_linea] = contenido[num_linea].replace(texto_actual, nuevo_texto)

        with open(nombre_archivo, 'w') as archivo:
            archivo.writelines(contenido)

        print("Texto reemplazado exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except IndexError:
        print("Número de línea inválido.")

def menu_principal():
    nombre_archivo = 'GRUPO-7.txt'

    while True:
        os.system("clear")
        print("--------------MENU-------------------")
        print("1. Leer archivo GRUPO-7.txt")
        print("2. Agregar al archivo GRUPO-7.txt")
        print("3. Reemplazar texto en archivo GRUPO-7.txt")
        print("4. Salir.")
        print("-------------------------------------")

        opcion = input("Ingrese la opción que desea realizar: ")

        if opcion == "1":
            leer_archivo(nombre_archivo)
            input("Presione Enter para continuar...")
        elif opcion == "2":
            agregar_al_archivo(nombre_archivo)
            input("Presione Enter para continuar...")
        elif opcion == "3":
            reemplazar_texto(nombre_archivo)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            break
        else:
            input("Opción inválida. Presione Enter para continuar...")

menu_principal()
