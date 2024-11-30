
import scipy.spatial.distance as dist

#Heuristik nach der manhattan-Distanz, welche sich nach |(x1-x2)| + |(y1-y2)| berechnet
class distance_manhattan:

    def copy(self):
        return type(self)(self.board,self.fruit_factor,self.snake_factor)
    def __init__(self, board, fruit_factor, snake_factor):
        self.board = board
        self.fruit_factor = fruit_factor
        self.snake_factor = snake_factor

    def evaluate(self):
        if self.board.snake.game_over:
            return 99999999
        snake_pos = self.board.get_snake_head()
        fruit_pos = self.board.get_fruit_position()
        #abstand zur frucht
        fruit_distance = abs(snake_pos[0] - fruit_pos[0]) + abs(snake_pos[1] - fruit_pos[1])
        #abstand zur gemittelten distanz aller körperteile der schlange
        snake_distance = 0
        for body_part in self.board.snake.body:
            snake_distance += abs(snake_pos[0] - body_part[0]) + abs(snake_pos[1] - body_part[1])
        snake_distance = snake_distance / len(self.board.snake.body)

        #gewichtung der distanz zur frucht/zum körper
        return self.fruit_factor * fruit_distance + self.snake_factor * snake_distance


#Heuristik nach der Euklid-Distanz, welche sich nach sqrt((x1-x2)^2+(y1-y2^2)) berechnet
class distance_euklid:

    def copy(self):
        return type(self)(self.board,self.fruit_factor,self.snake_factor)
    def __init__(self, board, fruit_factor, snake_factor):
        self.board = board
        self.fruit_factor = fruit_factor
        self.snake_factor = snake_factor

    def evaluate(self):
        if self.board.snake.game_over:
            return 99999999
        snake_pos = self.board.get_snake_head()
        fruit_pos = self.board.get_fruit_position()
        #abstand zur frucht
        fruit_distance = dist.euclidean(snake_pos, fruit_pos)
        #abstand zur gemittelten distanz aller körperteile der schlange
        snake_distance = 0
        for body_part in self.board.snake.body:
            snake_distance += dist.euclidean(snake_pos, body_part)
        snake_distance = snake_distance / len(self.board.snake.body)

        #gewichtung der distanz zur frucht/zum körper
        return self.fruit_factor * fruit_distance + self.snake_factor * snake_distance

