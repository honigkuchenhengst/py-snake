import pygame
import time

from pygame.board import Board
from pygame.food import Food
from snake import Snake

print("Wilkommen bei Sssnake!")

board = Board()
snake = Snake()
food = Food(board.SCREEN_WIDTH,board.SCREEN_HEIGHT)
key_pressed = False

snake_speed = 20

pygame.init()
#window
pygame.display.set_caption('Timon und Luca\'s Sssnake')
screen = pygame.display.set_mode((board.SCREEN_WIDTH, board.SCREEN_HEIGHT))
fps = pygame.time.Clock()

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(board.score), True, color)

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    screen.blit(score_surface, score_rect)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Dein Score ist : ' + str(board.score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (board.SCREEN_WIDTH / 2, board.SCREEN_HEIGHT / 4)

    # blit will draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the
    # program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()

path ="RRRRDDDDLLLLUUUURRRRDDDDLLLLUUUURRRRDDDDLLLLUUUURRRRRRRDDDDLLLLUUUURRRRDDDDLLLLUUUU"
pathindex = 0
#game loop
while True:
    key_pressed = False

    while not key_pressed:
        #event = pygame.event.wait()
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_UP:
        #        snake.snake_position[1] -= 10
        #    if event.key == pygame.K_DOWN:
        #        snake.snake_position[1] += 10
        #    if event.key == pygame.K_LEFT:
        #        snake.snake_position[0] -= 10
        #    if event.key == pygame.K_RIGHT:
        #        snake.snake_position[0] += 10
        #    key_pressed = True
        if path[pathindex] == 'U':
            snake.snake_position[1] -= 10
        if path[pathindex] == 'D':
            snake.snake_position[1] += 10
        if path[pathindex] == 'L':
            snake.snake_position[0] -= 10
        if path[pathindex] == 'R':
            snake.snake_position[0] += 10
        key_pressed = True
        pathindex += 1


    # Game Over conditions
    if snake.snake_position[0] < 0 or snake.snake_position[0] > board.SCREEN_WIDTH - 10:
        game_over()
    if snake.snake_position[1] < 0 or snake.snake_position[1] > board.SCREEN_HEIGHT - 10:
        game_over()

    # Touching the snake body
    for block in snake.snake_body[1:]:
        if snake.snake_position[0] == block[0] and snake.snake_position[1] == block[1]:
            game_over()







    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake.snake_body.insert(0, list(snake.snake_position))
    if snake.snake_position[0] == food.food_position[0] and snake.snake_position[1] == food.food_position[1]:
        board.score += 10
        food.food_spawn = False
    else:
        food.update_space(snake.snake_body.pop(), list(snake.snake_position))

    if not food.food_spawn:
        food.spawn_food()

    screen.fill(black)

    for pos in snake.snake_body:
        pygame.draw.rect(screen, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(
        food.food_position[0], food.food_position[1], 10, 10))



    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)


