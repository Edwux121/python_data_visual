from random import randint

class Dice:
    """Classs representing single dice"""

    def __init__(self, num_sides=6):
        """Assume a six-sided dice"""

        self.num_sides = num_sides

    def roll(self):
        """Return a random number betweeb 1 and number of sides"""
        return randint(1, self.num_sides)