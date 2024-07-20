from character import Character
from room import Room
import curses
import time

screen = curses.initscr()
screen.addstr(0,20,'---GAMEEEEEE---')
screen.addstr(2,0,'Enter a name: ')
name = screen.getstr().decode('utf-8') #here it is XD
screen.refresh()
creature_type = ''
while creature_type not in ['h','e']:
    screen.addstr(3,0,'What kind of creature do you want to be? (H-Human/E-Elf): ')
    creature_type = screen.getkey().lower()
p = Character(name, creature_type)
p.char_creator()
room = Room('Inside your house', 'This is your house',['rat'])
room.create_enemies()
#For now, let's write here, in the future we will do it better
p.room = room
screen.erase()
screen.addstr(3,0,'Hello,'+p.char_info()['name']+' you are a ' +p.char_info()['creature'])
screen.refresh()
#we need a main loop...
command = ''
while command != 'exit':
    screen.addstr(1,0,p.char_info()['name'])
    screen.addstr(5,0, p.room.describe_room()['name'])
    screen.addstr(20,0, 'Command: ')
    command = screen.getstr().decode('utf-8')
    screen.erase()
    #for now I will write some simple commands here, and then I will move them
    if command.lower() == 'describe':
        screen.addstr(8,0, 'Description: '+p.room.describe_room()['description'])
        screen.addstr(10,0, 'Enemies: '+p.room.describe_room()['enemies'])
    if command.lower() == 'stats':
        screen.addstr(8,0, 'Your stats: STR: '+ str(p.char_info()['strength'])+ ' DEF: '+str(p.char_info()['defense']))
curses.endwin()

print('Thank you for playing!')

