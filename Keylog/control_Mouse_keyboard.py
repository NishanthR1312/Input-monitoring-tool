import time
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

# Control Mouse
def controlMouse():
    mouse = MouseController()
    mouse.position = (100, 704)

# Control Keyboard
def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("I am awesome!!")

# Wait for 3 seconds
time.sleep(3)

# Call the function to control keyboard
controlKeyboard()
