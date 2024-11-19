import time

from board import board
import pandas as pd
import heapq


def idastar_search(board: board):

    score = 0 # Variable, um den maximal erreichten Score zu speichern
    way = 0 # Variable, um die Weglänge bis zum besten Score zu speichern

    #expandiere ersten Knoten und speichere geringste Kosten eines Kindknotens in lowest_cost
    openlist = []
    #closedlist = []
    heapq.heappush(openlist, board) # Füge das Startboard in die Prioritätswarteschlange ein
    # Expandiere den ersten Knoten und finde die geringsten Kosten eines Kindknotens
    for succ in heapq.heappop(openlist).expand_board():
        # Prüfe, ob der Nachfolger nicht bereits in der Closed-List (bereits besuchte Knoten) ist
        if not succ.snake.head.copy() in succ.snake.closedlist:
            heapq.heappush(openlist, succ) # Füge den Nachfolger der Open-List hinzu
            #closedlist.append(succ.snake.head.copy())
    lowest_cost = openlist[-1].get_cost() # Setze die geringsten Kosten als neuen Threshold

    # Beginne die iterative Suche
    while True:
        # Solange der Threshold nicht überschritten wird, expandiere Knoten
        while openlist[-1].get_cost() <= lowest_cost:
            # Expandiere den Knoten mit den aktuell geringsten Kosten
            for succ in heapq.heappop(openlist).expand_board():
                # Prüfe, ob der Nachfolger nicht in der Closed-List ist
                if not succ.snake.head.copy() in succ.snake.closedlist:
                    heapq.heappush(openlist, succ) # Füge den Nachfolger zur Open-List hinzu
                    #closedlist.append(succ.snake.head.copy())

                    # Aktualisiere den besten Score und Weglänge, falls ein besserer Zustand gefunden wurde
                    if(succ.snake.score > score):
                        score = succ.snake.score
                        way = succ.snake.way_length
                        board = succ # Speichere den aktuellen besten Zustand als Ausgangspunkt
                        #print(pd.DataFrame(board.return_board()))
                        #print()
            # Wenn keine weiteren Knoten expandiert werden können, beende die Suche
            if (len(openlist) == 0):
                return (score, way) # Rückgabe des maximalen Scores und der Weglänge

        # Threshold überschritten: Setze einen neuen Threshold
        lowest_cost = openlist[-1].get_cost() # Aktualisiere den Threshold auf die niedrigsten Kosten

        # Leere die Open-List und beginne die Suche erneut mit dem besten bisher gefundenen Zustand
        openlist.clear()
        openlist.clear()
        openlist.append(board) # Füge den zuletzt besten Zustand wieder ein

        # Leere die Closed-List, um den nächsten Durchlauf nicht zu blockieren
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
            tupel = idastar_search(board(5,5,"M",fruit_factor=m * 0.1,snake_factor=n * 0.1))
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
            tupel = idastar_search(board(5,5,"E",fruit_factor=m * 0.1,snake_factor=n * 0.1))
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