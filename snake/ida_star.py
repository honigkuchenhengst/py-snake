import time

from board import board
import pandas as pd
import heapq


def idastar_search(board: board):

    score = 0
    way = 0

    #expandiere ersten Knoten und speichere geringste Kosten eines Kindknotens in cheapest_child
    openlist = []
    #closedlist = []
    heapq.heappush(openlist, board)
    for succ in heapq.heappop(openlist).expand_board():
        if not succ.snake.head.copy() in succ.snake.closedlist:
            heapq.heappush(openlist, succ)
            #closedlist.append(succ.snake.head.copy())
    lowest_cost = openlist[-1].get_cost()


    while True:
        while openlist[-1].get_cost() <= lowest_cost:
            for succ in heapq.heappop(openlist).expand_board():
                if not succ.snake.head.copy() in succ.snake.closedlist:
                    heapq.heappush(openlist, succ)
                    #closedlist.append(succ.snake.head.copy())

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
        board.snake.closedlist.clear()



#Führe x Simulationen aus & Zeitmessung
way = 0
scores = 0
#board = board(5, 5,"M",fruit_factor=1,snake_factor=0)

print("alg,heuristik,boardgroesse,wiederholungen,gesamtlaufzeit(s),gesamtscore,gesamtweg,gewichtungFood,gewichtungSnake,closedListglobal")
for m in range(6):
    for n in range(4):
        start_time = time.perf_counter()  # Starte die Zeitmessung
        for i in range(500):
            # print("-----------------------------------------------------------------------------")
            tupel = idastar_search(board(5,5,"M",fruit_factor=m,snake_factor=n))
            scores += tupel[0]
            way += tupel[1]
        end_time = time.perf_counter()
        #print(f"Ida_star: fruit_factor= {m} and snake_factor= {n}")
        #print(scores / 500)
        #print(way / 500)
        #print(f"Laufzeit von 500 mal IDA*: {(end_time - start_time)} Sekunden")
        #print("_____")
        print(f"idaStar,m,5x5,500,{(end_time - start_time):.3f},{scores},{way},{m},{n},no")
        way = 0
        scores = 0
for m in range(6):
    for n in range(4):
        start_time = time.perf_counter()  # Starte die Zeitmessung
        for i in range(500):
            # print("-----------------------------------------------------------------------------")
            tupel = idastar_search(board(5,5,"E",fruit_factor=m,snake_factor=n))
            scores += tupel[0]
            way += tupel[1]
        end_time = time.perf_counter()
        #print(f"Ida_star: fruit_factor= {m} and snake_factor= {n}")
        #print(scores / 500)
        #print(way / 500)
        #print(f"Laufzeit von 500 mal IDA*: {(end_time - start_time)} Sekunden")
        #print("_____")
        print(f"idaStar,e,5x5,500,{(end_time - start_time):.3f},{scores},{way},{m},{n},no")
        way = 0
        scores = 0