import random
import logging #first time using this... wish me luck
logging.basicConfig( #TODO: this should be a class
    filename='room_file.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level = logging.DEBUG

)
class Room: #In non random rooms I want to have the hero in some position...
    def __init__(self, room_number=0) -> None:
        self.name = ''
        self.description = ''
        self.room_arch = [[0]*78 for _ in range(21)]
        self.room_number = room_number
        self.load_room()
        
    def describe_room(self):        
        return {'name':self.name, 'description': self.description}

    def random_room_architecture(self):
        for i in range(0,21):
            for j in range(0,78): #Hardcoded values, for now it will be ok...
                self.room_arch[i][j]= random.randint(0,1) #for now, 2 values will be ok. 0 = empty, 1 = wall
    
    def load_room(self):
        row = 0
        with open('./rooms/'+str(self.room_number)+'.room') as f:
            generated = f.readline()
            logging.info(generated)
            self.name = f.readline()
            self.description = f.readline()
            lines = f.readlines()
            if generated[0] == '0':
                for line in lines:
                    if row<22:
                        for i in range(78): #TODO:this is terrible, maybe we can change this later
                            self.room_arch[row][i] = int(line[i])    
                    row+=1
            else:
                self.random_room_architecture()
        
    
    def draw_room(self):
        pass #will move stuff here later
