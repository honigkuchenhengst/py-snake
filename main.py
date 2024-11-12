import pygame
import time
import heapq

from board import Board
from food import Food
from snake import Snake

print("Wilkommen bei Sssnake!")

board = Board()
snake = Snake()
food = Food(board.SCREEN_WIDTH, board.SCREEN_HEIGHT)
key_pressed = False
snake_speed = 25

pygame.init()
# window
pygame.display.set_caption("Timon und Luca's Sssnake")
screen = pygame.display.set_mode((board.SCREEN_WIDTH, board.SCREEN_HEIGHT))
fps = pygame.time.Clock()

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# A* helper classes and functions
class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def astar_search(snake, food_position):
    open_set = []
    closed_set = set()
    start = tuple(snake.snake_position)
    goal = tuple(food_position)

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.position == goal:
            # Path found, reconstruct path directions
            path = []
            while current_node.parent:
                dx = current_node.position[0] - current_node.parent.position[0]
                dy = current_node.position[1] - current_node.parent.position[1]
                if dx == 10:
                    path.append('R')
                elif dx == -10:
                    path.append('L')
                elif dy == 10:
                    path.append('D')
                elif dy == -10:
                    path.append('U')
                current_node = current_node.parent
            return path[::-1]  # Reverse path to start from snake's head

        closed_set.add(current_node.position)

        for dx, dy in [(-10, 0), (10, 0), (0, -10), (0, 10)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            # Check if the neighbor is within the screen bounds and not part of the snake's body
            if (0 <= neighbor_pos[0] < board.SCREEN_WIDTH and
                    0 <= neighbor_pos[1] < board.SCREEN_HEIGHT and
                    neighbor_pos not in closed_set and
                    neighbor_pos not in snake.snake_body):

                cost = current_node.cost + 1
                heuristic_val = heuristic(neighbor_pos, goal)
                new_node = Node(neighbor_pos, cost, heuristic_val)
                new_node.parent = current_node

                existing_node = next((node for node in open_set if node.position == neighbor_pos), None)
                if existing_node and existing_node.cost <= cost:
                    continue

                heapq.heappush(open_set, new_node)

    return None  # No path found


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(board.score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render("Dein Score ist : " + str(board.score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (board.SCREEN_WIDTH / 2, board.SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# game loop
while True:
    path = astar_search(snake, food.food_position) or []  # Calculate path each loop
    path_index = 0

    while path_index < len(path):
        # Move snake along the calculated path
        if path[path_index] == 'U':
            snake.snake_position[1] -= 10
        elif path[path_index] == 'D':
            snake.snake_position[1] += 10
        elif path[path_index] == 'L':
            snake.snake_position[0] -= 10
        elif path[path_index] == 'R':
            snake.snake_position[0] += 10

        path_index += 1

        # Check Game Over conditions
        if (snake.snake_position[0] < 0 or snake.snake_position[0] >= board.SCREEN_WIDTH or
                snake.snake_position[1] < 0 or snake.snake_position[1] >= board.SCREEN_HEIGHT or
                snake.snake_position in snake.snake_body[1:]):
            game_over()

        # Snake body growing mechanism
        snake.snake_body.insert(0, list(snake.snake_position))
        if snake.snake_position == food.food_position:
            board.score += 10
            food.food_spawn = False
        else:
            snake.snake_body.pop()

        if not food.food_spawn:
            food.spawn_food()

        # Draw everything
        screen.fill(black)
        for pos in snake.snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, white, pygame.Rect(food.food_position[0], food.food_position[1], 10, 10))
        show_score(1, white, "times new roman", 20)
        pygame.display.update()
        fps.tick(snake_speed)
