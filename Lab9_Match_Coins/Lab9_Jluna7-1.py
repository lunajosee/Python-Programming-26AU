"""
Program Name: Lab9_Jluna7-1.py
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

    play_again = input("\nDo you want to play a round? (yes/no): ")

    while (play_again == "y" or play_again == "Y" and player1.get_wallet() > 0 and player2.get_wallet() > 0):
        print("\nTossing...")
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

        print()
        print(player1.get_name(), "now has", player1.get_wallet(), "coins.")
        print(player2.get_name(), "now has", player2.get_wallet(), "coins.")

        if player1.get_wallet() > 0 and player2.get_wallet() > 0:
            play_again = input("\nDo you want to toss coins? (y/n): ")

    print("\n--- Final Score ---")
    print(player1.get_name() + ":", player1.get_wallet())
    print(player2.get_name() + ":", player2.get_wallet())

    if player1.get_wallet() == 0:
        print("Game Over!", player1.get_name(), "ran out of coins and loses!")
    elif player2.get_wallet() == 0:
        print("Game Over!", player2.get_name(), "ran out of coins and loses!")
    elif player1.get_wallet() > player2.get_wallet():
        print(player1.get_name(), "wins with", player1.get_wallet(), "coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(player2.get_name(), "wins with", player2.get_wallet(), "coins!")
    else:
        print("It's a draw!")

    
main()