# Mirco De Zorzi - 2018/06/28

from button import KeycapButton
from utils  import Rect
from config import *

class Keyboard:

    def __init__(self, parent, data, active_layer):

        self.data         = data
        self.active_layer = active_layer

        self.buttons = []

        scale = 4
        offset = 10

        for key in data['matrix']:
            KeycapButton(
                parent,
                self,
                Rect(
                    offset + key['x'] * scale,
                    offset + key['y'] * scale,
                    key['w'] * scale,
                    key['h'] * scale),
                key['code'],
                key['layers'],
                self.active_layer)

    def set_active_layer(self, layer):
        for button in self.buttons:
            button.set_active_layer(layer)
