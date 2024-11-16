from board import board
import pandas as pd
import heapq


def idastar_search(board: board):

    score = 0
    way = 0

    #expandiere ersten Knoten und speichere geringste Kosten eines Kindknotens in cheapest_child
    openlist = []
    heapq.heappush(openlist, board)
    for succ in heapq.heappop(openlist).expand_board():
        if not succ.snake.head.copy() in succ.snake.closedlist:
            heapq.heappush(openlist, succ)
    lowest_cost = openlist[-1].get_cost()


    while True:
        while openlist[-1].get_cost() <= lowest_cost:
            for succ in heapq.heappop(openlist).expand_board():
                if not succ.snake.head.copy() in succ.snake.closedlist:
                    heapq.heappush(openlist, succ)
                    if(succ.snake.score > score):
                        score = succ.snake.score
                        way = succ.snake.way_length
                        board = succ
                        #print(pd.DataFrame(board.return_board()))
                        #print()
            if (len(openlist) == 0):
                return (score, way)
        lowest_cost = openlist[-1].get_cost()

        openlist.clear()
        openlist.append(board)

way = 0
scores = 0
board = board(5, 5,"M",fruit_factor=1,snake_factor=1)
for i in range(50):
    print("-----------------------------------------------------------------------------")
    tupel = idastar_search(board)
    scores += tupel[0]
    way += tupel[1]


print(scores/50)
print(way/50)