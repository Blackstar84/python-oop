from abc import ABC, abstractclassmethod


class EstructuraAbstracta(ABC):

    @abstractclassmethod
    def obtener():
        pass

    @abstractclassmethod
    def agregar():    
        pass





class Hash(EstructuraAbstracta):
    datos = {}

    def obtener(self, llave):
        datos[llave]

    def agregar(self, llave, valor):
        datos[llave] = valor


h = Hash()

class Queue(EstructuraAbstracta):
    datos = []

    def obtener(self, llave):
        datos[0]

    def agregar(self, llave, valor):
        datos[len(datos)-1] = valor



class FilaBanco:
    usuarios = Hash()

    def __init__(self, almacen_usuarios):
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError('Store is not supported')
        self.usuarios = almacen_usuarios


    def siguiente_usuario(self, numero):
        #Implementación
        return self.usuarios.obtener(numero)

    def formar_usuario(self, numero,usuario):
        self.usuarios.agregar(numero, usuario)


FilaBanco(Queue())