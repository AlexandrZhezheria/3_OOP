"""
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать и получать
температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале, а получены в другой.
"""
class Term:
    def __int__(self, cels, faring):
        self.cels = cels
        self.faring = faring


        def convert(c):

            tf = (9/5)*c+32

            return tf

        while True:

            tc = input('t v celciax: ')
            if tc == '':

                break

            else:

            tc = int(tc)

            tf = convert(tc)

         print('t в цельсиях', tc, 'т в фаренгейтах', tf)




