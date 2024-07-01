# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


from random import randint


class Producto:
    def __init__(self, codigo, titulo, autor):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
    # def set_ (self, value):
    #     self.__ = value
    def set_codigo (self, value):
        self.__codigo = value
    def set_titulo (self, value):
        self.__titulo = value
    def set_autor (self, value):
        self.__autor = value

    # def get_ (self):
    #     return self.__
    def get_codigo (self):
        return self.__codigo
    def get_titulo (self):
        return self.__titulo
    def get_autor (self):
        return self.__autor
    
class ProductoImpreso(Producto):
    def __init__(self, codigo, titulo, autor, editorial, año, precio):
        super().__init__(codigo, titulo, autor)

        self.__editorial = editorial
        self.__año = año
        self.__precio = precio
    # def set_ (self, value):
    #     self.__ = value
    def set_editorial (self, value):
        self.__editorial = value
    def set_año (self, value):
        self.__año = value
    def set_precio (self, value):
        self.__precio = value


    
    # def get_ (self):
    #     return self.__
    def get_editorial (self):
        return self.__editorial
    def get_año (self):
        return self.__año
    def get_precio (self):
        return self.__precio


    # Creacion de metodos
    def estado(self, producto):
        estado_revista = ['Prestado', 'Disponible']
        estado_random = randint(0, len(estado_revista)-1)
        print(f'Su {producto} se encuentra {estado_revista[estado_random]}')


class Revista(ProductoImpreso):
    def __init__(self, codigo, titulo, autor, editorial, año, precio, volumen):
        super().__init__(codigo, titulo, autor, editorial, año, precio)
        self.__volumen = volumen

    # def set_ (self, value):
    #     self.__ = value
    
    def set_volumen (self, value):
        self.__volumen = value
    
    # def get_ (self):
    #     return self.__

    def get_volumen (self):
        return self.__volumen
    
    # Creacion de metodos

    def informacion(self):
        print(f'''
+---------------------------------------------------+
|                Producto Software                  |
+---------------------------------------------------+
|        precio: {self.get_precio()}
|        volumen: {self.get_volumen()}
|        codigo: {self.get_codigo()}
|        titulo: {self.get_titulo()}
|        editorial: {self.get_editorial()}
|        año: {self.get_año()}
+---------------------------------------------------+
''')

class Libro(ProductoImpreso):
    def __init__(self, codigo, titulo, autor, editorial, año, precio, idioma):
        super().__init__(codigo, titulo, autor, editorial, año, precio)

        self.__idioma = idioma
    # def set_ (self, value):
    #     self.__ = value
    def set_idioma (self, value):
        self.__idioma = value
    
    # def get_ (self):
    #     return self.__
    def get_idioma (self):
        return self.__idioma
    
    # Creacion de metodos
    def informacion(self):
        print(f'''
+---------------------------------------------------+
|                Producto Libro                     |
+---------------------------------------------------+
|          titulo: {self.get_titulo()}
|          autor: {self.get_autor()}
|          año: {self.get_año()}
|          precio: {self.get_precio()}
|          editorial: {self.get_editorial()}
|          codigo: {self.get_codigo()}
|          precio: {self.get_precio()}
|          idioma: {self.get_idioma()}
+---------------------------------------------------+
''')


class ProductoGrabado(Producto):
    def __init__(self, codigo, titulo, autor, tiempoDuracion, medioTecnologico):
        super().__init__(codigo, titulo, autor)

        self.__tiempoDuracion = tiempoDuracion
        self.__medioTecnologico = medioTecnologico
    # def set_ (self, value):
    #     self.__ = value
    def set_tiempoDuracion (self, value):
        self.__tiempoDuracion = value
    def set_ (self, value):
        self.__medioTecnologico = value
    
    # def get_ (self):
    #     return self.__
    def get_tiempoDuracion (self):
        return self.__tiempoDuracion
    def get_medioTecnologico (self):
        return self.__medioTecnologico
    
    # Creacion de metodos
    def informacion(self):
        print(f'''
+---------------------------------------------------+
|                Producto Grabado                   |
+---------------------------------------------------+
|          titulo: {self.get_titulo()}
|          autor: {self.get_autor()}
|          tiempo de duracion: {self.get_tiempoDuracion()}
|          medio tecnologico: {self.get_medioTecnologico()}
|          codigo: {self.get_codigo()}
+---------------------------------------------------+
''')
        
class ProductoSoftware(Producto):
    def __init__(self, codigo, titulo, autor, version, sistemaOperativo):
        super().__init__(codigo, titulo, autor)

        self.__version = version
        self.__sistemaOperativo = sistemaOperativo
    # def set_ (self, value):
    #     self.__ = value
    def set_version (self, value):
        self.__version = value
    def set_sistemaOperativo (self, value):
        self.__sistemaOperativo = value

    # def get_ (self):
    #     return self.__
    def get_version (self):
        return self.__version
    def get_sistemaOperativo (self):
        return self.__sistemaOperativo
    
    # Creacion de metodos
    def informacion(self):
        print(f'''
+---------------------------------------------------+
|                Producto Software                  |
+---------------------------------------------------+
|          titulo: {self.get_titulo()}
|          autor: {self.get_autor()}
|          version: {self.get_version()}
|          sistema operativo: {self.get_sistemaOperativo()}
|          codigo: {self.get_codigo()}
+---------------------------------------------------+
''')