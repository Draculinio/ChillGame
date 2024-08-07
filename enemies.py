import random

class Enemies:
    def __init__(self, name, strength, defense, life, posx,posy,symbol): 
        self.name = name
        self.strenght = strength
        self.defense = defense
        self.posx = posx
        self.posy = posy
        self.life = life
        self.symbol = symbol
    
    def initial_place(self, room):
        found = False
        while not found:
            self.posx = random.randint(0,77)
            self.posy = random.randint(0,21)
            if room.room_arch[self.posy][self.posx] in [0]:
                found = True
    
    #TODO: the enemies should move every turn.
    def move_enemy(self, room):
        move = random.randint(1,4)
        if move == 1: 
            if self.posx>1 and room.room_arch[self.posy][self.posx-1] in [0]:
                self.posx -=1
        if move == 2:
            if self.posx<78 and room.room_arch[self.posy][self.posx+1] in [0]:
                self.posx +=1
        if move == 3:
            if self.posy>1 and room.room_arch[self.posy-1][self.posx] in [0]:
                self.posy -=1
        if move == 4:
            if self.posy<20 and room.room_arch[self.posy+1][self.posx] in [0]:
                self.posy+=1