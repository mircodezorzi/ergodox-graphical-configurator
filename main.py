import sys, platform
sys.path.insert(0, './src/')

from PyQt5.QtWidgets import QApplication
from window          import App

req_modules = ['gi', 'PyQt5']
supported_platforms = ['Linux']

def check_compatibility(req_modules, supported_platforms):
    import importlib, subprocess, platform
    missing_modules = []

    if platform.system() not in supported_platforms:
        raise Exception('platform not compatible: this program only works on linux')

    for module in req_modules:
        if module not in sys.modules:
            missing_modules.append(module)

    if len(missing_modules) > 0:
        x = input('Some required modules are missing, do you want to install them? [Y/n]: ')
        if x.lowercase() == 'y' or x == '':
            if 'Succesfull' not in subprocess.run(['pip', 'install --user' + ' '.join(req_modules)]):
                raise Exception('An error occured while downloading missing modules: aborting')
                return False
        else:
            raise Exception('Program cannot work without missing modules: aborting')
            return False
    return True

if __name__ == '__main__':
    if check_compatibility(req_modules, supported_platforms):
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
