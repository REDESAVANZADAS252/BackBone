import os
import time
import ipaddress # Para intrducior direcciones IP
import platform
def ficheros():
    directory = os.getcwd()  #Carpeta donde se encuentra actualmente
    files = os.listdir(directory)  #Obtiene todos los archivos de la carpeta
    txt_files = [file for file in files if file.endswith('.txt')]  #filtra solos los archivos .txt
    print(txt_files)

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
listas = []# Crear una lista vacía para almacenar las listas de elementos
#matriz = ["ZONA","\t","DISPOSITIVO","\t","INTERFAZ","\t","IP","\t","\t","MASCARA","\t","\t","DESTINO","\t","\t","CAPA JERÁRQUICA","\t","PROTOCOLOS DE RED","\t","SERVICIOS DE RED","\n"]#encabezado de la documentacion
#listas.append(matriz)

def leer_documento_txt():
    clear_screen()
    filas = [] # Lista para almacenar las filas del documento
    try:
        with open(nombre_archivo, 'r') as archivo: # Abrir el archivo en modo lectura
            contents = archivo.read() 
            print(contents)
            while True:
                print("Desea prolongar su sesion de lectura? (S/N)")
                sesion = input()
                if sesion == "s" or sesion == "S":
                    clear_screen()
                    print(contents)
                    time.sleep(10)
                elif sesion == "n" or sesion == "N":
                    break
            for linea in archivo: # Leer cada línea del archivo
                fila = linea.strip("\n") # Eliminar el salto de línea al final de cada línea
                filas.append(fila) # Agregar la fila a la lista
        return filas
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None

def validador_IP(direccion_ip):
    try:
        ipaddress.ip_address(direccion_ip)
        return True
    except ValueError:
        return False

def generador_lista():# Solicitar al usuario que ingrese elementos
    clear_screen()
    while True:
        lista = []  # Crear una nueva lista vacía para cada iteración
        while True:
            i = 0
            zona = input("Ingrese nombre de la zona en que operan los dispositivos: "); i = i +1 #zona en la que trabajan los equipos
            largo = len(zona)
            if largo < 8:
                zona = zona+"\t"
            elif largo > 8:
                zona
            dispositivo = input("Ingrese nombre del dispositivo que pertenece a la zona: \n(ROUTER/MULTICAPA/SWITCH) (XX) [EJEMPLO: ROUTER 05] "); i = i +1
            cadena = len(dispositivo) #nombre del dispositivo
            if cadena < 8:
                dispositivo = dispositivo+"\t"
            elif cadena > 7:
                dispositivo
            interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X) [POR EJEMPLO: ETHER 0/1]: "); i = i +1 #numero de interfaz
            while True:
                direccion_ip = input("Ingrese la direccion ip de la interfaz: (POR EJEMPLO: 192.168.1.10) "); #direccion ip de la interfaz
                if validador_IP(direccion_ip):
                    i = i +1
                    break
                else:
                    print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
            while True:
                mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: \n(Solo debe ingresar el prefijo de la red sin (/) EJ: 24) "))#Mascara de red de la interfaz
                if mascara > 0 and mascara <= 32:
                    mascara = str(mascara); i = i + 1 #Mascara de red de la interfaz 
                    break
                elif mascara <= 0 or mascara > 32:
                    print("La mascara de red ha sido ingresada erroneamente.")
            destino = input("Ingrese nombre del dispositvo de destino: \n(ROUTER/MULTICAPA/SWITCH) (XX) [EJEMPLO: ROUTER 05] "); i = i + 1 #destino de la interfaz o hacia donde llegará esa interfaz
            capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo \n(NUCLEO, DISTRIBUCION, ACCESO): "); i = i +1 #jerarquia perteneciente al equipo
            servicio_adheridos = input("Ingrese los servicios que estan disponibles en el dispositivo: "); i = i +1 #servicios que estan configurados en el equipo
            protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: \n[POR EJEMPLO: OSPF10 ÁREA 0] "); i = i +1 #protocolos de red que tiene configurado el equipo
            lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n"); i = i +1 #se agrega las variables a una lista
            if i == 10:
                break
        listas.append(lista)  # Agregar la lista actual a la matriz lista
        clear_screen()
        while True:
            agregar = input("Desea agregar una nueva interfaz? (S/N) ") #se agrega interfaces adicionales del equipo en caso de tenerlas
            if agregar == "Si" or agregar == "si" or agregar == "SI" or agregar == "S" or agregar == "s":
                zona = ""
                dispositivo = "\t\t"
                interfaz = input("Ingrese la interfaz conectada:\n(SERIAL/FASTETH/GIGABIT/ETHER)(X/X) o (X/X/X) [POR EJEMPLO: ETHER 0/1]: "); #numero de interfaz
                while True:
                    direccion_ip = input("Ingrese la direccion ip de la interfaz: (POR EJEMPLO: 192.168.1.10) "); #direccion ip de la interfaz
                    if validador_IP(direccion_ip):
                        break
                    else:
                        print("direccion ip invalida. Favor de ingresar un direccion ip valida.")
                while True:
                    mascara = int(input("Ingrese mascara de red en la que trabaja la interfaz: \n(Solo debe ingresar el prefijo de la red sin (/) EJ: 24) "))#Mascara de red de la interfaz
                    if mascara >= 0 and mascara <= 32:
                        mascara = str(mascara)
                        break
                    elif mascara < 0 or mascara > 32:
                        print("La mascara de red ha sido ingresada erroneamente.")
                destino = input("Ingrese nombre del dispositvo de destino: \n(ROUTER/MULTICAPA/SWITCH) (XX) [EJEMPLO: ROUTER 05] ")
                capa_jerarquica = input("Ingrese la capa jerarquica perteneciente al equipo \n(NUCLEO, DISTRIBUCION, ACCESO): ")
                servicio_adheridos = "\t"
                protocolos_de_red = input("Ingrese los protocolos de enrutamiento del dispositivo: \n[POR EJEMPLO: OSPF10 ÁREA 0] ")
                lista.append(zona+"\t"+dispositivo+"\t"+interfaz+"\t"+direccion_ip+"\t"+"/"+mascara+"\t"+"\t"+destino+"\t"+capa_jerarquica+"\t"+"\t"+protocolos_de_red+"\t"+"\t"+servicio_adheridos+"\n") #agrega una lista de la interfaz configurada 
                clear_screen()
            elif agregar == "N" or agregar == "n" or agregar == "no" or agregar == "NO" or agregar == "No":
                break
        clear_screen()
        continuar = input("¿Deseas crear otra lista? (s/n): ") #creamos otra lista para otro dispositivo.
        if continuar.lower() == "N" or continuar.lower() == "n":
            break

def reemplazar(nombre_archivo):
    clear_screen()
    def leer_documento_txt(nombre_archivo):
        filas = []  # Lista para almacenar las filas del documento
        try:
            with open(nombre_archivo, 'r') as archivo:  # Abrir el archivo en modo lectura
                for linea in archivo:  # Leer cada línea del archivo
                    fila = linea.strip("\n")  # Eliminar el salto de línea al final de cada línea
                    filas.append(fila)  # Agregar la fila a la lista
            return filas
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe.")
            return None
    def reemplazar_texto(filas, num_fila, texto_reemplazar):
        if num_fila < 1 or num_fila > len(filas):  # Verificar si el número de fila es válido
            print("Número de fila inválido.")
            return filas
        fila_actualizada = filas[num_fila - 1].replace(texto_buscar, texto_reemplazar)  # Realizar el reemplazo de texto en la fila seleccionada
        filas_actualizadas = filas.copy()  # Actualizar la lista de filas
        filas_actualizadas[num_fila - 1] = fila_actualizada
        return filas_actualizadas
    def guardar_documento_txt(nombre_archivo, filas):
        try:
            with open(nombre_archivo, 'w') as archivo:  # Abrir el archivo en modo escritura
                for fila in filas:  # Escribir cada fila en el archivo
                    archivo.write(fila + '\n')
            print(f"El documento se ha guardado en '{nombre_archivo}'.")
        except:
            print(f"No se pudo guardar el documento en '{nombre_archivo}'.")
    # Leer el documento y guardar las filas en una lista
    filas_documento = leer_documento_txt(nombre_archivo)
    if filas_documento:
        print("Contenido del documento:")  # Imprimir las filas del documento
        for i, fila in enumerate(filas_documento):
            print(f"{i+1}. {fila}")
        texto_buscar = str(input("Ingrese el parámetro a cambiar: "))
        num_fila = int(input("Ingrese el número de fila en el que desea realizar el reemplazo: "))  # Pedir al usuario el número de fila para reemplazar el texto
        if num_fila < 1 or num_fila > len(filas_documento):  # Verificar si el número de fila es válido
            print("Número de fila inválido.")
        else:
            texto_reemplazar = input("Ingrese el texto con el que desea reemplazar: ")  # Pedir al usuario el texto con el que desea reemplazar
            filas_actualizadas = reemplazar_texto(filas_documento, num_fila, texto_reemplazar)  # Realizar el reemplazo de texto en la fila seleccionada
            print("\nContenido del documento actualizado:")  # Imprimir las filas actualizadas
            for i, fila in enumerate(filas_actualizadas):
                print(f"{i+1}. {fila}")
            guardar_documento_txt(nombre_archivo, filas_actualizadas)  # Guardar el documento actualizado

def leer_y_copiar_archivo(archivo_a_copiar, archivo_a_agregar): #Funcion para Copiar el contenido de un archivo y pegar el contenido en otro archivo
    try:
        with open(archivo_a_copiar, 'r') as archivo:
            contenido = archivo.read()
        with open(archivo_a_agregar, 'a') as archivo_nuevo:
            archivo_nuevo.write(contenido); print("Archivo copiado exitosamente.")
    except FileNotFoundError:
        print("El archivo de entrada no fue encontrado.")

def menu(): #Funcion MENU. Para generar un menú.
    clear_screen()
    print("---------------------------MENU-----------------------------")
    print("1. Ver archivos dentro de la carpeta")
    print("2. Leer algun archivo")
    print("3. Agregar al archivo backbone.txt")
    print("4. Reemplazar Texto en archivo backbone.txt")
    print("5. Copiar y pegar el contenido de un archivo a otro archivo.")
    print("9. Salir.")
    print("\n\n--------------------------------------------------------")

while True: #Codigo Principal
    menu()
    opc = int(input("Ingrese la opcion que desea realizar.\t"))
    if opc == 1: #Ver los Archivos.
        clear_screen(); print("Los archivos dentro de la carpeta son: ")
        ficheros()
        while True:
            opcion = input("Desea regresar al menú: (S/N)  ")
            if opcion == "S" or opcion == "s":
                clear_screen(); break
    elif opc == 2: #Leer algun archivo.
        clear_screen(); ficheros()
        nombre_archivo = input("Ingrese el nombre del archivo para leer los parametros registrados: \n(Ingrese solo el nombre, no coloque la extension .txt)")
        nombre_archivo = nombre_archivo+".txt"; leer_documento_txt()
        clear_screen()
    elif opc == 3: #Ingresar parametros a algun archivo.
        ficheros()
        nombre_archivo = input("Ingrese el nombre de archivo donde quiere que sean guardados los parametros registrados: \n(Ingrese solo el nombre, no coloque la extension .txt)")
        nombre_archivo = nombre_archivo+".txt"
        generador_lista()
        for i, lista in enumerate(listas): # Imprimir todas las listas creadas
            print("Lista", i + 1, ":", lista)
        with open(nombre_archivo, 'a') as archivo: #Guarda las listas en un archivo de texto.
            for fila in listas:
                for elements in fila:
                    archivo.write(elements)
        print("Parametros guardados con exito!"); time.sleep(4)
        clear_screen()
    elif opc == 4: #Reemplazar algun parametro de algun archivo
        ficheros()
        nombre_archivo = input("Ingrese el nombre de archivo donde quiere reemplazar los parametros registrados: \n(Ingrese solo el nombre, no coloque la extension .txt)")
        nombre_archivo = nombre_archivo+".txt"
        while True: #Para reemplazar varios parametros en caso de ser necesario.
            reemplazar(nombre_archivo)
            opcion = input("Desea reemplazar algun otro parametro?: (S/N)  ")
            if opcion == "N" or opcion == "n":
                clear_screen(); break
    elif opc == 5: #Copiar y pegar el contienido de un archivo a otro.
        ficheros()
        archivo_a_copiar = input("Ingrese el nombre del archivo del cual se desea copiar el contenido. \n(Solo nombre, sin extension) : ")+".txt"
        archivo_a_agregar = input("Ingrese el nombre del archivo del cual se desea agregar el contenido del archivo copiado. \n(Solo nombre, sin extension) : ")+".txt"
        leer_y_copiar_archivo(archivo_a_copiar, archivo_a_agregar)
    elif opc == 9: #Salir del programa.
        clear_screen(); break
    else:
        print("Opcion erronea.")
