"""
Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).
"""


class Car:
    def __int__(self, color, brand, model, v, tupe_of_car):
        self.color = color
        self.brand = brand
        self.model = model
        self.__v = v
        self.__tupe_of_car = tupe_of_car

    def get(self):
        return self.color_of_the_car

    def set (self, new_color):
        self.color_of_the_car = new_color


car1 = Car("blue", "Mercedese", "S-Class", "V8",  "Universal")

print(car1.get())
car1.set("green")
print(car1.get())
