'''
---------------------------------------------------------------
                CLASSES ABSTRATAS EM PYTHON
---------------------------------------------------------------

Trata-se de classes que define(cria) atributos e métodos, porém não os
implementa.

As classes abstratas são usadas para definir atributos  e ações que são implementadas/utilizadas em outras classes q são chmadas classes filha.

São usadas em projetos onde vários componentes implementam o mesmo comportamento.

Em Python uma classe é abstrata de ela tiver pelo menos  método abstrato.

'''

from abc import ABC, abstractmethod
from shutil import move

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Person(Animal):

    def move(self):
        print('\n I AM A MAN AND I CAN WALK \n')


class Dog(Animal):

    def move(self):
        print('\n I AM A DOG AND I CAN LATIR')


class Cat(Animal):

    def move(self):
        print('\n EU SOU GATO E EU POSSO MIAR')


class Lion(Animal):

    def move(self):
        print('\n EU SOU UM LEÃO E POSSO RUGIR')