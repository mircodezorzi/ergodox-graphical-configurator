import json

from window   import Window, KeycapConfigWindow
from button   import Button
from utils    import Rect
from config   import *

class App(Window):

    def __init__(self):
        super().__init__(None, 'ergodox-gui-configurator')

        self.import_layers('dvorak_programmer.json')
        self.active_layer = 0


        self.keys = []

        scale = 4
        offset = 10

        for key in self.data['matrix']:
            Button(
                self,
                self.keys,
                key['layers'][0]['label'],
                Rect(
                    offset + key['x'] * scale,
                    offset + key['y'] * scale,
                    key['w'] * scale,
                    key['h'] * scale
                    ),
                lambda: KeycapConfigWindow(self).show()
                )

        #self.ui = []
        #lb = LayerButton(self, 0, 0, self.layers)
        #Button(self, 'write', Rect(742, 560, button_size[0], button_size[1]),
        #       lambda: self.write(), self.ui, '')
        self.show()

    def set_active_layer(self, layer):
        for key in self.keys:
            key.set_label = self.data['layers'][layer]['label']

    def import_layers(self, filepath):
        with open(filepath) as f:
            self.data = json.loads(''.join(f.readlines()))

    def write(self):
        pass
