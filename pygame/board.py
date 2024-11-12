import pygame

class Board:
    def __init__(self):
        self.SCREEN_WIDTH = 200
        self.SCREEN_HEIGHT = 200
        self.score = 0


    def handling_key_events(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    snake.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    snake.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    snake.change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if snake.change_to == 'UP' and snake.direction != 'DOWN':
            snake.direction = 'UP'
        if snake.change_to == 'DOWN' and snake.direction != 'UP':
            snake.direction = 'DOWN'
        if snake.change_to == 'LEFT' and snake.direction != 'RIGHT':
            snake.direction = 'LEFT'
        if snake.change_to == 'RIGHT' and snake.direction != 'LEFT':
            snake.direction = 'RIGHT'

    def moving_the_snake(self, snake):
        if snake.direction == 'UP':
            snake.snake_position[1] -= 10
        if snake.direction == 'DOWN':
            snake.snake_position[1] += 10
        if snake.direction == 'LEFT':
            snake.snake_position[0] -= 10
        if snake.direction == 'RIGHT':
            snake.snake_position[0] += 10