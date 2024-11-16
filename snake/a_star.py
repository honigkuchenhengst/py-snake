from board import board
import pandas as pd


def astar_search(board: board):
    openlist = []
    openlist.append(board)
    score = 0
    while len(openlist) > 0:
        current_board = openlist.pop()
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
        openlist.sort(key=lambda x: x.snake.way_length + x.heuristic.evaluate(),reverse = True)
    return score


scores = 0
board = board(6, 6,"M",fruit_factor=1,snake_factor=0)
for i in range(1):
    scores += astar_search(board)
print(scores)
