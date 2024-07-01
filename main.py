# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2

# Importamos 
from functions import *


# Funcion principal
def main():    
    # Inicializamos
    while True:

        # Control de errores
        try:
            # Limpiamos la pantalla
            clear()

            #Imporimimos nuestro catalogo
            print('''
        Dentro de nuestros productos puede encontrar:
            1. Producto Impreso
            2. Producto Grabado
            3. Producto Software
            ''')
            # Pedimos el producto
            input_productos = int(input('Ingrese el numero del catalogo que le interesa: '))
            
            # Limpiamos la consola al elegir que producto queremos registrar
            clear()

            # Estructura de control para el control de los casos 
            match input_productos:

                # Uso de los casos 
                case 1:
                    producto_impreso(main)
                case 2:
                    producto_grabado(main)
                case 3:
                    producto_software(main)

                # Cualquier caso que no nos convenga
                case _:
                    # Impimimos 
                    print("Opción no válida")
                    # Limpiamos la consola
                    clear()
                    # Regresamos al menu principal
                    continue

        except ValueError as e:
            print("Error: ", e)
            clear()

if __name__ == '__main__':
    main()