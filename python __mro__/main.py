class A: ...

class A1(A): ...
class A2(A): ...

class B11(A1): ...
class B12(A1): ...

class B21(A2): ...

class D1(B11,B12): ...
class D2(B11,B21): ...

print("A->A1->B11, B12 | A->A2->B21")
print("B11, B12 -> D1 | B11, B21 -> D2 \n")
print(D1.__mro__)
print("")
print(D2.__mro__)

print("\n^^MRO goes upwards, but, subclass always before parent \n")

"""ABC v/s ABCMeta in __mro__"""

from abc import ABC, abstractmethod
from abc import ABCMeta

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Shape(metaclass=ABCMeta):
    def __init__(self, _id):
        self._id = _id

    @abstractmethod
    def display(self): 
        pass

print(Shape.__class__.__mro__)
print(Animal.__class__.__mro__)
