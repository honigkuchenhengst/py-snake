from fruit import fruit
from snake import snake


class board:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.fruit = fruit(length, width)
        self.snake = snake(length, width, self.fruit)

    def return_board(self):
        board = [[0 for i in range(self.length)] for j in range(self.width)]
        for position in self.snake.body:
            board[position[0]][position[1]] = 1
        board[self.fruit.get_position()[0]][self.fruit.get_position()[1]] = 2
        return board

    def get_snake_head(self):
        return self.snake.get_position()

    def get_fruit_position(self):
        return self.fruit.get_position()