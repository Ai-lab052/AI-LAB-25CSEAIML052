def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_queens(board, row):
    # All queens are placed
    if row == 8:
        print_board(board)
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve_queens(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Initialize board
board = [-1] * 8

if not solve_queens(board, 0):
    print("No solution exists")