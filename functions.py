# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2



from classes.clases import *
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def continuar(funcion, main):
    respuesta = input("¿Desea continuar? S/N: ").upper()
    if respuesta == 'N':
        print('Hasta luego')
        exit()
    else:
        clear()
        funcion()

# +++++++++++++++++++++++++++++++++++++producto grabado+++++++++++++++++++++++++++++++++++++

def revistas(main):
    while True:
        try:
            clear()
            print('''
                Tenemos las revistas:
                    1. Vea
                    2. Semana
                    3. Cambio
                    4. Times
                    ''')
            option = int(input("Ingrese el número correspondiente a la revista que desea ver: "))
            if option == 1:
                clear()
                Revista(123, 'Vea', '', 'Vea', 2024, 20000, '5').informacion()
                continuar(main, main)
            elif option == 2:
                clear()
                Revista(456, 'Semana', '', 'Semana', 2020, 20000, '7').informacion()
                continuar(main, main)                
            elif option == 3:
                clear()
                Revista(789, 'Cambio', '', 'Cambio', 2023, 20000, '12').informacion()
                continuar(main, main)    
            elif option == 4:
                clear()
                Revista(159, 'Times', '', 'Times', 2022, 20000, '9').informacion()
                continuar(main, main)    
            else:
                print("Opción inválida")
                continue
            continuar(producto_impreso)
        except ValueError as e:
            print("Error:", e)
            continue


def producto_impreso(main):
    while True:
        try:
            print('''
            Dentro de nuestros productos impresos puede encontrar:
            1. Revista
            2. Libro
            ''')
            input_producto = int(input('Ingrese el número del producto que desea ver: '))
            if input_producto == 1:
                    while True:
                        try:
                            # Creacion de las varibales que asignaran los valores para cada producto grabado que se cree
                            codigo = int(input('Ingrese el codigo: '))
                            titulo_de_revista = str(input('Ingrese el titulo del producto: '))
                            autor = str(input('Ingrese el(los) autor(es)'))
                            editorial = str(input('Ingrese la editporial: '))
                            año = int(input('Ingrese el año de la revista: '))
                            precio = int(input('Ingrese el precio de la revista: '))
                            volumen = str(input('Ingrese el volumen: '))

                            #Se limpia la pantalla
                            clear()

                            #Se rompre el bucle para continuar 
                            break

                        #Control de los errores definiendolos en una varibale como e
                        except ValueError as e:

                            #Mensaje de aviso en caso de errores
                            print(f'Error: {e}')

                    # Nuevo bucle en el momento de 
                    while True:
                        try:
                            print(Revista(codigo, titulo_de_revista, autor, editorial, año, precio, volumen).informacion())
                            continuar(main, main)
                            break
                        except ValueError as e:
                            print("Error:", e)
                            continue
                    continuar(main, main)
            elif input_producto == 2:
                    while True:
                        try:
                            # Creacion de las varibales que asignaran los valores para cada producto grabado que se cree
                            codigo = int(input('Ingrese el codigo: '))
                            titulo_de_libro = str(input('Ingrese el titulo del producto: '))
                            autor = str(input('Ingrese el(los) autor(es)'))
                            editorial = str(input('Ingrese la editorial: '))
                            año = int(input('Ingrese el año del libro: '))
                            precio = int(input('Ingrese el precio del libro: '))
                            idioma = str(input('Ingrese el idioma: '))

                            #Se limpia la pantalla
                            clear()

                            #Se rompre el bucle para continuar 
                            break

                        #Control de los errores definiendolos en una varibale como e
                        except ValueError as e:

                            #Mensaje de aviso en caso de errores
                            print(f'Error: {e}')

                    # Nuevo bucle en el momento de 
                    while True:
                        try:
                            print(Libro(codigo, titulo_de_libro, autor, editorial, año, precio, idioma).informacion())
                            continuar(main, main)
                        except ValueError as e:
                            print("Error:", e)
                            continue
            else:
                print("Opción no válida")
                continue
        except ValueError as e:
            print("Error:", e)
            continue

# +++++++++++++++++++++++++++++++++++++producto grabado+++++++++++++++++++++++++++++++++++++

def producto_grabado(main):

    while True:
        try:
            # Creacion de las varibales que asignaran los valores para cada producto grabado que se cree
            codigo = int(input('Ingrese el codigo: '))
            titulo_del_album = str(input('Ingrese el titulo del producto: '))
            autor = str(input('Ingrese el(los) autor(es)'))
            duracion = str(input('Ingrese la duracion: '))
            medio_tecnologico = str(input('Ingrese el medio tecnologico: '))

            #Se limpia la pantalla
            clear()

            #Se rompre el bucle para continuar 
            break

        #Control de los errores definiendolos en una varibale como e
        except ValueError as e:

            #Mensaje de aviso en caso de errores
            print(f'Error: {e}')

    # Nuevo bucle en el momento de 
    while True:
        try:
            print(ProductoGrabado(codigo, titulo_del_album, autor, duracion, medio_tecnologico).informacion())
            continuar(main, main)
        except ValueError as e:
            print("Error:", e)
            continue
# +++++++++++++++++++++++++++++++++++++producto grabado+++++++++++++++++++++++++++++++++++++
# Creamos la funcion encarga del control de los inputs del usuario
def producto_software(main):
                    while True:
                        try:
                            # Creacion de las varibales que asignaran los valores para cada producto grabado que se cree
                            codigo = int(input('Ingrese el codigo: '))
                            titulo_de_libro = str(input('Ingrese el titulo del producto: '))
                            autor = str(input('Ingrese el(los) autor(es)'))
                            version = str(input('Ingrese la version: '))
                            sistemaOperativo = str(input('Ingrese el sistema operativo: '))


                            #Se limpia la pantalla
                            clear()

                            #Se rompre el bucle para continuar 
                            break

                        #Control de los errores definiendolos en una varibale como e
                        except ValueError as e:

                            #Mensaje de aviso en caso de errores
                            print(f'Error: {e}')

                    # Nuevo bucle en el momento de 
                    while True:
                        try:
                            print(ProductoSoftware(codigo, titulo_de_libro, autor, version, sistemaOperativo).informacion())
                            continuar(main, main)
                        except ValueError as e:
                            print("Error:", e)
                            continue
    
