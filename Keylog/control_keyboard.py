import time
from pynput.keyboard import Controller as KeyboardController

# Function to control the keyboard
def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("I am awesome!!")

# Infinite loop to repeat every 3 seconds
while True:
    controlKeyboard()
    time.sleep(3)

