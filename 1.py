"""
Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:
    def __init__(self, color, brand, model, v, type_of_car):
        self.color = color
        self.brand = brand
        self.model = model
        self.__v = v
        self.__type_of_car = type_of_car

    def get(self):
        return self.__v

    def set(self, new_v):
        self.__v = new_v


car1 = Car("blue", "Mercedese", "S-Class", "V8", "Universal")

print(car1.get())
car1.set("V9")
print(car1.get())
