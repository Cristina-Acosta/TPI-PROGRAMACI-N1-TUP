import requests
import csv
import os
from colorama import *

def paises_lista():
    URL="https://restcountries.com/v3.1/all?fields=name,population,area,continents"
    try:
    #GET para obtener información de la API y cargarla en respuesta
        respuesta = requests.get(URL, timeout=8)
        
    #Comprobando que se ejecute con éxito
        if respuesta.status_code == 200:
        #generando un json de respuesta e ingresando a la lista datos
            datos = respuesta.json()
            paises_=[]
            print(Cursor.FORWARD(30)+Fore.GREEN+"Datos cargados con éxito!")
            for i in range(len(datos)):
                pais= datos[i]
                paises={"nombre":pais["name"]["common"],
                "poblacion":int(pais["population"]),
                "area":int(pais["area"]),
                "continente":pais["continents"][0]}
                paises_.append(paises)
            if not os.path.exists("paises.csv"):
                print(Cursor.FORWARD(30)+Back.WHITE+"CREANDO ARCHIVO...")
                paises_csv(paises_)
            return paises_#RETORNA LISTA DE FILTRADA POR EL FOR
        else:
            print("Error al obtener datos:"+respuesta.status_code)
    except:
        print("Error al obtener datos:"+respuesta.status_code)

def paises_csv(lista_paises):
    paises=lista_paises
#INGRESAMOS LA LISTA DE PAÍSES PARA CREAR EL CSV
    with open("C:\\Users\\f\\OneDrive\\Escritorio\\integrador\\prueba2\\funciones\\paises.csv", "w", newline="", encoding="utf-8") as archivo:
        #ESCRIBIMOS ENCABEZADOS
        escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Población", "Area", "Continente"])
        
        escritor.writeheader()  
#INGRESAMOS LOS PAÍSES SEGÚN LOS ENCABEZADOS AL CSV
        for pais in paises:
            escritor.writerow({
                "Nombre": pais["nombre"],
                "Población": pais["poblacion"],
                "Area": pais["area"],
                "Continente": pais["continente"]
            })
    print(Cursor.FORWARD(30)+Back.GREEN+"¡CSV CREADO!")







