"""
Program Name: Lab9_username-1.py
Author: Jose Luna
Purpose: This program simulates a coin matching game where the user can flip coins and try to match them.
Resources: None
Date: 9/27/2026
"""
from player import Player

def main():
    """Run the main menu loop for the coin matching game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Matching Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")

    player1.toss_coin()
    player2.toss_coin()

    side1 = player1.get_coin_side()
    side2 = player2.get_coin_side()

    print(player1.get_name(), "tossed:", side1)
    print(player2.get_name(), "tossed:", side2)

    if side1 == side2:
        player1.win_coin()
        player2.lose_coin()
        print("...It's a Match! Player 1 wins a coin.")
    else:
        player2.win_coin()
        player1.lose_coin()
        print("...No match! Player 2 wins a coin.")

    print(player1.get_name(), "now has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "now has", player2.get_wallet(), "coins.")


main()