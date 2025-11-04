import os
#funcion para limpiar pantalla en Windows y Linux
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")