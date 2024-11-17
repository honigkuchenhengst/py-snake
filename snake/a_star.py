from board import board
import pandas as pd
import heapq


def astar_search(board: board):
    openlist = []
    heapq.heappush(openlist,board)
    score = 0
    way = 0
    while len(openlist) > 0:
        current_board = heapq.heappop(openlist)
        current_board.snake.closedlist.append(current_board.snake.head.copy())

        if current_board.snake.score > score:
            #print(pd.DataFrame(current_board.return_board()))
            #print()
            score = current_board.snake.score
            openlist.clear()
            current_board.snake.closedlist.clear()
            way = current_board.snake.way_length
            heapq.heappush(openlist, current_board)

        for succ in current_board.expand_board():
            if not succ.snake.head.copy() in succ.snake.closedlist:
                heapq.heappush(openlist, succ)

    return (score, way)

way = 0
scores = 0

for m in range(6):
    for n in range(4):
        for i in range(50):
            # print("-----------------------------------------------------------------------------")
            tupel = astar_search(board(5,5,"M",fruit_factor=m,snake_factor=n))
            scores += tupel[0]
            way += tupel[1]
        print(f"Ida_star: fruit_factor= {m} and snake_factor= {n}")
        print(scores / 50)
        print(way / 50)
        print("_____")
        way = 0
        scores = 0

for m in range(6):
    for n in range(4):
        for i in range(50):
            # print("-----------------------------------------------------------------------------")
            tupel = astar_search(board(6,6,"E",fruit_factor=10*m,snake_factor=10*n))
            scores += tupel[0]
            way += tupel[1]
        print(f"Ida_star: fruit_factor= {10*m} and snake_factor= {10*n}")
        print(scores / 50)
        print(way / 50)
        print("_____")
        way = 0
        scores = 0
