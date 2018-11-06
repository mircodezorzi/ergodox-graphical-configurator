from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtCore    import Qt

import gi.repository
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

from utils  import Rect

# from keyboard import Keybroad
# from button   import Button
# moved inside classes to prevent cyclic import

# Window(parent, title, width=1280, height=720)
#
# Simple class to create PyQt5 windows.
# Default window size is 1280x720 and position the center of the screen.
# If another window is passed as the first argument, when showing the child
# window the parent one will temporarily freeze.
#
# Use:
#
# class App(Window):
#   def __init__(self, parent, title):
#       super().__init__(parent, title, modal)
#
# primary   = App(None,    'This is my primary window')
# secondary = App(primary, 'This is my secondary window')
#
# primary.show()

class Window(QMainWindow):

    def __init__(self, parent, title, modal=True, width=1280, height=720):
        if parent == None:
            super().__init__()
        else:
            super().__init__(parent)

        self.parent = parent
        self.title  = title
        self.modal  = modal
        self.width  = width
        self.height = height

        screen = Gdk.Screen.get_default()
        window_x = (screen.get_width() - width) / 2
        window_y = (screen.get_height() - height) / 2

        self.setWindowTitle(self.title)
        if modal:
            self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(window_x, window_y, width, height)

class KeycapConfigWindow(Window):
    def __init__(self, parent, width=800, height=600):
        super().__init__(
            parent,
            'tooltip',
            'window title',
            True,
            width,
            height)

        from button import Button

        self.ui = []
        Button(self, self.ui, 'save', Rect(742, 560, 10, 10),
               lambda: self.hide(), '')
        self.show()

