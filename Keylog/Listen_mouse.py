from pynput.mouse import Listener

def writetofile(x, y):
    print('Current mouse position: ({0}, {1})'.format(x, y))

with Listener(on_move=writetofile) as l:
    l.join()
