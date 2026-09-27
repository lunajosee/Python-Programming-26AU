"""
Program Name: coin.py
Author: Jose Luna
Purpose: This program simulates a coin matching game where the user can flip coins and try to match them.
Resources: None
Date: 9/27/2026
"""
import random

class Coin:
    """Represents a single coin that can be tossed to show either "Heads" or "Tails"."""

    def __init__(self):
        """Initialize the coin with a starting value of "Heads"."""
        self.__sideup = "Heads"

    def toss(self):
        """Toss the coin and update its side."""

        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin that is facing up."""
        return self.__sideup

test_coin = Coin()
for i in range(5):
    test_coin.toss()
    print(test_coin.get_sideup())