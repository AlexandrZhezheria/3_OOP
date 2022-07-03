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
