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
                        break
                        #print(pd.DataFrame(board.return_board()))
                        #print()
            if (len(openlist) == 0):
                return (score, way)
        lowest_cost = openlist[-1].get_cost()
        openlist.clear()
        openlist.append(board)
        board.snake.closedlist.clear()

way = 0
scores = 0
#board = board(5, 5,"M",fruit_factor=1,snake_factor=0)
for m in range(6):
    for n in range(4):
        for i in range(50):
            # print("-----------------------------------------------------------------------------")
            tupel = idastar_search(board(5,5,"M",fruit_factor=m,snake_factor=n))
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
            tupel = idastar_search(board(6,6,"E",fruit_factor=10*m,snake_factor=10*n))
            scores += tupel[0]
            way += tupel[1]
        print(f"Ida_star: fruit_factor= {10*m} and snake_factor= {10*n}")
        print(scores / 50)
        print(way / 50)
        print("_____")
        way = 0
        scores = 0


