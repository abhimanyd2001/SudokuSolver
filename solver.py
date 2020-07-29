import numpy as np
import random


class SudokuSolver:
    def __init__(self):
        self.puzzle = np.array([
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ])
        self.rows = self.puzzle.shape[0]
        self.columns = self.puzzle.shape[1]

        self.generate_puzzle()

    def __repr__(self):
        return "Rows: " + str(self.rows) + " Cols: " + str(self.columns)

    def generate_puzzle(self):
        for k in range(10):
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            self.puzzle[i, j] = random.randint(1, 9)
            if not self.is_solvable():
                self.puzzle[i, j] = None

        self.solver()

        running = 50
        while running > 0:
            print("Generating board...")
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.puzzle[i, j] is not None:
                self.puzzle[i, j] = None
                running -= 1
        print("Ready")



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
        initial_array = np.copy(self.puzzle)
        if self.validate_initial_board():
            solvable = self.backtracking_algorithm(self.puzzle)[0]
            self.puzzle = initial_array
            return solvable
        return False

    def solver(self):
        status = self.backtracking_algorithm(self.puzzle)
        if status[0] is True:
            return status[1]
        else:
            print("Sorry, the sudoku puzzle has no solution.")
            return None






