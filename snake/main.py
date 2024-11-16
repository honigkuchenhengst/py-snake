from board import board
import pandas as pd
from heuristik import *


#Variable zum Speichern des Gesamtscores über mehrere Simulationen
scores = 0

#Board initialisieren (6x6)
board = board(6, 6)

# 50 Iterationen, um mehrere Spiele zu simulieren und Durchschnittswerte zu berechnen
for i in range(50):
    # Boards, die noch nicht expandiert wurden
    openlist = []
    openlist.append(board)

    #Variable zur Speicherung des höchsten Scores im aktuellen Spiel
    score = 0

    #BFS -> alle möglichen Spielzüge zu evaluieren
    while len(openlist) > 0:
        #Das nächste Board aus der openlist holen (FIFO)
        current_board = openlist.pop(0)
        #aktuelle Position der Snake (Kopf) zur closedlist hinzufügen
        current_board.snake.closedlist.append(current_board.snake.head.copy())

        #Wenn der aktuelle Score höher ist als der bisherige Score:
        if current_board.snake.score > score:
            #Board als Tabelle ausgeben, aktuellen Zustand darstellen
            print(pd.DataFrame(current_board.return_board()))

            #aktualisiere höchsten score
            score = current_board.snake.score

            #zurücksetzen der lists, da besserer Zustand gefunden
            openlist.clear()
            current_board.snake.closedlist.clear()

            openlist.append(current_board)

        #Erweitere das aktuelle Board, um alle möglichen Nachfolger (Züge) zu generieren
        for succ in current_board.expand_board():
            if not succ.snake.head.copy() in current_board.snake.closedlist: #nicht bereits besucht
                openlist.append(succ)

    #höchster aktueller score
    print(score)
    scores += score #zum Gesamtscore addieren

print(scores / 50) #Durchschnitt score pro Simulation

#0 -> leere Felder
#1 -> Körper der Schlange
#2 -> Frucht
#3 -> Kopf der Schlange
