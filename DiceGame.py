from abc import ABCMeta, abstractclassmethod, abstractmethod
import random

class Person(metaclass = ABCMeta):
    def __init__(self):
        self.balance = 1000
        self.hp = 10
        self.shield = 0
        self.dice_deck = 15

    # @abstractmethod
    # def set_default(self):
    #     pass

class Player(Person):
    def __init__(self):
        super().__init__()

    def output(self):
        print(self.balance)
        print(self.hp)
        print(self.shield)
        print(self.dice_deck)
   
   
class Dealar(Person):
    def __init__(self):
        super().__init__()

    def output(self):
        print(self.balance)
        print(self.hp)
        print(self.shield)
        print(self.dice_deck)

