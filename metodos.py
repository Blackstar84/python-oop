class Usuario:
    nombre = "Uriel"
    def saludar(self):
        print("Hola, soy ", self.nombre)

    def saludo(self, saludo):
        print(saludo + self.nombre)    


uriel = Usuario()

uriel.saludo('Aloha! Mi nombre es: ')



cody = Usuario()
cody.nombre = 'Cody'

cody.saludar()

print(f'Mr. {cody.nombre} ')