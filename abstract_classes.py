'''
---------------------------------------------------------------
                CLASSES ABSTRATAS EM PYTHON
---------------------------------------------------------------

Trata-se de classes que define(cria) atributos e métodos, porém não os
implementa.

As classes abstratas são usadas para definir atributos  e ações que são implementadas/utilizadas em outras classes que são achmadas classes filha.

São usadas em projetos  de grande porte onde vários componentes implementam o mesma ação, ou seja, possuem o mesmo interface.

Python não possui define classes abstratas de maneira impirica, e sim possui um módulo base de classes abstratas chamado abc no qual é criado uma class base abstrata que é ABC.

Em Python uma classe é abstrata se ela tiver pelo menos  método abstrato.

um método abstrato quando é decorado com um método chamado
@abstractmethod

'''

from abc import ABC, abstractmethod

class Animal(ABC):

    name_type = ''

    @abstractmethod
    def move(self):
        pass


class Person(Animal):
    name_type = ''
    def move(self):
        print(f'\n {self.name_type} AND I CAN WALK \n')

class Dog(Animal):
    def move(self):
        print('\n I AM A DOG AND I CAN LATIR')

class Cat(Animal):
    def move(self):
        print('\n EU SOU GATO E EU POSSO MIAR')

class Lion(Animal):
    def move(self):
        print('\n EU SOU UM LEÃO E POSSO RUGIR')

class Eagle(Animal):
    def move(self):
        print('\n I AM A EAGLE AND I CAN MAKE A SOUND \n')
