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
        super().saludo('Hola!')
        print("Mi nombre es:", self.nombre, 'Y gano', str(self.salario))    
        

empleado = Empleado('Carlos');

empleado.saludar()


class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)

class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        super().imprimir_pie_pagina()   
        print('Derechos reservados')


html = PaginaLegal()
html.pie_pagina = '<p>Hola</p>'

html.imprimir_pie_pagina()
