import sys
from PyQt4 import QtGui
import pygame

def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(500, 600)
    w.move(400, 20)
    w.setWindowTitle('Tetris')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()