# rock-paper-scissors.py
from game import Game

def get_user_menu_choice():
    # """Display menu and return user choice (no looping here)."""
    print("\n--- Rock Paper Scissors ---")
    print("(1) Play a new game")
    print("(2) Show scores")
    print("(x) Exit")
    choice = input("Enter your choice: ").lower()

    valid_choices = ['1', '2', 'x']
    if choice in valid_choices:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return None


def print_results(results):
# """Display all results and thank the user."""
    print("\n--- Game Summary ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThanks for playing! 👋")


def main():
    # """Main loop controlling the menu and results."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1  # Count result

        elif choice == "2":
            print_results(results)

        elif choice == "x":
            print_results(results)
            break


if __name__ == "__main__":
    main()