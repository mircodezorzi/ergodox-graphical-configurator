# Mirco De Zorzi - 2018/06/28

from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtCore import pyqtSlot, Qt

from window import ConfigWindow
from utils  import Rect
from config import *

class Button(QWidget):

    def __init__(self, parent, label, rect, callback, group, tooltip = ''):
        super().__init__()

        self.callback = callback
        self.tooltip  = tooltip
        self.parent   = parent
        self.label    = label
        self.rect     = rect
        self.group    = group

        self.group.append(self)

        self.button = QPushButton(label, parent)
        self.button.clicked.connect(self.callback)
        self.button.resize(rect.w, rect.h)
        self.button.move(rect.x, rect.y)
        self.button.setToolTip(tooltip)

class KeycapButton(Button):

    def __init__(self, parent, keyboard, rect, key_id, layers, active_layer):
        super().__init__(
                parent,
                layers[active_layer][1][key_id],
                rect,
                self.open_config_menu,
                keyboard.buttons,
                'open key config')

        self.active_layer = active_layer
        self.parent       = parent
        self.layers       = layers
        self.key_id       = key_id

    def set_active_layer(self, active_layer):
        self.active_layer = active_layer
        self.button.setText(self.layers[self.active_layer][1][self.key_id])

    def open_config_menu(self):
        config_menu = ConfigWindow(self)
        config_menu.show()

class LayerButton:

    def __init__(self, parent, x, y, layers):
        self.ui = []
        self.parent = parent
        self.layers = layers
        for i in range(len(layers)):
            Button(parent, self.layers[i][0], Rect((button_size[0] + 5) * i + 100, 560, button_size[0], button_size[1]), lambda: self.parent.keyboard.set_active_layer(i), self.ui, '')
