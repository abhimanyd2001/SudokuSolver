## Sudoku Solver

### Files
`gui.py`: Graphical interface of the sudoku solver.  This is implemented in pygame.  

`solver.py`: Responsible for the algorithm of solving the sudoku board.  This is implemented as a class, and the main
solver method uses backtracking in order to solve the sudoku puzzle by recursively calling itself after a move is made 
to see if the board has a solution.

### Rules of the GUI:
After launching gui.py, you will be shown a partially filled sudoku puzzle.  The goal is to fill in the remaining tiles.
To bring a tile into focus, simply `left click` on it.  This will highlight the tile, and you can now
type in a number in order to fill the board in.  

To confirm this choice, press `enter`.  If it is a valid choice, the tile will remain filled, otherwise it will get 
removed and you must continue trying to choose a number.  

If you want to clear the tile instead of confirming the choice, press `delete`.  This will clear the contents of the 
tile regardless of whether it is the right choice or not.  

If you would like the see the board solved, press `E`.  This will fill in the board contents.
