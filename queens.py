# Made for GCI
import numpy as np


def print_board(board):
    for rows in board:
        print(rows)


def isSafe(board, row, col, side):

    # Checking for collision to the left of the placed queen
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Checking upper diagonal on the left side of the queen for collision
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking lower diagonal on the left side of the queen for collision
    for i, j in zip(range(row, side, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # there is no need to check for other directions as the board is populated
    # from left to right
    # function returns true when there is not collision detected
    return True


def place_queens(board, col, side):
    # the function is recursive, so it checks whether it has already filled all columns
    if col >= side:
        return True
    # it tries to place a queen in an i-th place
    for i in range(side):
        temp = int(i)
        # implementing randomness in order to achieve different results on every run,
        # queen on the first column is placed randomly, the outcome is dependent on this first placement
        # so it should yield different results just by placing the queen differently on the first column
        if col == 0:
            temp = np.random.randint(side)
        # checking whether it's possible to place the queen so that it doesn't attack any other existing ones
        if isSafe(board, temp, col, side):
            board[temp][col] = 1
            # calling itself with adjacent column
            if place_queens(board, col + 1, side):
                return True
            # this gets executed only if the queen can't be placed in this i-th place
            # because the board won't be populated properly
            board[temp][col] = 0
            # in such case the whole process will be repeated with consecutive queen placement
            # unless it's still the first column, as queen placement there is selected randomly
    return False


if __name__ == "__main__":
    x = int(input("Please enter the number of queens to solve:"))
    # creating the board: 0 -> empty space, 1 -> queen
    board = np.zeros((x, x), dtype=int)
    # calling function to populate the board with queens
    if not place_queens(board, 0, x):
        print("Solution does not exist")
    else:
        print_board(board)
