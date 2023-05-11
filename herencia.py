class Usuario:
    nombre = "Uriel"
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self, saludo):
        print(saludo + self.nombre)    


class Empleado(Usuario):
    salario = 0

    def modificar_salario(self, salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)    

    def saludar(self):
        print("Mi nombre es:", self.nombre, 'Y gano', str(self.salario))    
        

empleado = Empleado('Carlos');

empleado.saludo('Hola! me llamo: ')

empleado.modificar_salario(1000)

empleado.ver_salario()

empleado.saludar()

usuario = Usuario('Uriel')
''' usuario.ver_salario() '''
