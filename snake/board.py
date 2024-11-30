from fruit import fruit
from snake import snake
from heuristik import distance_euklid, distance_manhattan

class board:
    #heuristic (str): Heuristiktyp ("E" für euklidisch, "M" für Manhattan)
    #fruit_factor (float): Gewichtung für die Distanz zur Frucht in der Heuristik
    #snake_factor (float): Gewichtung für die Schlange in der Heuristik
    def __init__(self, length, width, heuristic="M",fruit_factor = 1,snake_factor = 0):
        self.length = length
        self.width = width
        self.fruit = fruit(length, width)
        self.snake = snake(length, width, self.fruit)
        if heuristic == "E":
            self.heuristic = distance_euklid(self,fruit_factor,snake_factor).evaluate()
        elif heuristic == "M":
            self.heuristic = distance_manhattan(self,fruit_factor,snake_factor).evaluate()

    #Gibt das Spielfeld als 2D-Liste zurück
    def return_board(self):
        board = [[0 for i in range(self.length)] for j in range(self.width)]
        for position in self.snake.body:
            board[position[0]][position[1]] = 1
        board[self.fruit.get_position()[0]][self.fruit.get_position()[1]] = 2
        board[self.snake.head[0]][self.snake.head[1]] = 3
        return board

    def get_snake_head(self):
        return self.snake.get_position()

    def get_fruit_position(self):
        return self.fruit.get_position()

    #Erstellt eine Kopie des Spielfelds, inklusive Schlange, Frucht und Heuristik
    def copy(self):
        copy = type(self)(self.length, self.width)
        copy.fruit = self.fruit.copy()
        copy.snake = self.snake.copy(copy.fruit)
        copy.heuristic = self.heuristic
        return copy

    #Generiert alle möglichen Nachfolgezustände durch Bewegung der Schlange
    def expand_board(self):
        copies = [] #Liste für die Kopien des Spielfelds
        n = 0 #Index für Bewegungen
        for i in range(4):
            copies.append(self.copy())
        #Versuche Bewegungen in jede Richtung, entferne ungültige Zustände
        if copies[n].snake.move("U",copies[n].fruit):
            copies.pop(n)
            n -= 1
        n += 1
        if copies[n].snake.move("D",copies[n].fruit):
            copies.pop(n)
            n -= 1
        n += 1
        if copies[n].snake.move("L",copies[n].fruit):
            copies.pop(n)
            n -= 1
        n += 1
        if copies[n].snake.move("R",copies[n].fruit):
            copies.pop(n)
            n -= 1
        return copies

    #Vergleichsfunktion für die Priorität im A*-Algorithmus.
    def __lt__(self, other):
        return self.heuristic + self.snake.way_length < other.heuristic + other.snake.way_length

    #Die berechneten Kosten
    def get_cost(self):
        return self.heuristic + self.snake.way_length