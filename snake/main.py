from board import board
import pandas as pd
from heuristik import *


board = board(10, 10)

print(pd.DataFrame(board.return_board()))
board.snake.move('U',board.fruit)
print()

print(pd.DataFrame(board.return_board()))
board.snake.move('R',board.fruit)
print()
print(pd.DataFrame(board.return_board()))
board.snake.move('D',board.fruit)
board.snake.move('D',board.fruit)
board.snake.move('D',board.fruit)
board.snake.move('L',board.fruit)
board.snake.move('L',board.fruit)
print()
print(pd.DataFrame(board.return_board()))
print(distance_euklid(board, 1,0).evaluate())
print(distance_manhattan(board, 1,0).evaluate())

