import random

class Character:
    def __init__(self, name, creature):
        self.name = name
        self.creature = creature #let's start with human or elf.
        self.strength = 0
        self.defense = 0
        self.gold = 0
        self.room = '' #here is a question... do the character need to know where he is or the room should know who is there????
    
    #Here is the question. Should the player generator be here? 
    #The point is, a human will have a different number in strength, magic, defense, agility etc than an elf.
    #The question is if the logic should be here or not. For now, maybe we can create this here and see what happens

    def char_creator(self):
        str_mod = {'h':5, 'e':3}
        def_mod = {'h':4, 'e':3}
        self.strength = random.randint(1,6) + str_mod[self.creature]
        self.defense = random.randint(1,6) + def_mod[self.creature]

    def char_info(self):
        creatures = {'h':'Human', 'e':'Elf'} #maybe this may die.
        return {'name': self.name, 'creature': creatures[self.creature], 'strength': self.strength, 'defense': self.defense}
    
