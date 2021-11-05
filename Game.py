import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PlayerClass import Player
from CastleClass import Castle, unit, elfs, orcs
from OpenWindow import empty_info, Castle_info, Pole_info, error_info, class_info
from Errors import Its_time_to_attack_the_castle, wrong_target, wrong_index
turn1 = ['◇', '△', '○']
turn2 = ['◆', '▼', '●']

def game():
    class MyWidget(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('designvr1.ui', self)
            self.sp = []
            self.turn = 1
            self.turns = 1
            self.warrior = '△'
            self.warrior_enemy = '▼'
            self.mage = '◇'
            self.mage_enemy = '◆'
            self.archer = '○'
            self.archer_enemy = '●'
            self.turn1 = ['◇', '△', '○']
            self.turn2 = ['◆', '▼', '●']
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
            self.max_range = 0
            self.max_move = 0
            self.power = 0
            self.health2 = 0
            self.player1 = Player(1)
            self.player2 = Player(2)
            self.log_text = []
            self.current_player = self.player1
            self.done = 0
            self.turner = None
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
                self.sp[l][f2 - 1].setText(self.gr)
                self.sp[l][p - 1].setText(self.p)
                self.sp[l][p2 - 1].setText(self.p)
            self.sp[0][4].setText(self.zm)
            self.sp[1][4].setText(self.warrior_enemy)
            self.sp[1][3].setText(self.mage_enemy)
            self.sp[1][5].setText(self.archer_enemy)
            self.castle1 = Castle('elfs', 1)
            self.castle2 = Castle('orcs', 2)
            self.sp[7][4].setText(self.zm2)
            self.sp[6][4].setText(self.warrior)
            self.sp[6][3].setText(self.mage)
            self.sp[6][5].setText(self.archer)
            self.player1.add_castle(self.castle1)
            self.player2.add_castle(self.castle2)
            info = self.current_player.print_info()
            self.army.setText(str(info[2]))
            self.castles.setText(str(info[1]))
            self.turnk.setText(str(self.turn))
            for u in range(8):
                for h in range(8):
                    if self.sp[u][h].text() == self.gr:
                        self.sp[u][h].setDisabled(True)

            self.button.clicked.connect(self.button_clicked)
            self.log_go.clicked.connect(self.go)

        def button_clicked(self):
            text = self.sender().text()
            if self.done == 0:
                if text == self.p:
                    swindow = Pole_info(self)
                    swindow.exec_()
                elif text == self.zm:
                    swindow = Castle_info(self.castle1)
                    swindow.exec_()
                elif text == self.zm2:
                    swindow = Castle_info(self.castle2)
                    swindow.exec_()
                elif text == self.g or text == '':
                    swindow = empty_info(self)
                    swindow.exec_()
                else:
                    try:
                        if self.turn == 1:
                            current_group = self.turn1
                        else:
                            current_group = self.turn2
                        self.turner = unit(text)
                        self.inform = self.turner.print_info()
                        print(self.inform)
                        if self.inform[0] in current_group:
                            print('yes')
                            self.idx = 0
                            self.idy = 0
                            for x in range(8):
                                for y in range(8):
                                    if self.sp[x][y] == self.sender():
                                        self.idx, self.idy = x, y
                            self.done += 1
                            self.max_range = self.inform[1]
                            self.max_move = self.inform[2]
                            print(type(self.max_move))
                        else:
                            pass
                            #self.turn_info = unit(text)
                            #swindow = class_info(self.turn_info)
                            #swindow.exec_()
                    except wrong_target:
                        swindow = error_info('enemy')
                        swindow.exec_()
            elif self.done == 1:
                try:
                    self.idx2 = 0
                    self.idy2 = 0
                    print(self.idx, self.idy, self.idx2, self.idy2)
                    for q in range(8):
                        for w in range(8):
                            if self.sp[q][w] == self.sender():
                                self.idx2, self.idy2 = q, w
                    print(self.idx, self.idy, self.idx2, self.idy2)
                    if self.idx2 == self.idx and self.idy2 == self.idy:
                        raise wrong_index
                    elif self.idy2 != self.idy and self.idx2 != self.idx:
                        raise wrong_index
                    elif abs(self.idx - self.idx2) > self.max_move:
                        raise wrong_index
                    elif self.sender().text() == self.zm or self.sender().text() == self.zm2:
                        raise Its_time_to_attack_the_castle
                    elif self.sender().text() == self.p:
                        self.sp[self.idx][self.idy].setText('')
                        self.sp[self.idx2][self.idy2].setText(self.p + self.inform[0])
                    elif self.sender().text() == '':
                        print(1)
                        self.sp[self.idx][self.idy].setText('')
                        self.sp[self.idx2][self.idy2].setText(self.inform[0])
                        self.done += 1
                    else:
                        raise wrong_target


                except wrong_target:
                    swindow = error_info('enemy')
                    swindow.exec_()
                    self.done = 0
                except Its_time_to_attack_the_castle:
                    pass
                except wrong_index:
                    self.done = 0
                    swindow = error_info('index')
                    swindow.exec_()

            else:
                if text == self.p:
                    swindow = Pole_info(self)
                    swindow.exec_()
                elif text == self.zm:
                    swindow = Castle_info(self.castle1)
                    swindow.exec_()
                elif text == self.zm2:
                    swindow = Castle_info(self.castle2)
                    swindow.exec_()
                elif text == self.g or text == '':
                    swindow = empty_info(self)
                    swindow.exec_()
                else:
                    if self.turn == 1:
                        current_group = self.turn1
                    else:
                        current_group = self.turn2
                    self.turner = unit(text)
                    self.inform = self.turner.print_info()
                    if self.inform[0] in current_group:
                        swindow = error_info('already_done')
                        swindow.exec_()
                    else:
                        pass

        def go(self):
            self.log.setDisabled(False)
            self.turns += 1
            self.done = 0
            txt = self.info.toPlainText()
            print(31)
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