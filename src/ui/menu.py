from PyQt5.QtWidgets import QAction
from PyQt5.QtCore    import Qt

def new_action(parent, menu, label, shortcut, tooltip, callback):
    action = QAction(label, parent)
    action.setShortcut(shortcut)
    action.setStatusTip(tooltip)
    action.triggered.connect(callback)
    menu.addAction(action)
