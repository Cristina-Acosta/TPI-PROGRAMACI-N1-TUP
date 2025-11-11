#Script de estadísticas
from operator import itemgetter
#itemgetter nos permite seleccionar de la lista de diccionarios por la key y sorted la ordena 

# Ordenar países por nombre
def ordenar_paises(lista_paises,key, orden):
    try:
        ordenados=sorted(lista_paises, key=itemgetter(key), reverse=orden)
        if key=="nombre":
            for pais in ordenados:
                print(f"{key.capitalize()} de {pais["nombre"]} : {pais[key]}")
        else:
            for pais in ordenados:
                print(f"{key.capitalize()} de {pais["nombre"]} : {pais[key]:,.2f}")
        return ordenados
    except KeyError:
        print("Error: clave 'nombre' no encontrada en los datos.")
        return []
# País con mayor y menor población
def mayor_menor_poblacion(paises):
    lista=ordenar_paises(paises,"poblacion","ascendente")
    menor=lista[-1]
    mayor=lista[0]

    print(f"\n {menor["nombre"]} es el país con menor población en el mundo: {menor["poblacion"]:,.2f} habitantes")
    print(f"\n {mayor["nombre"]} es el país con mayor población en el mundo: {mayor["poblacion"]:,.2f} habitantes\n")

# Promedio de población o superficie
def funcion_promedio(paises,valor):
    suma:float=0
    if valor=="continente":
        promedio:float=len(paises)/7
        print(f"Promedio de paises por continente: {promedio:,.2f}")
    else:
        for pais in paises:
            suma+=pais[valor]
            promedio:float=suma/(len(paises))
            print(f"Promedio {valor} mundial: {promedio:,.2f}")

# Cantidad de países por continente
def cantidad_paises(paises):
    #Diccionario acumulador de paises
    cantidad = {"Asia": 0,"Europe": 0,"Africa": 0,"North America":0,"South America":0,"Antarctica":0,"Oceania": 0}
    for pais in paises:
        continente = pais["continente"]  
        # Sumamos uno al continente que corresponda
        if continente in cantidad:
            cantidad[continente] += 1
    print (*cantidad.items(), sep='\n')

if __name__=="__main__":
    from app import paises_lista
    paises=paises_lista()
    funcion_promedio(paises,"area")
    cantidad_paises(paises)
