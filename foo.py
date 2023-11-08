from abc import ABC, abstractmethod

from bar import Bar
from baz import Baz
from grault import Grault


class Foo(Grault, ABC):
    __something: int
    __anotherThing: int
    __bar: Bar
    __bazs: [Baz]

    def __init__(self, something: int):
        self.__something = something
        self.__anotherThing = 0
        self.__bar = Bar()
        self.__bazs = []

    def getSomething(self) -> int:
        return self.__something

    def setSomething(self, something: int):
        self.__something = something

    @property
    def AnotherThing(self) -> int:
        return self.__anotherThing

    @AnotherThing.setter
    def AnotherThing(self, anotherThing: int) -> None:
        if (type(anotherThing) != int):
            raise ("invalid type for anotherThing")
        if (anotherThing < 1):
            raise ("anotherThing must be strictly higher than 0")
        self.__anotherThing = anotherThing

    @abstractmethod
    def doSomething(self):
        ...

    def doSomethingElse(self):
        print("Je fais un autre truc")

    def addBaz(self, baz: Baz):
        self.__bazs.append(baz)
        baz.setFoo(self)
