from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtCore    import Qt, pyqtSlot

#from window import ConfigWindow
#from utils  import Rect
#from config import *

class Button(QWidget):

    def __init__(self, parent, group, label, rect, callback, tooltip = ''):
        super().__init__()

        self.parent   = parent
        self.group    = group
        self.label    = label
        self.rect     = rect
        self.callback = callback
        self.tooltip  = tooltip

        self.group.append(self)

        self.button = QPushButton(label, parent)
        self.button.clicked.connect(self.callback)
        self.button.resize(rect.w, rect.h)
        self.button.move(rect.x, rect.y)
        self.button.setToolTip(tooltip)

'''
class LayerButton:

    def __init__(self, parent, x, y, layers):
        self.ui = []
        self.parent = parent
        self.layers = layers
        for i in range(len(layers)):
            Button(
                parent,
                self.layers[i][0],
                Rect(
                    (button_size[0] + 5) * i + 100,
                    560,
                    button_size[0],
                    button_size[1]),
                lambda: self.parent.keyboard.set_active_layer(i),
                self.ui,
                'Layer {}'.format(i + 1))
'''
