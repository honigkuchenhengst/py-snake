from fruit import fruit
class snake:
    def __init__(self, length, width, fruit):
        self.head = [1,1]
        self.body = [
            [1,1]
        ]
        self.length = length
        self.width = width
        self.score = 0
        self.way_length = 0 #bisher zurückgelegter weg der Schlange
        self.fruit = fruit
        self.game_over = False
        self.closedlist = [] #in der aktuellen Runde besuchte Felder, Felder sollen auf der Wegsuche zu einer Frucht je nur 1 Mal besucht werden

    #Bewegung der Schlange,
    #wenn game_over True ist, wird True zurückgegeben -> führt zur nicht berücksichtigung beim expandieren
    #wenn die Schlange eine Frucht isst, wird die Schlange länger und eine neue Frucht wird erzeugt
    def move(self, direction, fruit):
        if direction == 'U':    #U == up
            self.head[0] -= 1
        if direction == 'D':    #D == down
            self.head[0] += 1
        if direction == 'L':    #L == left
            self.head[1] -= 1
        if direction == 'R':    #R == right
            self.head[1] += 1

        self.way_length += 1
        self.gameOver()

        if fruit.get_position() != self.head and not self.game_over:
            self.body.pop(0)
        elif not self.game_over:
            blocked_tiles = self.body.copy()
            blocked_tiles.append(self.head.copy())
            fruit.spawn_fruit(blocked_tiles)
            self.score += 1
        else:
            return self.game_over

        self.body.append(self.head.copy())

        return self.game_over

    #ermittelt, ob die Schlange in sich selbst bewegt wurde, in den Rand oder ob das Board voll ist
    # gibt True zurück, falls einer dieser Fälle zutrifft
    def gameOver(self):
        if self.head in self.body:
            self.game_over = True
        if self.head[0] > self.length-1 or self.head[0] < 0 or self.head[1] > self.width-1 or self.head[1] < 0:
            self.game_over = True
        if self.fruit.get_position() == [-1,-1]:
            self.game_over = True

    def get_position(self):
        return self.head.copy()

    def copy(self, fruit: fruit):
        copy = snake(self.length, self.width, fruit)
        copy.score = self.score
        copy.head = self.head.copy()
        copy.body = self.body.copy()
        copy.game_over = self.game_over
        copy.way_length = self.way_length
        copy.closedlist = self.closedlist.copy()
        return copy