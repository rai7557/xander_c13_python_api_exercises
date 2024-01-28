"""
Starter code for refactoring exercise.

A simple CLI-based rock, paper, scissors game to play against the computer.
"""

import random


if __name__ == "__main__":

    collection = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors! Select one the following three options:")

    while True:
        user_input = input(
            "\t 1. Rock\n"
            "\t 2. Paper\n"
            "\t 3. Scissors\n"
            "\t 4. Quit\n\n"
        )

        if int(user_input) == 4:
            print("Goodbye!")
            break
        elif 1 <= int(user_input) <= 3:
            player_selection = collection[int(user_input) - 1]
            print(f"You selected '{player_selection}'")

            random_number = random.randint(0, 2)

            computer_selection = collection[random_number]

            if player_selection == computer_selection:
                print(f"Computer also selected '{computer_selection}'. It's a tie! Try again.")
                continue

            if player_selection == "rock" and computer_selection == "scissors" or \
                player_selection == "paper" and computer_selection == "rock" or \
                    player_selection == "scissors" and computer_selection == "paper":

                print(f"Computer selected '{computer_selection}'. You win!")
                try_again = input("Try again?\n 1. Yes \n 2. No\n")

                if int(try_again) == 1:
                    continue
                else:
                    print("Goodbye!")
                    break

            elif player_selection == "rock" and computer_selection == "paper" or \
                    player_selection == "paper" and computer_selection == "scissors" or \
                    player_selection == "scissors" and computer_selection == "rock":

                print(f"Computer selected '{computer_selection}'. You lose!")
                try_again = input("Try again?\n 1. Yes \n 2. No\n")

                if int(try_again) == 1:
                    continue
                else:
                    print("Goodbye!")
                    break
        else:
            print("Invalid selection. Please select again.")
            continue
