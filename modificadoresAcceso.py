class Usuario:
    nombre = "Uriel"
    def __init__(self, nombre):
        self._nombre = nombre

    def saludo(self, saludo):
        print(saludo + self.nombre)    


class Empleado(Usuario):
    __salario = 0

    def modificar_salario(self, salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)    

    def saludar(self):
        super().saludo('Hola!')
        print("Mi nombre es:", self.nombre, 'Y gano', str(self.__salario))    


class Administrativo(Empleado):
    def mi_salario(self):
        print(self.__salario)        
        

empleado = Empleado('Carlos')

empleado.modificar_salario(1000)

empleado.ver_salario()

# Si queremos acceder igual a una propiedad privada se tiene que hacer esto que no es recomendable
# para esto se utilizan los métodos que se encargan de acceder a los atributos
print(empleado._Empleado__salario)

# Esto no puede realizarse ya que está como privado
# print(empleado.__salario)



admin = Administrativo("Carlos")
# Esto no podemos hacerlo ya que desde la clase hija no tenemos acceso al atributo declarado como privado _salario
admin.mi_salario()