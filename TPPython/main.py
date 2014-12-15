# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from annuaire_controller import *

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.controller = Annuaire_controller(self)

if  __name__ =='__main__':
    app = QtGui.QApplication(sys.argv)
    annuaire = MyMainWindow()
    annuaire.show()
    sys.exit(app.exec_())
