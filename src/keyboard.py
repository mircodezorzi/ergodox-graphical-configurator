# Mirco De Zorzi - 2018/06/28

from button import KeycapButton
from utils  import Rect
from config import *

class Keyboard:

    def __init__(self, parent, layers, active_layer):
        self.active_layer = active_layer
        self.layers       = layers

        self.buttons = []

        # Left side
        # First row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size * 0.5,\
                                     keyboard_position[1],\
                                     keyboard_size * 1.5,\
                                     keyboard_size), 0, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2,\
                                     keyboard_position[1],\
                                     keyboard_size,\
                                     keyboard_size), 1, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,\
                                     keyboard_position[1] - keyboard_stagger[0],\
                                     keyboard_size,\
                                     keyboard_size), 2, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,\
                                     keyboard_position[1] - keyboard_stagger[1],\
                                     keyboard_size,\
                                     keyboard_size), 3, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,\
                                     keyboard_position[1] - keyboard_stagger[0],\
                                     keyboard_size,\
                                     keyboard_size), 4, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,\
                                     keyboard_position[1],\
                                     keyboard_size,\
                                     keyboard_size), 5, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,\
                                     keyboard_position[1],\
                                     keyboard_size,\
                                     keyboard_size), 6, self.layers, self.active_layer)
        # Second row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size * 0.5,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 7, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size), 8, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 9, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 10, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 11, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size), 12, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size * 1.5 + keyboard_spacing), 13, self.layers, self.active_layer)

        # Third row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size * 0.5,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 14, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size,\
                                    keyboard_size), 15, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 16, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 17, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 18, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size,\
                                    keyboard_size), 19, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2.5,\
                                    keyboard_size,\
                                    keyboard_size * 1.5 + keyboard_spacing), 26, self.layers, self.active_layer)

        # Fourth row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size * 0.5,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 20, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size,\
                                    keyboard_size), 21, self.layers, 0)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 22, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 23, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 24, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size,\
                                    keyboard_size), 25, self.layers, self.active_layer)

        # Fifth row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 27, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 28, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 29, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 30, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 31, self.layers, self.active_layer)


        # Left cluster
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 32, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 33, self.layers, self.active_layer)
        # Left Key
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,\
                                    keyboard_size,\
                                    keyboard_size * 2 + keyboard_spacing), 35, self.layers, self.active_layer)
        # Right Key
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,\
                                    keyboard_size,\
                                    keyboard_size * 2 + keyboard_spacing), 36, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,\
                                    keyboard_size,\
                                    keyboard_size), 34, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 6,\
                                    keyboard_size,\
                                    keyboard_size), 37, self.layers, self.active_layer)


        # Right side
        # First row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size + keyboard_distance,\
                                    keyboard_position[1],\
                                    keyboard_size,\
                                    keyboard_size), 38, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,\
                                    keyboard_position[1],\
                                    keyboard_size,\
                                    keyboard_size), 39, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,\
                                    keyboard_position[1] - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 40, self.layers, 0)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,\
                                    keyboard_position[1] - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 41, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,\
                                    keyboard_position[1] - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 42, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,\
                                    keyboard_position[1],\
                                    keyboard_size,\
                                    keyboard_size), 43, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,\
                                    keyboard_position[1],\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 44, self.layers, self.active_layer)

        # Second row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size * 1.5 + keyboard_spacing), 45, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size), 46, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 47, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 48, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 49, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size,\
                                    keyboard_size), 50, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,\
                                    keyboard_position[1] + keyboard_spacing + keyboard_size,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 51, self.layers, self.active_layer)

        # Third row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size,\
                                    keyboard_size), 52, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 53, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 54, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 55, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size,\
                                    keyboard_size), 56, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 57, self.layers, self.active_layer)

        # Fourth row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size,\
                                    keyboard_size), 59, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 60, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 61, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 62, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size,\
                                    keyboard_size), 63, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,\
                                    keyboard_size * 1.5,\
                                    keyboard_size), 64, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2.5,\
                                    keyboard_size,\
                                    keyboard_size * 1.5 + keyboard_spacing), 65, self.layers, self.active_layer)

        # Fith row
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 66, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[1],\
                                    keyboard_size,\
                                    keyboard_size), 67, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],\
                                    keyboard_size,\
                                    keyboard_size), 68, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 69, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,\
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,\
                                    keyboard_size,\
                                    keyboard_size), 70, self.layers, self.active_layer)


        # Right cluster
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                                    keyboard_size,
                                    keyboard_size), 71, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] - keyboard_spacing + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                                    keyboard_size,
                                    keyboard_size), 70, self.layers, self.active_layer)
        # Left Key
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_size + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                                    keyboard_size,
                                    keyboard_size * 2 + keyboard_spacing), 74, self.layers, 0)
        # Right Key
        KeycapButton(parent, self, Rect(keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                                    keyboard_size,
                                    keyboard_size * 2 + keyboard_spacing), 75, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] - keyboard_spacing + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                                    keyboard_size,
                                    keyboard_size), 72, self.layers, self.active_layer)
        KeycapButton(parent, self, Rect(keyboard_position[0] - keyboard_spacing + keyboard_distance,
                                    keyboard_position[1] + (keyboard_spacing + keyboard_size) * 6,
                                    keyboard_size,
                                    keyboard_size), 73, self.layers, self.active_layer)

    def set_active_layer(self, layer):
        for button in self.buttons:
            button.set_active_layer(layer)
