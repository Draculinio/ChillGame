from character import Character
from room import Room
import curses
from curses import wrapper

def print_player(character,stdscr):
    info = character.char_info()
    stdscr.addstr(24,0,info['name']+' the '+info['creature']+' S:'+str(info['strength'])+' D:'+str(info['defense'])+' G:'+str(info['gold']))

def print_room(room,stdscr):
    desc = room.describe_room()
    stdscr.addstr(0,0, desc['name'])

def print_board(stdscr):
    
    for i in range(80):
        stdscr.addstr(1,i,'-', curses.color_pair(2))
        stdscr.addstr(23,i,'-', curses.color_pair(2))
    for i in range(2,24):
        stdscr.addstr(i,0,'|', curses.color_pair(2))
        stdscr.addstr(i,80,'|', curses.color_pair(2))

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(10,20, 'This is the game I am creating')
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
    #Initial room creator
    room = Room('Inside your house', 'This is your house',['rat'])
    room.create_enemies()
    p.room = room
    stdscr.erase()
                               
                               #######MAIN LOOP#######
    command = ''
    while command != 101:
        stdscr.addstr(p.posy,p.posx,'@',curses.color_pair(1)) #WRITE THE CHARACTER
        #We need to put any enemy that is available in the room
        for i in room.enemies:
            stdscr.addstr(i.posy,i.posx,i.symbol)
        print_player(p, stdscr)
        print_board(stdscr)
        print_room(room,stdscr)
        command = stdscr.getch() #Interesting, this returns an ASCII char...
        stdscr.erase()
        if command == curses.KEY_LEFT: #Interesting, if I want to have arrows I should not convert ascii...
            if p.posx>1:
                p.posx -=1
        if command == curses.KEY_RIGHT:
            if p.posx<79:
                p.posx +=1
        if command == curses.KEY_UP:
            if p.posy>2:
                p.posy -=1
        if command == curses.KEY_DOWN:
            if p.posy<22:
                p.posy +=1        #Yes, terrible...
        #Move enemies
        room.move_enemies()
        

        #if command == 100:
        #    stdscr.addstr(8,0, 'Description: '+p.room.describe_room()['description'])
        #    stdscr.addstr(10,0, 'Enemies: '+p.room.describe_room()['enemies'])
        #if command == 115:
        #    stdscr.addstr(8,0, 'Your stats: STR: '+ str(p.char_info()['strength'])+ ' DEF: '+str(p.char_info()['defense']))
        
wrapper(main)

