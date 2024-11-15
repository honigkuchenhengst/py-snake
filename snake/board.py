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
        board[self.snake.head[0]][self.snake.head[1]] = 3
        return board

    def get_snake_head(self):
        return self.snake.get_position()

    def get_fruit_position(self):
        return self.fruit.get_position()

    def copy(self):
        copy = type(self)(self.length, self.width)
        copy.fruit = self.fruit.copy()
        copy.snake = self.snake.copy(copy.fruit)
        return copy

    def expand_board(self):
        copies = []
        n = 0
        for i in range(4):
            copies.append(self.copy())
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