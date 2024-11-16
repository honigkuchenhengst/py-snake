import random as rn

class Food:
    def __init__(self, width, height):
        self.food_position = []
        self.food_spawn = False
        self.empty_space = []
        for i in range((int)(width/10)):
            for j in range((int)(height/10)):
                self.empty_space.append([i*10, j*10])
        self.empty_space.remove([100, 50])
        self.empty_space.remove([90, 50])
        self.empty_space.remove([80, 50])
        self.empty_space.remove([70, 50])
        self.spawn_food()
    def spawn_food(self):
        print(len(self.empty_space))
        self.food_position = self.empty_space.pop(rn.randint(0, len(self.empty_space) - 1))
        print(self.food_position)
        self.food_spawn = True

    def update_space(self, free_tile, blocked_tile):
        self.empty_space.append(free_tile)
        self.empty_space.remove(blocked_tile)