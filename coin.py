from dice import Dice


class Coin(Dice):
    def __init__(self):
        super().__init__("Coin", 2)
