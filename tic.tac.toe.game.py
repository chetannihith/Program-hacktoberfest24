def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    for _ in range(9):
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                
                if board[row][col] != ' ':
                    print("This cell is already occupied. Try again.")
                    continue
                
                board[row][col] = current_player
                break
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
