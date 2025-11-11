#Script de Menú con llamado a funciones e importación de módulos
from colorama import *
from funciones.limpiar_pantalla import limpiar_pantalla
from funciones.app import paises_lista
from funciones.Buscar_por_nombre import buscar_pais
from funciones.filtrado import filtrar_continente,filtrar_valor
from funciones.estadisticas import mayor_menor_poblacion, funcion_promedio,ordenar_paises
#Inicializamos colorama
init()
#Función menú interactivo
def menu():
    #Guardamos el retorno de paises_lista en la variable paises
    paises = paises_lista()
    bandera=True
    while bandera==True:
        print(Cursor.FORWARD(30)+Fore.BLACK+Back.GREEN+"=== MENÚ DE OPCIONES ===")
        print(Cursor.FORWARD(30)+Fore.GREEN+Back.BLACK+"1. Buscar país por nombre")
        print(Cursor.FORWARD(30)+Fore.BLACK+Back.GREEN+"2. Filtrar países")
        print(Cursor.FORWARD(30)+Fore.GREEN+Back.BLACK+"3. Ordenar países")
        print(Cursor.FORWARD(30)+Fore.BLACK+Back.GREEN+"4. Mostrar estadísticas")
        print(Cursor.FORWARD(30)+Fore.GREEN+Back.BLACK+"5. Salir")

        opcion = input(Cursor.FORWARD(30)+Fore.BLUE+Back.BLACK+"Ingrese una opción: ").strip()
        limpiar_pantalla()
        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del país: ").capitalize().strip()
                limpiar_pantalla()
                buscar_pais(paises, nombre)
            case "2":
                print("\nOpciones de filtrado:")
                print("a. Por continente")
                print("b. Por rango de población")
                print("c. Por rango de superficie")
                opc = input("Seleccione una opción: ").strip()
                limpiar_pantalla()

                match opc.lower():
                    case "a":
                        continente = input("Ingrese el continente: ").capitalize().strip()
                        filtrar_continente(paises, continente)
                    case "b":
                        min_poblacion = int(input("Población mínima: "))
                        max_poblacion = int(input("Población máxima: "))
                        filtrar_valor(paises,"poblacion", min_poblacion, max_poblacion)
                    case "c":
                        min_area = int(input("Superficie mínima: "))
                        max_area = int(input("Superficie máxima: "))
                        filtrar_valor(paises,"area", min_area, max_area)
            case "3":
                print("\nOpciones de ordenamiento:")
                print("a. Por nombre")
                print("b. Por población")
                print("c. Por superficie")
                categoria = input("Seleccione opción: ").lower()
                limpiar_pantalla()

                match categoria:
                    case "a":criterio="nombre"
                    case "b":criterio="poblacion"
                    case "c":criterio="area"
                    case _:bandera=False
                orden = input("Ascendente (a) o descendente (d)? ").lower() .strip()
                limpiar_pantalla()

                match orden:
                    case "a":orden=False
                    case "d":orden=True
                    case _:bandera=False
                ordenados=ordenar_paises(paises, criterio, orden)

            case "4":
                print("\nOpciones de estadísticas:")
                print("a. País con mayor y menor población")
                print("b. Promedio de población")
                print("c. Promedio de superficie")
                print("d. Cantidad de países por continente")
                seleccion:str = input("Seleccione opción: ").lower()
                limpiar_pantalla()

                match seleccion:
                    case "a": mayor_menor_poblacion(paises)
                    case "b": funcion_promedio(paises,"poblacion")
                    case "c": funcion_promedio(paises,"area")
                    case "d": funcion_promedio(paises,"continente")
            case "5":
                print("¡Hasta luego!")
                bandera=False
            case _:
                print(" Opción inválida. Intente nuevamente.")
            

if __name__ == "__main__":
    menu()