class Example():
    class_attribute = 'class_value'


    def __init__(self):
        self.instance_attribute = 'instance_value'
        self.__this_is_not_visible = 'buy alsop not pythonic'

    def __init__(self, with_parameter):
        self.instance_attribute = with_parameter

    def instanceMethod(self, parameter):
        print(parameter)

    @classmethod
    def classMethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticMethod():
        return 'static method called'

class Animal():
    def makeNoise(self):
        pass

    def sayName(self):
        pass

    def learnName(self, name):
        pass

class Dog(Animal):
    def makeNoise(self):
        print('guau')

# Abstract classes

from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def foo(self):
        pass

class Concrete(Abstract):
    def notFoo(self):
        print('foo implemented method')

Concrete().foo()

class multiple_inheritance(Abstract, Animal):
    def foo(self):
        print('Im everything')


