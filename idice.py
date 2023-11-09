from abc import ABC, abstractmethod


class IDice(ABC):
    @abstractmethod
    def roll(self) -> int:
        ...

    @abstractmethod
    def prettyRoll(self) -> str:
        ...

    @abstractmethod
    def getName(self) -> str:
        ...
