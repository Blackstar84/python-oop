''' class Usuario:
    edad = 0
    def __init__(self, nombre):
        self._nombre = nombre

    def saludo(self, saludo):
        print(saludo + self.nombre)    


class Empleado(Usuario):
    __salario = 0 #private

    def modificar_salario(self, salario): #setter
        self.__salario = salario

    def ver_salario(self): #getter
        print(self.__salario)    

    def saludar(self):
        super().saludo('Hola!')
        print("Mi nombre es:", self.nombre, 'Y gano', str(self.__salario))    ''' 


# La forma ideal es hacerlo como se muestra a continuación
class Usuario:
    __edad = 0
    def __init__(self, nombre):
        self._nombre = nombre

    def saludo(self, saludo):
        print(saludo + self.nombre)   

    @property     
    def edad(self): #getter
        return self.__edad
    
    @edad.setter
    def edad(self, valor): #setter
        if (valor < 0):
            raise ValueError('Edad no puede ser menor que 0')     
        self.__edad = valor

class Empleado(Usuario):
    __salario = 0 #private

    def modificar_salario(self, salario): #setter
        self.__salario = salario

    def ver_salario(self): #getter
        print(self.__salario)    

    def saludar(self):
        super().saludo('Hola!')
        print("Mi nombre es:", self.nombre, 'Y gano', str(self.__salario))   


empleado = Empleado('Carlos')
empleado.edad = 38

print(empleado.edad)