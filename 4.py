"""
Опишите два класса Base и его наследника Child с методами method(), который выводит
на консоль фразы соответственно "Hello from Base" и "Hello from Child".
"""


class Base():
    def __init__(self):
        print('Hello from Base')

    def method(self):
        print('Hello from Child')


class Child(Base):
    def __init__(self):
        Base.__init__(self)

    def method(self):
        super(Child, self).method()


child = Child()
child.method()
