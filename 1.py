"""
Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:
    def __int__(self, company, model, color, year, price):
        self.company = company
        self.model = model
        self.__color = color
        self.year = year
        self.__price = price

volvo = Car('Volvo', 'x60', 'yellow',  1845, 2000)
honda = Car('Honda', 'CRV', 'red',  1950, 1050)
car3 = Car("Toyota", "Camry", "green", 2000, 30000,)


class Javatpoint:
    def __init__(self):
        self.emp = "None"
    def getEmp(self):
        return self.emp
    def setEmp(self, emp):
        self.emp = emp
Mark = Javatpoint()
John = Javatpoint()
Mark.setEmp("Developer")
John.setEmp("Designer")
print(John.emp)
print(Mark.emp)
