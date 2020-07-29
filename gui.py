import math

import pygame

import copy

from solver import SudokuSolver

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Sudoku Solver")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_YELLOW = (215, 230, 177)
myFont = pygame.font.SysFont("Times New Roman", 18)

#get time
def get_time():
    milliseconds = pygame.time.get_ticks()
    seconds = milliseconds / 1000
    time = myFont.render("Seconds Passed: " + str(seconds), 5, BLACK)
    screen.blit(time, (200, 500))

#Game over
def game_over():
    for i in range(sudoku.rows):
        for j in range(sudoku.columns):
            if sudoku.puzzle[i, j] is None:
                return False
    return True

# Making the grid layout
startX = 20
endX = 380
deltaX = int((endX - startX) / 9)

startY = 20
endY = 380
deltaY = int((endY - startY) / 9)


def draw_grid():
    counter = 0
    for x in range(startX, endX + 1, deltaX):
        if counter % 3 == 0:
            pygame.draw.line(screen, BLACK, (x, startY), (x, endY), 3)
        else:
            pygame.draw.line(screen, BLACK, (x, startY), (x, endY), 1)
        counter += 1
    counter = 0
    for y in range(startY, endY + 1, deltaY):
        if counter % 3 == 0:
            pygame.draw.line(screen, BLACK, (startX, y), (endX, y), 3)
        else:
            pygame.draw.line(screen, BLACK, (startX, y), (endX, y), 1)
        counter += 1


# Display initial numbers
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


def display_puzzle(board):
    centerX = startX + int(deltaX / 2) - 5
    centerY = startY + int(deltaY / 2) - 10
    for i in range(board.rows):
        for j in range(board.columns):
            if board.puzzle[i, j] is not None:
                myNum = myFont.render(str(board.puzzle[i, j]), 1, BLACK)
                screen.blit(myNum, (centerX, centerY))
            centerX += deltaX
        centerX = startX + int(deltaX / 2)
        centerY += deltaY


# Allowing for user input
def highlight_box(x, y):
    while (x - 20) % 40 != 0:
        x -= 1
    while (y - 20) % 40 != 0:
        y -= 1
    screen.fill(LIGHT_YELLOW, (x, y, deltaX, deltaY))


# Get the cell of the sudoku puzzle that has been clicked on
def get_cell(x, y):
    # return (math.floor((x-startX)/deltaX), math.floor((y-startY)/deltaY))
    return math.floor((y - startY) / deltaY), math.floor((x - startX) / deltaX)

def update_cell(x, y):
    (i, j) = get_cell(x, y)
    sudoku.puzzle[i, j] = user_choice

def remove_cell_entry(x, y):
    i, j = get_cell(x, y)
    sudoku.puzzle[i, j] = None


running = True
isClicked = False
xClick = 0
yClick = 0
user_choice = 0
while running:
    screen.fill((255, 255, 255))
    if not game_over():
        get_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if (x >= startX and x <= endX) and (y >= startY and y <= endY):
                isClicked = True
                xClick = x
                yClick = y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isClicked = False

            if event.key == pygame.K_e:
                sudoku.solver()

            if isClicked:
                if event.key == pygame.K_1:
                    user_choice = 1
                    update_cell(xClick, yClick)
                if event.key == pygame.K_2:
                    user_choice = 2
                    update_cell(xClick, yClick)
                if event.key == pygame.K_3:
                    user_choice = 3
                    update_cell(xClick, yClick)
                if event.key == pygame.K_4:
                    user_choice = 4
                    update_cell(xClick, yClick)
                if event.key == pygame.K_5:
                    user_choice = 5
                    update_cell(xClick, yClick)
                if event.key == pygame.K_6:
                    user_choice = 6
                    update_cell(xClick, yClick)
                if event.key == pygame.K_7:
                    user_choice = 7
                    update_cell(xClick, yClick)
                if event.key == pygame.K_8:
                    user_choice = 8
                    update_cell(xClick, yClick)
                if event.key == pygame.K_9:
                    user_choice = 9
                    update_cell(xClick, yClick)

                if event.key == pygame.K_RETURN:
                    sudoku_copy = copy.deepcopy(sudoku)
                    if not sudoku_copy.is_solvable():
                        remove_cell_entry(xClick, yClick)
                if event.key == pygame.K_DELETE:
                    remove_cell_entry(xClick, yClick)



    if isClicked:
        highlight_box(xClick, yClick)

    draw_grid()
    display_puzzle(sudoku)
    pygame.display.update()
