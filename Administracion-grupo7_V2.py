import os
import ipaddress

def mostrar_menu():
    print("--------------MENU-------------------")
    print("1. Leer archivo GRUPO-7.txt")
    print("2. Agregar al archivo GRUPO-7.txt")
    print("3. Agregar interfaz")
    print("4. Reemplazar texto en archivo GRUPO-7.txt")
    print("5. Salir.")
    print("-------------------------------------")

def leer_opcion():
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ['1', '2', '3', '4', '5']:
            return opcion
        else:
            print("Opción inválida. Intente nuevamente.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def generador_lista():
    listas = []

    while True:
        lista = []
        i = 0
        zona = input("Ingrese nombre de la zona en que operan los dispositivos: ")
        i += 1
        dispositivo = input("Ingrese dispositivo que pertenece a la zona: ")
        i += 1
        interfaz = input("Ingrese la interfaz conectada: ")
        i += 1

        while True:
            direccion_ip = input("Ingrese la dirección IP de la interfaz antes mencionada: ")
            if validar_direccion_ip(direccion_ip):
                i += 1
                break
            else:
                print("Dirección IP inválida. Favor de ingresar una dirección IP válida.")

        while True:
            mascara = int(input("Ingrese máscara de red en la que trabaja la interfaz: "))
            if 0 <= mascara <= 32:
                mascara = str(mascara)
                i += 1
                break
            elif mascara <= 0 or mascara > 30:
                print("La máscara de red ha sido ingresada de forma incorrecta.")

        destino = input("Ingrese nombre del dispositivo de destino: ")
        i += 1
        capa_jerarquica = input("Ingrese la capa jerárquica perteneciente al equipo: ")
        i += 1
        servicios_adheridos = input("Ingrese los servicios que están disponibles en el dispositivo: ")
        i += 1
        protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: ")
        i += 1

        lista.append(
            zona + "\t" + dispositivo + "\t" + interfaz + "\t" + direccion_ip + "/" + mascara + "\t" + destino + "\t" + capa_jerarquica + "\t" + servicios_adheridos + "\t" + protocolos_de_red
        )

        listas.append(lista)

        respuesta = input("Desea agregar otro dispositivo a la lista (S/N)? ")
        if respuesta.lower() != 's':
            break

    return listas

def agregar_al_archivo(nombre_archivo):
    listas = generador_lista()

    with open(nombre_archivo, 'a') as archivo:
        for lista in listas:
            archivo.write('\n'.join(lista) + '\n')

    print("Los dispositivos han sido agregados correctamente al archivo.")

def agregar_interfaz(listas):
    zona = ""
    dispositivo = "\t"
    interfaz = input("Ingrese la interfaz conectada: ")
    while True:
        direccion_ip = input("Ingrese la dirección IP de la interfaz antes mencionada: ")
        if validar_direccion_ip(direccion_ip):
            break
        else:
            print("Dirección IP inválida. Favor de ingresar una dirección IP válida.")
    while True:
        mascara = int(input("Ingrese la máscara de red en la que trabaja la interfaz: "))
        if 0 <= mascara <= 32:
            mascara = str(mascara)
            break
        else:
            print("La máscara de red ha sido ingresada de forma incorrecta.")
    destino = input("Ingrese el nombre del dispositivo de destino: ")
    capa_jerarquica = "\t"
    servicios_adheridos = "\t"
    protocolos_de_red = "\t"
    lista = [
        zona
        + "\t"
        + dispositivo
        + "\t"
        + interfaz
        + "\t"
        + direccion_ip
        + "/"
        + mascara
        + "\t"
        + destino
        + "\t"
        + capa_jerarquica
        + "\t"
        + servicios_adheridos
        + "\t"
        + protocolos_de_red
        + "\n"
    ]
    listas.append(lista)

def agregar_interfaz_al_archivo(nombre_archivo):
    listas = []

    while True:
        agregar_interfaz(listas)
        respuesta = input("Desea agregar otra interfaz (S/N)? ")
        if respuesta.lower() != 's':
            break

    with open(nombre_archivo, 'a') as archivo:
        for lista in listas:
            archivo.write('\n'.join(lista))

    print("Las interfaces han sido agregadas correctamente al archivo.")

def reemplazar_texto(nombre_archivo):
    buscar = input("Ingrese el texto que desea buscar: ")
    reemplazar = input("Ingrese el texto con el que desea reemplazar: ")

    try:
        with open(nombre_archivo, 'r+') as archivo:
            contenido = archivo.read()
            contenido_modificado = contenido.replace(buscar, reemplazar)
            archivo.seek(0)
            archivo.write(contenido_modificado)
            archivo.truncate()

        print("El texto ha sido reemplazado correctamente en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def menu_principal():
    nombre_archivo = 'GRUPO-7.txt'

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == '1':
            leer_archivo(nombre_archivo)
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        elif opcion == '2':
            agregar_al_archivo(nombre_archivo)
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        elif opcion == '3':
            agregar_interfaz_al_archivo(nombre_archivo)
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        elif opcion == '4':
            reemplazar_texto(nombre_archivo)
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        elif opcion == '5':
            break

if __name__ == '__main__':
    menu_principal()
