from dice import IDice


class DiceBag(IDice):
    __dices: [IDice]

    def __init__(self):
        self.__dices = []

    def add(self, dice: IDice):
        self.__dices.append(dice)

    def roll(self) -> int:
        result = 0
        for dice in self.__dices:
            result += dice.roll()
        return result

    def prettyRoll(self) -> str:
        result = ""
        for i in range(len(self.__dices)):
            result += self.__dices[i].prettyRoll()
            if i != len(self.__dices) - 1:
                result += " + "
        return result

    def getName(self) -> str:
        return ""
