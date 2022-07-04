"""
Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:

    def __int__(self, company, model, color, year, price):
        self.__company = company
        self.__model = model
        self.color = color
        self.year = year
        self.price = price

Volvo = Car('Volvo', 'x60', 'yellow',  1845, 2000)
Honda = Car('Honda', 'CRV', 'red',  1950, 1050)
Toyota = Car("Toyota", "Camry", "green", 2000, 30000,)

@property:


@setter:



