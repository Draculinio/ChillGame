from character import Character
from room import Room
from enemies import Enemies
import curses
from curses import wrapper

def print_player(character,stdscr): #dont even know if this is needed
    stdscr.addstr(24,0,character.char_info())

#TODO: This must be part of room responsability or a printer class.
def print_room(room,stdscr):
    #TODO: All this is terrible because dependencies here are a mess. REFACTOR OR DIE!!!!!
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    desc = room.describe_room()
    stdscr.addstr(0,0, desc['name'])
    symbols = {0:[' ', 3], 1:['#', 3],2:['@',1], 3:['r',2]} #Don't kill me for this...
    for i in range(0,21):
        for j in range(0,78): #This really looks like yandere simulator...
                stdscr.addstr(i+2,j+2,symbols[room.room_arch[i][j]][0], curses.color_pair(symbols[room.room_arch[i][j]][1]))

def print_board(stdscr):
    for i in range(80):
        stdscr.addstr(1,i,'-', curses.color_pair(2))
        stdscr.addstr(23,i,'-', curses.color_pair(2))
    for i in range(2,24):
        stdscr.addstr(i,0,'|', curses.color_pair(2))
        stdscr.addstr(i,80,'|', curses.color_pair(2))

def main(stdscr):
    #Initial room creator
    room = Room('Inside your house', 'This is your house',['rat'])
    enemy = Enemies('Rat',2,2,30,11,11,3)
    enemy.initial_place(room)
    #TODO: Need a logging system...
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(10,20, 'CHILL AND PYTHON')
    stdscr.addstr(0,0, 'Python Is God presents...')
    stdscr.refresh()
    stdscr.getch()
    stdscr.erase()
    #Character creation (Still think this should go elsewhere)
    stdscr.addstr(2,0,'Enter a name: ')
    name = stdscr.getstr(2,15).decode('utf-8')
    name = name.capitalize()
    creature_type = ''
    while creature_type not in ['h','e']:
        stdscr.addstr(3,0,'What kind of creature do you want to be? (H-Human/E-Elf): ')
        creature_type = stdscr.getkey().lower()
    p = Character(name, creature_type)
    p.char_creator()
    stdscr.erase()
                               
                               #######MAIN LOOP#######
    command = ''
    while command != 101:
        #stdscr.addstr(p.posy,p.posx,'@',curses.color_pair(1)) #WRITE THE CHARACTER
        print_player(p, stdscr)
        print_board(stdscr)
        print_room(room,stdscr)
        command = stdscr.getch() #Interesting, this returns an ASCII char...
        stdscr.erase()
        if command == curses.KEY_LEFT: #Interesting, if I want to have arrows I should not convert ascii...
            if p.posx>1:
                if room.room_arch[p.posy][p.posx-1] != 1: #In the future this will depend in lots of codes
                    room.room_arch[p.posy][p.posx] = 0 
                    p.posx -=1
        if command == curses.KEY_RIGHT:
            if p.posx<79:
                if room.room_arch[p.posy][p.posx+1] != 1: 
                    room.room_arch[p.posy][p.posx] = 0
                    p.posx +=1
        if command == curses.KEY_UP:
            if p.posy>2:
                if room.room_arch[p.posy-1][p.posx] != 1:  
                   room.room_arch[p.posy][p.posx] = 0
                   p.posy -=1
        if command == curses.KEY_DOWN:
            if p.posy<22:
                if room.room_arch[p.posy+1][p.posx] != 1:
                    room.room_arch[p.posy][p.posx] = 0 #TERRIBLE AGAIN
                    p.posy +=1        #Yes, terrible...
        room.room_arch[p.posy][p.posx] = 2
        #Move enemies
        #room.move_enemies()
        room.room_arch[enemy.posy][enemy.posx] = 0 #THE MOST HARDCODED THING ON EARTH
        enemy.move_enemy(room)
        room.room_arch[enemy.posy][enemy.posx] = enemy.symbol #Better...

        #if command == 100:
        #    stdscr.addstr(8,0, 'Description: '+p.room.describe_room()['description'])
        #    stdscr.addstr(10,0, 'Enemies: '+p.room.describe_room()['enemies'])
        #if command == 115:
        #    stdscr.addstr(8,0, 'Your stats: STR: '+ str(p.char_info()['strength'])+ ' DEF: '+str(p.char_info()['defense']))
 
wrapper(main)