import sys
sys.path.insert(0, './src/')

from PyQt5.QtWidgets import QApplication
from app             import App
from utils           import check_compatibility

req_modules         = ['gi', 'PyQt5']
supported_platforms = ['Linux']

if __name__ == '__main__':
    if check_compatibility(req_modules, supported_platforms):
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
