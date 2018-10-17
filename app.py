import jon

from window   import Window
from button   import Button, LayerButton
from keyboard import Keyboard
from utils    import Rect
from config   import *

class App(Window):

    def __init__(self):
        super().__init__(None, 'ergodox-gui-configurator')
        self.layers = {}
        self.active_layer = '0'

        self.import_layers('default.json')
        self.keyboard = Keyboard(self, self.layers, self.active_layer)

        #self.layers.append(['layer 0', default_dvp_layout])
        #self.export_layers('new.json')
        #self.generate_json('default.json')
        #self.ui = []
        #lb = LayerButton(self, 0, 0, self.layers)
        #Button(self, 'write', Rect(742, 560, button_size[0], button_size[1]),
        #       lambda: self.write(), self.ui, '')
        self.show()


    def generate_json(self, filepath):
        data = []
        for i in range(76):
            key = input("pressa key to assign it to key {}: ".format(i))
            data.append({'code': i, 'layers': {'0':{'key': key ,'label': key}}})

        data = json.dumps(data)
        with open(filepath, 'w') as f:
            f.write(data)

    def import_layers(self, filepath):
        with open(filepath) as f:
            self.layers = json.loads(''.join(f.readlines()))

    def export_layers(self, filepath):
        data = json.dumps(self.layers)

        with open(filepath, 'w') as f:
            f.write(data)

    def write(self):
        pass
