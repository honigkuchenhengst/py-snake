import time

from board import board
import pandas as pd
from heuristik import *


def bfs(board: board):
        # Boards, die noch nicht expandiert wurden
    openlist = []
    openlist.append(board)

        #Variable zur Speicherung des höchsten Scores im aktuellen Spiel
    score = 0
    way = 0

        #BFS -> alle möglichen Spielzüge zu evaluieren
    while len(openlist) > 0:
            #Das nächste Board aus der openlist holen (FIFO)
        current_board = openlist.pop(0)
            #aktuelle Position der Snake (Kopf) zur closedlist hinzufügen
        current_board.snake.closedlist.append(current_board.snake.head.copy())

            #Wenn der aktuelle Score höher ist als der bisherige Score:
        if current_board.snake.score > score:
                #Board als Tabelle ausgeben, aktuellen Zustand darstellen
            #print(pd.DataFrame(current_board.return_board()))

                #aktualisiere höchsten score
            score = current_board.snake.score
            way = current_board.snake.way_length

                #zurücksetzen der lists, da besserer Zustand gefunden
            openlist.clear()
            current_board.snake.closedlist.clear()

            openlist.append(current_board)

            #Erweitere das aktuelle Board, um alle möglichen Nachfolger (Züge) zu generieren
        for succ in current_board.expand_board():
            if not succ.snake.head.copy() in current_board.snake.closedlist: #nicht bereits besucht
                openlist.append(succ)
    return(score,way)


scores= 0
way = 0
print("alg,heuristik,boardgroesse,wiederholungen,gesamtlaufzeit(s),gesamtscore,gesamtweg,gewichtungFood,gewichtungSnake")
for m in range(6):
    for n in range(4):
        start_time = time.perf_counter()  # Starte die Zeitmessung
        for i in range(500):
            # print("-----------------------------------------------------------------------------")
            tupel = bfs(board(5,5,"M",fruit_factor=m,snake_factor=n))
            scores += tupel[0]
            way += tupel[1]
        end_time = time.perf_counter()
        #print(f"Ida_star: fruit_factor= {m} and snake_factor= {n}")
        #print(scores / 500)
        #print(way / 500)
        #print(f"Laufzeit von 500 mal IDA*: {(end_time - start_time)} Sekunden")
        #print("_____")
        print(f"bfs,m,5x5,500,{(end_time - start_time):.3f},{scores},{way},{m},{n}")
        way = 0
        scores = 0
for m in range(6):
    for n in range(4):
        start_time = time.perf_counter()  # Starte die Zeitmessung
        for i in range(500):
            # print("-----------------------------------------------------------------------------")
            tupel = bfs(board(5,5,"E",fruit_factor=m,snake_factor=n))
            scores += tupel[0]
            way += tupel[1]
        end_time = time.perf_counter()
        #print(f"Ida_star: fruit_factor= {m} and snake_factor= {n}")
        #print(scores / 500)
        #print(way / 500)
        #print(f"Laufzeit von 500 mal IDA*: {(end_time - start_time)} Sekunden")
        #print("_____")
        print(f"bfs,e,5x5,500,{(end_time - start_time):.3f},{scores},{way},{m},{n}")

#0 -> leere Felder
#1 -> Körper der Schlange
#2 -> Frucht
#3 -> Kopf der Schlange
