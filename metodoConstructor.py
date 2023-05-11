class Usuario:
    nombre = "Uriel"
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self, saludo):
        print(saludo + self.nombre)    


uriel = Usuario('Carlos')

uriel.saludo('Aloha! Mi nombre es: ')



