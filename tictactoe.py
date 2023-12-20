# Import necessary libraries
import random

# Define the Tic-Tac-Toe board as a list
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board():
    print(f"    {board[0]} | {board[1]} | {board[2]}")
    print('    - + - + -')
    print(f"    {board[3]} | {board[4]} | {board[5]}")
    print('    - + - + -')
    print(f"    {board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (
            (board[i] == board[i + 3] == board[i + 6] == player) or
            (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player)
        ):
            return True
    if (
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    ):
        return True
    return False

# Function to make a player's move
def player_move():
    while True:
        try:
            move = int(input("\nEnter your move (1-9): ")) - 1
            print("\n")
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("\nInvalid move. Try again.")
        except ValueError:
            print("\nInvalid input. Enter a number between 1 and 9.")

# Function to make the AI's move using Minimax algorithm
def ai_move():
    best_score = -float("inf")  # Initialize the best score to negative infinity
    best_move = None  # Initialize the best move to None

    for i in range(9):  # Iterate through the board positions (0-8)
        if board[i] == " ":  # If the position is empty
            board[i] = "O"  # Place the AI's symbol "O" in that position
            score = minimax(board, 0, False)  # Calculate the score for this move using minimax algorithm
            board[i] = " "  # Undo the move to explore other possibilities
            if score > best_score:  # If the calculated score is better than the current best score
                best_score = score  # Update the best score
                best_move = i  # Update the best move (position)

    print(f"\nAI chooses position '{best_move + 1}'\n")  # Print the AI's chosen position
    board[best_move] = "O"  # Place the AI's symbol "O" in the best move

# Minimax algorithm for AI's move
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):  # If AI wins, return a score of 1
        return 1
    elif check_winner(board, "X"):  # If player wins, return a score of -1
        return -1
    elif is_board_full(board):  # If the board is full and no one wins, return a score of 0 (tie)
        return 0

    if is_maximizing:  # If it's AI's turn to maximize the score
        best_score = -float("inf")  # Initialize the best score to negative infinity
        for i in range(9):  # Iterate through the board positions (0-8)
            if board[i] == " ":  # If the position is empty
                board[i] = "O"  # Place the AI's symbol "O" in that position
                score = minimax(board, depth + 1, False)  # Recursively calculate the score for this move (player's turn)
                board[i] = " "  # Undo the move to explore other possibilities
                best_score = max(score, best_score)  # Update the best score with the maximum score

        return best_score  # Return the best score found during maximizing
    else:  # If it's player's turn to minimize the score
        best_score = float("inf")  # Initialize the best score to positive infinity
        for i in range(9):  # Iterate through the board positions (0-8)
            if board[i] == " ":  # If the position is empty
                board[i] = "X"  # Place the player's symbol "X" in that position
                score = minimax(board, depth + 1, True)  # Recursively calculate the score for this move (AI's turn)
                board[i] = " "  # Undo the move to explore other possibilities
                best_score = min(score, best_score)  # Update the best score with the minimum score

        return best_score  # Return the best score found during minimizing


# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe with AI!")
    print("Instructions: This game is played by inputing numbers that corresponds to the spaces as shown below. \n")
    print("     1 | 2 | 3")
    print("     - + - + -")
    print("     4 | 5 | 6")
    print("     - + - + -")
    print("     7 | 8 | 9")
    print("\nAt this point, you will be player 'X' while the AI will be player 'O' \n")
    print("Start ...\n")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("\n*** Congratulations! You win! ***\n")
            break
        if is_board_full(board):
            print("\n*** It's a tie! ***\n")
            break

        print("\n --------------------")
        ai_move()
        print_board()
        print("\n --------------------\n")
        print_board()
        if check_winner(board, "O"):
            print("\n*** AI wins! Better luck next time ***\n")
            break
        if is_board_full(board):
            print("\n*** It's a tie! ***\n")
            break

if __name__ == "__main__":
    main()