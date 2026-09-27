"""
Program Name: player.py
Author: Jose Luna
Purpose: This program simulates a coin matching game where the user can flip coins and try to match them.
Resources: None
Date: 9/27/2026
"""
from coin import Coin

class Player:
    """Represents a player in the coin matching game."""

    def __init__(self, name):
        """Initialize the player with a name, wallet, and a coin to toss."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtract one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the current amount of coins in the player's wallet."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name