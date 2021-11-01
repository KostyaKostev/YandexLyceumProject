from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
from PlayerClass import Player
from PyQt5.QtGui import QPixmap
from CastleClass import Castle, unit, elf, orc


class empty_info(QDialog):
    def __init__(self, parent=None):
        super(empty_info, self).__init__(parent)
        uic.loadUi('empty_design.ui', self)

    def btnClosed(self):
        self.close()


class Castle_info(QDialog):
    def __init__(self, castle, parent=None):
        super(Castle_info, self).__init__(parent)
        info = castle.print_info()
        nation = info[1]
        print(info)
        uic.loadUi('castle_design.ui', self)
        if nation == 'elfs':
            pixmap = QPixmap('elftown.jpg')
            self.label_3.setPixmap(pixmap)
        else:
            pixmap = QPixmap('orctown.jpg')
            self.label_3.setPixmap(pixmap)
        self.label.setText('Замок игрока' + ' ' + str(info[0]))
        self.label_2.setText('aрмия:' + ' ' + str(len(info[2])))
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


class Pole_info(QDialog):
    def __init__(self, parent=None):
        super(Pole_info, self).__init__(parent)
        uic.loadUi('field_design.ui', self)
        pixmap = QPixmap('field.jpg')
        self.label_7.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()
