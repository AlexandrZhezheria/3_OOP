"""
Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting().
Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия этих двух
объектов в одной функции (функция hello_friend).
"""


class English:
    def greeting(self):
        print("Hello")


class French:
    def greeting(self):
        print("Bonjour")

def intro(language):
  language.greeting()

john = English()
gerard = French()
intro(john) # Hello
intro(gerard) # Bonjour

