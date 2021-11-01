import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PlayerClass import Player
from CastleClass import Castle, unit, elf, orc
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
            self.g = ''
            self.p = '༉༉༉'
            self.vr = '⌛'
            self.player1 = Player(1)
            self.player2 = Player(2)
            self.log_text = []
            self.current_player = self.player1
            x = 10
            y = 10
            for i in range(8):
                kt = []
                for j in range(8):
                    self.button = QPushButton(self)
                    self.button.clicked.connect(self.button_clicked)
                    self.button.resize(50, 50)
                    self.button.move(x, y)
                    self.log.setDisabled(True)
                    x += 70
                    kt.append(self.button)
                self.sp.append(kt)
                x = 10
                y += 60
            for l in range(0, len(self.sp), 2):
                f = random.randint(1, 7)
                f2 = random.randint(1, f)
                p = random.randint(1, 7)
                p2 = random.randint(f, 8)
                print(self.sp[l][f - 1])
                self.sp[l][f - 1].setText('/\ ')
                self.sp[l][f].setText('༉')
                self.sp[l][f - 1].setDisabled(True)
                self.sp[l][f2 - 1].setText('/\ ')
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
            if self.turn == 1:
                self.turn = 2
                self.current_player = self.player2
                self.log.setPlainText('Ходит 2 игрок')
            else:
                self.current_player = self.player1
                self.turn = 1
                self.log.setPlainText('Ходит 1 игрок')
            self.turns += 1
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