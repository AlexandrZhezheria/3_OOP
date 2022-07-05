"""
Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:
    def __int__(self, company, model, color, price):
        self.__company = company
        self.__model = model
        self.color = color
        self.price = price

        print(self.__model)
        print(self.price)
        print(self.color)


car1 = Car("Honda", "Civic", "red", 2000)

print(car1.color)
print(car1.__company)
