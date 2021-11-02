import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PlayerClass import Player
from CastleClass import Castle, unit, elfs, orcs
from OpenWindow import empty_info, Castle_info, Pole_info

def game():
    class MyWidget(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('designvr1.ui', self)
            self.sp = []
            self.turn = 1
            self.turns = 1
            self.o = '⛹'
            self.zm = '⛫-⛫1'
            self.zm2 = '⛫-⛫2'
            self.g = '༉'
            self.p = '༉༉༉'
            self.vr = '⌛'
            self.gr = '/\ '
            self.t = '---------------'
            self.r = ';'
            self.st = 'сила: '
            self.hl = 'здоровье: '
            self.fp = 'фактор пи: '
            self.sep = '\n'
            self.player1 = Player(1)
            self.player2 = Player(2)
            self.log_text = []
            self.current_player = self.player1
            x = 10
            y = 10
            r_x = 70
            r_y = 60
            for i in range(8):
                kt = []
                for j in range(8):
                    self.button = QPushButton(self)
                    self.button.clicked.connect(self.button_clicked)
                    self.button.resize(50, 50)
                    self.button.move(x, y)
                    self.log.setDisabled(True)
                    x += r_x
                    kt.append(self.button)
                self.sp.append(kt)
                x = 10
                y += r_y
            for l in range(0, len(self.sp), 2):
                f = random.randint(1, 7)
                f2 = random.randint(1, f)
                p = random.randint(1, 7)
                p2 = random.randint(f, 8)
                print(self.sp[l][f - 1])
                self.sp[l][f - 1].setText(self.gr)
                self.sp[l][f].setText(self.g)
                self.sp[l][f - 1].setDisabled(True)
                self.sp[l][f2 - 1].setText(self.gr)
                self.sp[l][f2 - 1].setDisabled(True)
                self.sp[l][p - 1].setText(self.p)
                self.sp[l][p2 - 1].setText(self.p)
            self.sp[0][7].setText(self.zm)
            self.castle1 = Castle('elfs', 1)
            self.castle2 = Castle('orcs', 2)
            self.sp[7][0].setText(self.zm2)
            self.player1.add_castle(self.castle1)
            self.player2.add_castle(self.castle2)
            info = self.current_player.print_info()
            self.army.setText(str(info[2]))
            self.castles.setText(str(info[1]))
            self.turnk.setText(str(self.turn))

            self.button.clicked.connect(self.button_clicked)
            self.log_go.clicked.connect(self.go)

        def button_clicked(self):
            text = self.sender().text()
            if text == self.p:
                swindow = Pole_info(self)
            elif text == self.zm:
                swindow = Castle_info(self.castle1)
            elif text == self.zm2:
                swindow = Castle_info(self.castle2)
            else:
                swindow = empty_info(self)
            swindow.exec_()

        def go(self):
            self.log.setDisabled(False)
            self.turns += 1
            txt = self.info.toPlainText()
            found = False
            if len(txt) != 0:
                for key in elfs.keys():
                    if key == txt:
                        strg, hlth, fctp = elfs[key][0], elfs[key][1], elfs[key][2]
                        self.log.appendPlainText(self.st + strg + self.sep)
                        self.log.appendPlainText(self.hl + hlth + self.sep)
                        self.log.appendPlainText(self.fp + fctp + self.sep)
                        found = True
                if not found:
                    for key in orcs.keys():
                        if key == txt:
                            strg, hlth, fctp = orcs[key][0], orcs[key][1], orcs[key][2]
                            self.log.appendPlainText(self.st + strg + self.sep)
                            self.log.appendPlainText(self.hl + hlth + self.sep)
                            self.log.appendPlainText(self.fp + fctp + self.sep)
                            found = True
                if not found:
                    self.log.appendPlainText('информация не найдена' + self.sep)
                self.log.appendPlainText(self.t + self.sep)
                if self.turn == 1:
                    self.turn = 2
                    self.current_player = self.player2
                    text = 'Ходит 2 игрок;' + self.sep
                    self.log.appendPlainText(text)
                    self.log_text.append(text)
                else:
                    self.current_player = self.player1
                    self.turn = 1
                    text = 'Ходит 1 игрок;' + self.sep
                    self.log.appendPlainText(text)
                    self.log_text.append(text)

            info = self.current_player.print_info()
            self.army.setText(str(info[2]))
            self.castles.setText(str(info[1]))
            self.lcdNumber.display(self.turns)
            self.turnk.setText(str(self.turn))
            self.log.setDisabled(True)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec_())
game()