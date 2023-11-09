from dice import Dice


class D6(Dice):
    def __init__(self):
        super().__init__("D6", 6)
