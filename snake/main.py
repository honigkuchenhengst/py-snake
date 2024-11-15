from board import board
import pandas as pd
from heuristik import *



scores = 0

board = board(6, 6)
for i in range(50):
    openlist = []
    openlist.append(board)

    score = 0

    #BFS
    while len(openlist) > 0:
        current_board = openlist.pop(0)
        current_board.snake.closedlist.append(current_board.snake.head.copy())

        if current_board.snake.score > score:
            print(pd.DataFrame(current_board.return_board()))
            score = current_board.snake.score
            openlist.clear()
            current_board.snake.closedlist.clear()
            openlist.append(current_board)

        for succ in current_board.expand_board():
            if not succ.snake.head.copy() in current_board.snake.closedlist:
                openlist.append(succ)
    print(score)
    scores += score

#0 are empty tiles
#1 are the body of the snake
#2 is the fruit
#3 is the head
print(scores / 50)





