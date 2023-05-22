import pyautogui as pg
import time

time.sleep(2)

def saving_code(n):
    '''
    Save the ticket code texts previously written in PowerPoint as images.
    To use this function, the text on the upper left corner has to
    be selected first.

    Arguments:
        n:  Ticket number written in the text to be saved
    '''
    pg.press('apps')
    pg.press('down',9)
    pg.press('enter')

    time.sleep(1.5)

    if n >= 100:
        pg.write(f'{n}.png')
    elif n >= 10 and n < 100:
        pg.write(f'0{n}.png')
    elif n < 10:
        pg.write(f'00{n}.png')
     
    pg.press('enter')
    pg.press('tab')


# To save event code ####
# for n in range(150,200):
#     saving_code(n+1)


def make_sheet(n):
    '''
    Import images from /print_sets folder and make a new sheet in PowerPoint with it
    Result in PowerPoint sheet with tickets of the n-th set.

    Arguments:
        n:  The sheet id number
    '''
    pg.hotkey('alt','5','d')

    time.sleep(1.5)
    pg.write(f'set_{n}.png')
    pg.press('enter')

    time.sleep(0.5)
    pg.hotkey('ctrl','m')
    pg.hotkey('ctrl','e')
    pg.press('del')

# To make 50 sheets with tickets
# for n in range(0,50):
#     make_sheet(n+1)