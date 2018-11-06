from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox
from PyQt5.QtCore    import Qt, pyqtSlot

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
        self.button.clicked.connect(callback)
        self.button.resize(rect.w, rect.h)
        self.button.move(rect.x, rect.y)
        self.button.setToolTip(tooltip)

class Checkbox(QWidget):

    def __init__(self, parent, group, label, rect, state, callback):
        super().__init__()

        self.parent   = parent
        self.group    = group
        self.label    = label
        self.rect     = rect
        self.callback = callback

        self.group.append(self)

        self.checkbox = QCheckBox(label, parent)
        self.checkbox.stateChanged.connect(callback)
        self.checkbox.resize(rect.w, rect.h)
        self.checkbox.move(rect.x, rect.y)
        self.checkbox.setCheckState(state)

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
