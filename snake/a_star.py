from board import board
import pandas as pd
import heapq

#Implementiert den A*-Algorithmus für die Suche nach optimalen Zügen im snake game
def astar_search(board: board):
    openlist = [] #Prioritätswarteschlange für offene Zustände
    heapq.heappush(openlist,board)
    score = 0 #Höchste erreichte Punktzahl
    way = 0 #Zurückgelegter Weg (Anzahl der Bewegungen)

    while len(openlist) > 0:
        current_board = heapq.heappop(openlist) #Entferne das board mit den niedrigsten Kosten
        current_board.snake.closedlist.append(current_board.snake.head.copy()) #Markiere aktuellen Schlangenkopf als besucht

        #Prüfe, ob die aktuelle Punktzahl höher ist als der bisherige Score
        if current_board.snake.score > score:
            #Gib das Spielfeld aus, falls ein neuer Highscore erreicht wurde
            print(pd.DataFrame(current_board.return_board()))
            print()
            score = current_board.snake.score
            openlist.clear()
            current_board.snake.closedlist.clear()
            way = current_board.snake.way_length #Aktualisiere die Weglänge
            heapq.heappush(openlist, current_board) #Füge das aktuelle Spielfeld erneut hinzu

        #Generiere alle möglichen Nachfolgezustände
        for succ in current_board.expand_board():
            if not succ.snake.head.copy() in succ.snake.closedlist: #nicht bereits besucht
                heapq.heappush(openlist, succ)

    return (score, way) #höchster aktueller score und Weglänge

#Initialisierung der Variablen für das Gesamtergebnis
way = 0 #Summe der zurückgelegten Wege
scores = 0 #Summe der erreichten Punktzahlen

#Erstelle ein neues Spielfeld mit den gewünschten Parametern
board = board(5, 5,"M",fruit_factor=1,snake_factor=0)

#Führe x Simulationen aus
for i in range(50):
    print ("-----------------------------------------------------------------------------")
    tupel = astar_search(board)
    scores += tupel[0]
    way += tupel[1]

#Gib die durchschnittlichen Ergebnisse aus
print(scores/50)
print(way/50)
