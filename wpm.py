import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    # Clear the screen
    stdscr.clear()
    
    # Add a string at position (0, 0)
    stdscr.addstr(0, 0, "Hello world!",curses.color_pair(1))
    
    # Refresh the screen to show the changes
    stdscr.refresh()
    
    # Wait for the user to press a key
    stdscr.getkey()

# Initialize the curses application
wrapper(main)
