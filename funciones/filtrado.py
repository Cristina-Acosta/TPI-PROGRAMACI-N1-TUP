#Script filtrar y ordenar países


#Por continente- Parámetros(paises:lista de paises,continente:ingresa el usuario)

def filtrar_continente(paises, continente):
    filtrados=[]
    for pais in paises:
        if continente == pais["continente"]:
            filtrados.append(pais)#acumulador de paises que coincide con el nombre
    if filtrados:
        for pais in filtrados:
            print(f"{pais['nombre']} ({pais['continente']})")
    else:
        print("No hay países en ese continente.")

#Por población o area- Parámetros(paises:listade paises,valor, min y máx:rango  de población ingresado por el usuario)

def filtrar_valor(paises,valor, min_p, max_p):
    
    filtrados=[]
    
    for pais in paises: 
        if min_p <= pais[valor] and pais[valor] <= max_p:
            
            filtrados.append(pais)#acumulador de paises que coincide con el rango
    if filtrados:
        for pais in filtrados:
            print(f"{pais["nombre"]} - {valor.capitalize()}: {pais[valor]}")
    else:
        print("No hay países en ese rango.")

