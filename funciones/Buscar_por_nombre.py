#"1. Buscar país por nombre"
def buscar_pais(paises,inpu):
    encontrados = []
    for pais in paises:
        nombre = pais["nombre"].lower() 
        if inpu.lower() in nombre:
            encontrados.append(nombre)
    if encontrados:
        print("Países encontrados:")
        for pais in encontrados:
            print(f"- {pais.capitalize()}")
    else:
        print(f" No se encontró ningún país con el nombre '{inpu}'.")


if __name__=="__main__":
    from app import paises_lista

    paises=paises_lista()
    buscar_pais(paises,"cHi")