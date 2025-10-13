# Tic Tac Toe Game (Two Players)

# Display the game board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# Get player input and validate it
def player_input(board, player):
    while True:
        try:
            position = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), choose your position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("❌ Invalid position! Choose a number between 1 and 9.")
            elif board[position] != " ":
                print("⚠️  That spot is already taken! Choose another one.")
            else:
                return position
        except ValueError:
            print("❌ Please enter a valid number between 1 and 9.")


# Check if a player has won
def check_win(board, mark):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == mark for i in condition):
            return True
    return False


# Check if the board is full (tie)
def is_board_full(board):
    return all(space != " " for space in board)


# Main game loop
def play():
    print("🎮 Welcome to Tic Tac Toe!")
    print("Player 1 = X, Player 2 = O")
    print("Positions are numbered from 1 to 9 as shown below:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")

    board = [" "] * 9
    current_player = 1

    while True:
        display_board(board)
        position = player_input(board, current_player)
        mark = "X" if current_player == 1 else "O"
        board[position] = mark

        if check_win(board, mark):
            display_board(board)
            print(f"🏆 Player {current_player} ({mark}) wins! Congratulations!")
            break
        elif is_board_full(board):
            display_board(board)
            print("🤝 It's a tie! The board is full.")
            break

        # Switch players
        current_player = 2 if current_player == 1 else 1


# Run the game
if __name__ == "__main__":
    play()
