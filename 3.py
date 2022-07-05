"""
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать
температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""


class Temperature:
    def __init__(self, value, system):
        self.__value = value
        self.__system = system
        if system == 'f':
            f = self.f_to_c(value)
        elif system == 'c':
            c = self.c_to_f(value)

    def с_to_f(self):
        """Перевод из цельсия в фаренгейт"""
        return (9/5) * self.c + 32

    def f_to_c(self):
        """Перевод из фаренгейт в цельсий"""
        return 5.0*(self.f - 32) / 9

t = Temperature(5, 'f')











# class Temperature():
#     def __init__(self, value, system):
#         self.__value = value
#         self.__system = system
#
#
#     def getvalue(self): # получение значения атрибута
#         return self.__value
#
#     def setvalue(self, value): # установка значения атрибута
#         self.__value = value
#
#
#     value = property(getvalue, setvalue,)




