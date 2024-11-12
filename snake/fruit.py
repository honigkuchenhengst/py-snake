import random as rn

class fruit:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.position=[]
        self.empty_space = []
        self.empty_space_length = 0
        for i in range(length):
            for j in range(width):
                self.empty_space.append([i,j])
                self.empty_space_length += 1
        self.empty_space.remove([1,1])
        self.empty_space.remove([1,2])
        self.empty_space.remove([1,3])
        self.empty_space.remove([1,4])
        self.empty_space.remove([1,5])
        self.empty_space_length -= 5
        self.spawn_fruit()


    def spawn_fruit(self):
        self.position = self.empty_space.pop(rn.randint(0, self.empty_space_length - 1))
        self.empty_space_length -= 1

    def update_space(self,blocked_tile,free_tile):
        self.empty_space.remove(blocked_tile)
        self.empty_space.append(free_tile)

    def get_position(self):
        return self.position.copy()