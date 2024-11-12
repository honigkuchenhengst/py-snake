class Snake:
    def __init__(self):
        self.snake_position = [100, 50]
        self.snake_body = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]

        # default snake direction
        self.direction = 'RIGHT'
        self.change_to = self.direction