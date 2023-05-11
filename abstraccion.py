class FilaBanco:
    usuarios = Hash()

    def siguiente_usuario(self, numero):
        #Implementación
        return self.usuarios.obtener(numero)]

    def formar_usuario(self, numero,usuario):
        self.usuarios.agregar(numero, usuario)



class Hash():
    datos = {}

    def obtener(self, llave):
        self.datos[llave]

    def agregar(self, llave, valor):
        self.datos[llave] = valor

class Queue:
    datos = []

    def obtener(self, llave):
        self.datos[0]

    def agregar(self, llave, valor):
        self.datos[len(datos)-1] = valor
