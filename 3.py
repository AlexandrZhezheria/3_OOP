"""
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать
температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""
# class Term:
#     def __int__(self, cels, faring):
#         self.cels = cels
#         self.faring = faring
#
#
#         def convert(c):
#
#             tf = (9/5)*c+32
#
#             return tf
#
#         while True:
#
#             tc = input('t v celciax: ')
#             if tc == '':
#
#                 break
#
#             else:
#
#                 tc = int(tc)
#
#             tf = convert(tc)
#
#          print('t в цельсиях', tc, 'т в фаренгейтах', tf)

class Temperature:
    def __init__(self, value, system):
        if system == 'f':
            __f = self.f_to_c(value)
        elif system == 'c':
            __c = self.c_to_f(value)

    def с_to_f(self):
        """Перевод из цельсия в фаренгейт"""
        return (9/5) * self.__c + 32

    def f_to_c(self):
        """Перевод из фаренгейт в цельсий"""
        return 5.0*(self.__f - 32) / 9



if __name__ == "__main__":

    t = Temperature(5, 'f')





