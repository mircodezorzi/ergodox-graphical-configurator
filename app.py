from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
from PyQt5           import QtCore

from json  import loads, dump
from sys   import exit

from window   import Window, KeycapConfigWindow
from button   import Button, Checkbox
from menu     import new_action
from utils    import Rect
from config   import *

class App(Window):

    def __init__(self):
        super().__init__(None, 'ergodox-gui-configurator')

        self.viewing_layer = 0

        self.keys = []

        scale = 4
        offset = 50

        self.read_data('dvorak.json')
        self.read_data()

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

        self.active_layer = 0
        self.ui = []
        Checkbox(self, self.ui, 'LED 1', Rect(500, 500, 70, 50), self.data['layers'][self.active_layer]['leds']['led1'] * 2, self.check_led_button1_state)
        Checkbox(self, self.ui, 'LED 1', Rect(550, 500, 70, 50), self.data['layers'][self.active_layer]['leds']['led2'] * 2, self.check_led_button2_state)
        Checkbox(self, self.ui, 'LED 1', Rect(600, 500, 70, 50), self.data['layers'][self.active_layer]['leds']['led3'] * 2, self.check_led_button3_state)
        #lb = LayerButton(self, 0, 0, self.layers)
        #Button(self, 'write', Rect(742, 560, button_size[0], button_size[1]),
        #       lambda: self.write(), self.ui, '')

        self.show()

    def set_active_layer(self, layer):
        for key in self.keys:
            key.set_label = self.data['layers'][layer]['label']

    def read_data(self, filepath=None):
        if not filepath:
            filepath, _ = QFileDialog.getOpenFileName(
                self,
                'Open file...',
                '',
                'Json Files (*.json);;All Files (*)',
                options=QFileDialog.Options()
                | QFileDialog.DontUseNativeDialog
                )
        with open(filepath) as f:
            self.data = loads(''.join(f.readlines()))

    def write_data(self, filepath=None):
        if not filepath:
            filepath, _ = QFileDialog.getSaveFileName(
                self,
                'Save file as...',
                '',
                'Json Files (*.json);;All Files (*)',
                options=QFileDialog.Options()
                | QFileDialog.DontUseNativeDialogfileName)
        with open(filepath, 'w') as f:
            dump(self.data, f, indent = 4)

    def check_led_button1_state(self, state):
        self.data['layers'][self.active_layer]['leds']['led1'] = state == QtCore.Qt.Checked

    def check_led_button2_state(self, state):
        self.data['layers'][self.active_layer]['leds']['led2'] = state == QtCore.Qt.Checked

    def check_led_button3_state(self, state):
        self.data['layers'][self.active_layer]['leds']['led3'] = state == QtCore.Qt.Checked

    def write(self):
        pass
