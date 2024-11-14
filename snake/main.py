from board import board
import pandas as pd
from heuristik import *


board = board(10, 10)


for copy in board.expand_board():
    print(pd.DataFrame(copy.return_board()))
    print()

