# Mini Projet : game.py
import random

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        # """Ask the user for rock/paper/scissors and validate input."""
        while True:
            user_input = input("Select (rock/paper/scissors): ").lower()
            if user_input in self.items:
                return user_input
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        # """Randomly select rock/paper/scissors for the computer."""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        # """Determine if the user won, lost, or drew."""
        if user_item == computer_item:
            return "draw"

        # Winning combinations
        if (user_item == "rock" and computer_item == "scissors") or \
           (user_item == "paper" and computer_item == "rock") or \
           (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        # """Play one round of Rock-Paper-Scissors."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou selected {user_item}. The computer selected {computer_item}.")

        if result == "win":
            print("You win! 🎉")
        elif result == "loss":
            print("You lose! 😢")
        else:
            print("It's a draw! 🤝")

        return result