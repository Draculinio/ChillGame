#At some point, printing stuff and the main loop should not be in the same place...

from room import Room
import curses

class Printer:
    def __init__(self, stdscr): #TODO: want to initialize all here
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.stdscr = stdscr
    def print_room(self, room: Room):
        desc = room.describe_room()
        self.stdscr.addstr(0,0, desc['name'])

        symbols = {0:[' ', 3], 1:['#', 3],2:['@',1], 3:['r',2]} #Don't kill me for this...
        for i in range(0,21):
            for j in range(0,78): #This really looks like yandere simulator...
                    self.stdscr.addstr(i+2,j+2,symbols[room.room_arch[i][j]][0], curses.color_pair(symbols[room.room_arch[i][j]][1]))

    def print_intro(self):
        self.stdscr.addstr(10,20, 'CHILL AND PYTHON')
        self.stdscr.addstr(0,0, 'Python Is God presents...')