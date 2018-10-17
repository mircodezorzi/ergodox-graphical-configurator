# Mirco De Zorzi - 2018/06/28

from button import KeycapButton
from utils  import Rect
from config import *

class Keyboard:

    def __init__(self, parent, layers, active_layer):

        self.layers       = layers
        self.active_layer = active_layer

        self.buttons = []

        # Left side
        # First row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size * 0.5,
                keyboard_position[1],
                keyboard_size * 1.5,
                keyboard_size),
            self.layers[0]['code'],
            self.layers[0]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2,
                keyboard_position[1],
                keyboard_size,
                keyboard_size),
            self.layers[1]['code'],
            self.layers[1]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,
                keyboard_position[1] - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[2]['code'],
            self.layers[2]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,
                keyboard_position[1] - keyboard_stagger[1],
                keyboard_size,
                keyboard_size),
            self.layers[3]['code'],
            self.layers[3]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,
                keyboard_position[1] - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[4]['code'],
            self.layers[4]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,
                keyboard_position[1],
                keyboard_size,
                keyboard_size),
            self.layers[5]['code'],
            self.layers[5]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,
                keyboard_position[1],
                keyboard_size,
                keyboard_size),
            self.layers[6]['code'],
            self.layers[6]['layers'],
            self.active_layer)

        # Second row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size * 0.5,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size * 1.5,
                keyboard_size),
            self.layers[7]['code'],
            self.layers[7]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size),
            self.layers[8]['code'],
            self.layers[8]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[9]['code'],
            self.layers[9]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[1],
                keyboard_size,
                keyboard_size),
            self.layers[10]['code'],
            self.layers[10]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[11]['code'],
            self.layers[11]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size),
            self.layers[12]['code'],
            self.layers[12]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size * 1.5 + keyboard_spacing),
            self.layers[13]['code'],
            self.layers[13]['layers'],
            self.active_layer)

        # Third row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size * 0.5,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size * 1.5,
                keyboard_size),
            self.layers[14]['code'],
            self.layers[14]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size,
                keyboard_size),
            self.layers[15]['code'],
            self.layers[15]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[16]['code'],
            self.layers[16]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size),
            self.layers[17]['code'],
            self.layers[17]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[18]['code'],
            self.layers[18]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size,
                keyboard_size),
            self.layers[19]['code'],
            self.layers[19]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2.5,
                keyboard_size,
                keyboard_size * 1.5 + keyboard_spacing),
            self.layers[26]['code'],
            self.layers[26]['layers'],
            self.active_layer)

        # Fourth row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size * 0.5,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size * 1.5,
                keyboard_size),
            self.layers[20]['code'],
            self.layers[20]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size,
                keyboard_size),
            self.layers[21]['code'],
            self.layers[21]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[22]['code'],
            self.layers[22]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size),
            self.layers[23]['code'],
            self.layers[23]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size),
            self.layers[24]['code'],
            self.layers[24]['layers'],
            self.active_layer)

        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size,
                keyboard_size),
            self.layers[25]['code'],
            self.layers[25]['layers'],
            self.active_layer)

        '''
        # Fifth row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 27, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 28, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 29, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 30, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 31, self.layers, self.active_layer)


        # Left cluster
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 32, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 33, self.layers, self.active_layer)
        # Left Key
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size * 2 + keyboard_spacing), 35, self.layers, self.active_layer)
        # Right Key
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size * 2 + keyboard_spacing), 36, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size), 34, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 7 + keyboard_size * 8,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 6,
                keyboard_size,
                keyboard_size), 37, self.layers, self.active_layer)


        # Right side
        # First row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size + keyboard_distance,
                keyboard_position[1],
                keyboard_size,
                keyboard_size), 38, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                keyboard_position[1],
                keyboard_size,
                keyboard_size), 39, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,
                keyboard_position[1] - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 40, self.layers, 0)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,
                keyboard_position[1] - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 41, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,
                keyboard_position[1] - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 42, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,
                keyboard_position[1],
                keyboard_size,
                keyboard_size), 43, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,
                keyboard_position[1],
                keyboard_size * 1.5,
                keyboard_size), 44, self.layers, self.active_layer)

        # Second row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size * 1.5 + keyboard_spacing), 45, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size), 46, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 47, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 48, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 49, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size,
                keyboard_size), 50, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,
                keyboard_position[1] + keyboard_spacing + keyboard_size,
                keyboard_size * 1.5,
                keyboard_size), 51, self.layers, self.active_layer)

        # Third row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size,
                keyboard_size), 52, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 53, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 54, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 55, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size,
                keyboard_size), 56, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2,
                keyboard_size * 1.5,
                keyboard_size), 57, self.layers, self.active_layer)

        # Fourth row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size,
                keyboard_size), 59, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 60, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 61, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 62, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size,
                keyboard_size), 63, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 3,
                keyboard_size * 1.5,
                keyboard_size), 64, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 2.5,
                keyboard_size,
                keyboard_size * 1.5 + keyboard_spacing), 65, self.layers, self.active_layer)

        # Fith row
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 2 + keyboard_size * 3 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 66, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 3 + keyboard_size * 4 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[1],
                keyboard_size,
                keyboard_size), 67, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 4 + keyboard_size * 5 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4 - keyboard_stagger[0],
                keyboard_size,
                keyboard_size), 68, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 5 + keyboard_size * 6 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 69, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing * 6 + keyboard_size * 7 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 70, self.layers, self.active_layer)


        # Right cluster
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 71, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] - keyboard_spacing + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 4,
                keyboard_size,
                keyboard_size), 70, self.layers, self.active_layer)
        # Left Key
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_size + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size * 2 + keyboard_spacing), 74, self.layers, 0)
        # Right Key
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] + keyboard_spacing + keyboard_size * 2 + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size * 2 + keyboard_spacing), 75, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] - keyboard_spacing + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 5,
                keyboard_size,
                keyboard_size), 72, self.layers, self.active_layer)
        KeycapButton(
            parent,
            self,
            Rect(
                keyboard_position[0] - keyboard_spacing + keyboard_distance,
                keyboard_position[1] + (keyboard_spacing + keyboard_size) * 6,
                keyboard_size,
                keyboard_size), 73, self.layers, self.active_layer)
        '''

    def set_active_layer(self, layer):
        for button in self.buttons:
            button.set_active_layer(layer)
