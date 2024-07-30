import random

class Room:
    def __init__(self, name, description, enemies) -> None:
        self.name = name
        self.description = description
        #what kind of monsters can appear?
        self.possible_enemies = enemies #this will have a list of possible monsters that can appear in a room
        #self.enemies = [] #this is getting weird...
        self.room_arch = [[0]*78 for _ in range(21)]
        self.room_architecture()
        
    def describe_room(self):        
        return {'name':self.name, 'description': self.description}
    
    #def create_enemies(self):
    #    #we will do something better than this in the near future...
    #    for i in self.possible_enemies:
    #        #if random.randint(1,2) == 1: #a coin flip for appearance
    #            if i == 'rat':
    #                self.enemies.append(Enemies('Rat', 2,2, random.randint(2,79),random.randint(2,23),'r'))
    
    def room_architecture(self):
        for i in range(0,21):
            for j in range(0,78): #Hardcoded values, for now it will be ok...
                self.room_arch[i][j]= random.randint(0,1) #for now, 2 values will be ok. 0 = empty, 1 = wall
    
    def draw_room(self):
        pass #will move stuff here later

    #def move_enemies(self):
    #     for i in self.enemies:
    #        move = random.randint(1,4)
    #        if move == 1: 
    #            if i.posx>1 and self.room_arch[i.posy][i.posx-1] in [0]:
    #                i.posx -=1
    #        if move == 2:
    #            if i.posx<79 and self.room_arch[i.posy][i.posx+1] in [0]:
    #                i.posx +=1
    #        if move == 3:
    #            if i.posy>2 and self.room_arch[i.posy-1][i.posx] in [0]:
    #                i.posy -=1
    #        if move == 4:
    #            if i.posy<22 and self.room_arch[i.posy+1][i.posx] in [0]:
    #                i.posy +=1        #Yes, terrible, AGAIN...