import numpy as np
import copy

class SudokuSolver:
    def __init__(self, puzzle):
        puzzle = np.array(puzzle)
        if self.check_invariants(puzzle):
            self.puzzle = puzzle
            self.rows = puzzle.shape[0]
            self.columns = puzzle.shape[1]

    def __repr__(self):
        return "Rows: " + str(self.rows) + " Cols: " + str(self.columns)

    def check_invariants(self, puzzle):
        shape = puzzle.shape
        if shape != (9, 9):
            return False
        return True

    def get_empty_cell(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.puzzle[i, j] is None:
                    return i, j
        return None

    def initial_check(self, i, j, cell):
        # Get the row, column, and subset
        row = self.puzzle[i, :]

        column = self.puzzle[:, j]

        row_start = i - i % 3
        row_end = row_start + 3
        col_start = j - j % 3
        col_end = col_start + 3
        subset = self.puzzle[row_start:row_end, col_start:col_end]

        # See if the cell exists in these three
        if cell in row:
            return False
        if cell in column:
            return False
        if cell in subset:
            return False
        return True

    def validate_initial_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.puzzle[i, j] is not None:
                    num = self.puzzle[i, j]
                    self.puzzle[i, j] = None
                    is_valid = self.initial_check(i, j, num)
                    self.puzzle[i, j] = num
                    if not is_valid:
                        return False
        return True

    def backtracking_algorithm(self, solved_array):
        if self.get_empty_cell() is None:
            return (True, solved_array)
        else:
            (i, j) = self.get_empty_cell()
            for num in range(1, 10):
                if self.initial_check(i, j, num):
                    solved_array[i, j] = num
                    status = self.backtracking_algorithm(solved_array)
                    if status[0] is True:
                        return status
                    else:
                        solved_array[i, j] = None
            return (False, solved_array)

    def is_solvable(self):
        if self.validate_initial_board():
            return self.backtracking_algorithm(self.puzzle)[0]
        return False

    def solver(self):
        status = self.backtracking_algorithm(self.puzzle)
        if status[0] is True:
            return status[1]
        else:
            print("Sorry, the sudoku puzzle has no solution.")
            return None


sudoku = SudokuSolver([
    [None, None, None, 6, None, 1, None, None, None],
    [None, None, None, None, 7, 9, 1, None, None],
    [4, None, None, 5, None, None, None, 3, None],
    [2, None, 6, None, None, None, None, 4, 9],
    [None, None, 5, None, None, None, 3, None, None],
    [8, 3, None, None, None, None, 2, None, 1],
    [None, 9, None, None, None, 5, None, None, 7],
    [None, None, 3, 9, 6, None, None, None, None],
    [None, None, None, 2, None, 4, None, None, None],
])

print(sudoku.is_solvable())

