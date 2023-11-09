from dice import Dice


class D4(Dice):
    def __init__(self):
        super().__init__("D4", 4)
