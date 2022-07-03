"""
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать
температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""

# def convert(x):
#
#     tf = (9/5)*x+32
#
#     return tf
#
# while True:
#     tc=input('t v celciax: ')
#     if tc == '':
#
#         break
#
#     else:
#      tc = int(tc)
#
#     tf = convert(tc)
#
#     print('t в цельсиях',tc,'т в фаренгейтах',tf)

class Temperature:
    def __init__(self, value, system):
        if system == 'f':
            self.__k = __f_to_k(int(value))
        elif system == 'c':
            self.__k = __c_to_k(int(value))


    def __repr__(self):
        return "Temperature <{}>".format(self.__k)


    def __k_to_f(v):
        """Перевод из кельвина в фаренгейт"""
        return 1.8 * (v - 273) + 32


    def __f_to_k(v):
        """Перевод из фаренгейт в кельвина"""
        return ((v - 32) / 1.8) + 273


    def __k_to_c(v):
        """Перевод из кельвина в цельсий"""
        return v - 273


    def __c_to_k(v):
        """Перевод из цельсия в кельвина"""
        return v + 273


if __name__ == "__main__":
    t = Temperature(0, 'f')
    print(repr(t))
