from fruit import fruit
class snake:
    def __init__(self, length, width, fruit):
        self.head = [1,5]
        self.body = [
            [1,1],
            [1,2],
            [1,3],
            [1,4],
            [1,5]
        ]
        self.length = length
        self.width = width
        self.score = 0
        self.fruit = fruit
        self.game_over = False

    def move(self, direction, fruit):
        moving_into_snake = False
        if direction == 'U':    #U == up
            self.head[0] -= 1
            if self.head in self.body:
                moving_into_snake = True
        if direction == 'D':    #D == down
            self.head[0] += 1
            if self.head in self.body:
                moving_into_snake = True
        if direction == 'L':    #L == left
            self.head[1] -= 1
            if self.head in self.body:
                moving_into_snake = True
        if direction == 'R':    #R == right
            self.head[1] += 1
            if self.head in self.body:
                moving_into_snake = True

        if fruit.get_position() != self.head and not moving_into_snake:
            tmp = self.body[-1]
            self.body.pop(0)
            fruit.update_space(self.head,tmp)
        elif not moving_into_snake:
            fruit.spawn_fruit()
            self.score += 1
        else:
            return False

        self.body.append(self.head.copy())
        return True

    def game_over(self):
        if self.head in self.body:
            self.game_over = True
        if self.head[0] > self.length or self.head[0] < 0 or self.head[1] > self.width or self.head[1] < 0:
            self.game_over = True

    def get_position(self):
        return self.head.copy()

    def copy(self, fruit: fruit):
        copy = snake(self.length, self.width, fruit)
        copy.score = self.score
        copy.head = self.head.copy()
        copy.body = self.body.copy()
        copy.game_over = self.game_over
        return copy