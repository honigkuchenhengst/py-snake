import random as rn

class fruit:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.position=[3,3]


    def spawn_fruit(self, snake):
        empty_space = []
        for i in range(self.length):
            for j in range(self.width):
                empty_space.append([i,j])
        for part in snake:
            empty_space.remove(part)
        if len(empty_space)!=0:
            self.position = empty_space[rn.randint(0, len(empty_space)-1)]
        else:
            self.position=[-1,-1]


    def get_position(self):
        return self.position.copy()
    def set_position(self,position):
        self.position = position

    def copy(self):
        copy = fruit(self.length,self.width)
        copy.position = self.position
        return copy
