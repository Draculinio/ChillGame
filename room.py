import random
from enemies import Enemies
class Room:
    def __init__(self, name, description, enemies) -> None:
        self.name = name
        self.description = description
        #what kind of monsters can appear?
        self.possible_enemies = enemies #this will have a list of possible monsters that can appear in a room
        self.enemies = [] #this is getting weird...
    def describe_room(self):
        #TODO: show monsters in a better way
        enemies = ''
        for i in self.enemies:
            enemies += i.name+' '
        return {'name':self.name, 'description': self.description, 'enemies': enemies}
    
    def create_enemies(self):
        #we will do something better than this in the near future...
        for i in self.possible_enemies:
            #if random.randint(1,2) == 1: #a coin flip for appearance
                if i == 'rat':
                    self.enemies.append(Enemies('Rat', 2,2, random.randint(2,23),random.randint(2,79),'r'))
    
    def move_enemies(self):
         for i in self.enemies:
            move = random.randint(1,4)
            if move == 1: 
                if i.posx>1:
                    i.posx -=1
            if move == 2:
                if i.posx<79:
                    i.posx +=1
            if move == 3:
                if i.posy>2:
                    i.posy -=1
            if move == 4:
                if i.posy<22:
                    i.posy +=1        #Yes, terrible, AGAIN...