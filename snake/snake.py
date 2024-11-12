from fruit import fruit
class snake:
    def __init__(self, length, width, my_fruit):
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
        self.fruit = my_fruit
        self.game_over = False

    def move(self, direction, fruit: fruit):
        if direction == 'U':    #U == up
            self.head[0] -= 1
        if direction == 'D':    #D == down
            self.head[0] += 1
        if direction == 'L':    #L == left
            self.head[1] -= 1
        if direction == 'R':    #R == right
            self.head[1] += 1

        if fruit.get_position() != self.head:
            tmp = self.body[-1]
            self.body.pop(0)
            fruit.update_space(self.head,tmp)
        else:
            fruit.spawn_fruit()
            self.score += 1

        self.body.append(self.head.copy())
        return True

    def game_over(self):
        if self.head in self.body:
            self.game_over = True
        if self.head[0] > self.length or self.head[0] < 0 or self.head[1] > self.width or self.head[1] < 0:
            self.game_over = True

    def get_position(self):
        return self.head.copy()