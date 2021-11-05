from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PlayerClass import Player
from PyQt5.QtGui import QPixmap
from CastleClass import Castle, unit


class empty_info(QDialog):
    def __init__(self, parent=None):
        super(empty_info, self).__init__(parent)
        uic.loadUi('empty_design.ui', self)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


class Castle_info(QDialog):
    def __init__(self, castle, parent=None):
        elfs = 'elfs'
        player_town = 'Замок игрока'
        army = 'армия:'
        super(Castle_info, self).__init__(parent)
        info = castle.print_info()
        nation = info[1]
        print(info)
        uic.loadUi('castle_design.ui', self)
        if nation == elfs:
            pixmap = QPixmap('elftown.jpg')
            self.label_3.setPixmap(pixmap)
            race = 'раса: эльфы'
        else:
            pixmap = QPixmap('orctown.jpg')
            self.label_3.setPixmap(pixmap)
            race = 'раса: орки'
        self.label.setText(player_town + ' ' + str(info[0]))
        self.label_2.setText(army + ' ' + str(len(info[2])))
        self.label_4.setText(race)
        self.description.clicked.connect(self.describe)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()

    def describe(self):
        pass


class Pole_info(QDialog):
    def __init__(self, parent=None):
        super(Pole_info, self).__init__(parent)
        self.salary = 2
        uic.loadUi('field_design.ui', self)
        pixmap = QPixmap('field.jpg')
        self.label_7.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


class error_info(QDialog):
    def __init__(self, error, parent=None):
        super(error_info, self).__init__(parent)
        uic.loadUi('error_window.ui', self)
        if error == 'index':
            self.label.setText('юнит не может дойти до сюда. даже не пытайся')
        elif error == 'already_done':
            self.label.setText('вы уже совершили ход.')
        self.go_to_button.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


class class_info(QDialog):
    def __init__(self, human, parent=None):
        super(class_info, self).__init__(parent)
        info = human.print_info()
        uic.loadUi('class_design.ui', self)
        self.pushButton.clicked.connect(self.btnClosed)
        self.go_to_button.clicked.connect(self.go_go)

    def btnClosed(self):
        self.close()

    def go_go(self):
        pass
