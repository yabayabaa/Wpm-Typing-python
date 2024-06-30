import curses
from curses import wrapper

def start_screen(stdscr):
     # Clear the screen
    stdscr.clear()
    
    # Add a string at position (0, 0)
    stdscr.addstr("Welcome To The Typotest")
    stdscr.addstr("\nPress any keys to begin")
    
    # Refresh the screen to show the changes
    stdscr.refresh()

    # Wait for the user to press a key
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = "Hello World This is a demo of typo\n"
    current_text = []


    while True:

        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key)== 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text)>0:
                current_text.pop()

        else:
            current_text.append(key)



def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

# Initialize the curses application
wrapper(main)
