import random
from abc import ABC

from idice import IDice


class Dice(IDice, ABC):
    __nbSides: int
    __name: str

    def __init__(self, name: str, nbSides: int):
        self.__name = name
        if nbSides < 2:
            raise "Invalid sides number, nbSides must be strictly higher than 1."
        self.__nbSides = nbSides

    def roll(self) -> int:
        return random.randint(1, self.__nbSides)

    def prettyRoll(self) -> str:
        return self.getName() + "(" + str(self.roll()) + ")"

    def getName(self) -> str:
        return self.__name
