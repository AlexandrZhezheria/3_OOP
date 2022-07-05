"""
Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting().
Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия этих двух
объектов в одной функции (функция hello_friend).
"""


class English:
    def greeting(self):
        print("Hello")


class Español:
    def greeting(self):
        print("Hola")

def hello_friend(language):
  language.greeting()

john = English()
gerard = Español()
hello_friend(john)
hello_friend(gerard)
