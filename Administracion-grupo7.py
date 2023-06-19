import os
import curses
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
    listas = []  # Matriz para almacenar las listas generadas

    while True:
        zona = input("Ingrese nombre de la zona en la que operan los dispositivos: ")
        dispositivo = input("Ingrese el dispositivo que pertenece a la zona: ")
        interfaz = input("Ingrese la interfaz conectada: ")
        
        while True:
            direccion_ip = input("Ingrese la dirección IP de la interfaz antes mencionada: ")
            if validar_direccion_ip(direccion_ip):
                break
            else:
                print("Dirección IP inválida. Por favor, ingrese una dirección IP válida.")

        while True:
            mascara = int(input("Ingrese la máscara de red en la que trabaja la interfaz: "))
            if 0 < mascara <= 32:
                break
            else:
                print("La máscara de red ha sido ingresada incorrectamente.")

        destino = input("Ingrese el nombre del dispositivo de destino: ")
        capa_jerarquica = input("Ingrese la capa jerárquica perteneciente al equipo: ")
        servicio_adheridos = input("Ingrese los servicios disponibles en el dispositivo: ")
        protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: ")

        lista = [
            zona,
            dispositivo,
            interfaz,
            direccion_ip,
            "/" + str(mascara),
            destino,
            capa_jerarquica,
            protocolos_de_red,
            servicio_adheridos
        ]
        listas.append(lista)

        agregar_interfaz = input("¿Desea agregar una nueva interfaz? (S/N): ")
        if agregar_interfaz.lower() != "s":
            break

    return listas

def agregar_al_archivo(nombre_archivo):
    lista = generar_lista()

    with open(nombre_archivo, 'a') as archivo:
        for elemento in lista:
            archivo.write("\t".join(elemento) + "\n")

    print("Datos agregados al archivo exitosamente.")

def reemplazar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

        print("Contenido del archivo:")
        for i, linea in enumerate(contenido):
            print(f"{i+1}. {linea.strip()}")

        num_linea = int(input("Ingrese el número de línea en el que desea realizar el reemplazo: ")) - 1
        if 0 <= num_linea < len(contenido):
            texto_actual = contenido[num_linea].strip()
            nuevo_texto = input("Ingrese el nuevo texto: ")

            contenido[num_linea] = contenido[num_linea].replace(texto_actual, nuevo_texto)

            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(contenido)

            print("Texto reemplazado exitosamente.")
        else:
            print("Número de línea inválido.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

import curses

def mostrar_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("--------------MENU-------------------\n")
    stdscr.addstr("1. Leer archivo GRUPO-7.txt\n")
    stdscr.addstr("2. Agregar al archivo GRUPO-7.txt\n")
    stdscr.addstr("3. Reemplazar texto en archivo GRUPO-7.txt\n")
    stdscr.addstr("4. Salir.\n")
    stdscr.addstr("-------------------------------------\n")
    stdscr.refresh()

def leer_opcion(stdscr):
    while True:
        key = stdscr.getch()
        if key in [ord('1'), ord('2'), ord('3'), ord('4')]:
            return chr(key)
        else:
            stdscr.addstr("Opción inválida. Intente nuevamente.\n")
            stdscr.refresh()

def limpiar_pantalla(stdscr):
    stdscr.clear()
    stdscr.refresh()

def esperar_confirmacion(stdscr):
    stdscr.addstr("Presione Enter para continuar...")
    stdscr.refresh()
    stdscr.getch()

def menu_principal(stdscr):
    nombre_archivo = 'GRUPO-7.txt'

    while True:
        mostrar_menu(stdscr)
        opcion = leer_opcion(stdscr)

        if opcion == '1':
            leer_archivo(nombre_archivo)
            esperar_confirmacion(stdscr)
        elif opcion == '2':
            agregar_al_archivo(nombre_archivo)
            esperar_confirmacion(stdscr)
        elif opcion == '3':
            reemplazar_texto(nombre_archivo)
            esperar_confirmacion(stdscr)
        elif opcion == '4':
            break

        limpiar_pantalla(stdscr)

curses.wrapper(menu_principal)

