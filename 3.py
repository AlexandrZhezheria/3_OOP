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
            self.__f = self.__f_to_c(int(value))
        elif system == 'c':
            self.__c = self.__c_to_f(int(value))


    def __repr__(self):
        return "Temperature <{}>".format(self.__c)


    def __с_to_f(c):
        """Перевод из цельсия в фаренгейт"""
        return (9/5) * c + 32


    def __f_to_c(f):
        """Перевод из фаренгейт в цельсий"""
        return 5.0*(f - 32) / 9



if __name__ == "__main__":
    t = Temperature(0, 'f')
    t.get_value()
    print(repr(t))




