import pygame
import time
import random

print("Wilkommen bei Sssnake!")

snake_speed = 15

#screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

#window
pygame.display.set_caption('Timon und Luca\'s Sssnake')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS (frames per second) controller
fps = pygame.time.Clock()

#define snake position
snake_position = [100, 50]

#define snake body (start)
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

#futter position
futter_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                   random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
futter_spawn = True

#default snake direction
direction = 'RIGHT'
change_to = direction

#score (start)
score = 0

def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

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
    game_over_surface = my_font.render('Dein Score ist : ' + str(score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

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


#game loop
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == futter_position[0] and snake_position[1] == futter_position[1]:
        score += 10
        futter_spawn = False
    else:
        snake_body.pop()

    if not futter_spawn:
        futter_position = [random.randrange(1, (SCREEN_WIDTH// 10)) * 10,
                          random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]

    futter_spawn = True
    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(
        futter_position[0], futter_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)


