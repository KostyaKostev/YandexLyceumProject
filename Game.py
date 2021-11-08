import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PlayerClass import Player
from CastleClass import Castle, unit
from OpenWindow import empty_info, Castle_info, Pole_info, error_info, class_info, attack_info, extra_message, game_over
from Errors import Its_time_to_attack_the_castle, wrong_target, wrong_index, boloto, donut, stupid_player
from UploadFromBD import all_abilities
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
            self.g = ''
            self.p = '༉༉༉'
            self.vr = '⌛'
            self.gr = '/\ '
            self.units = {}
            self.t = '---------------'
            self.lr = '---'
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
            self.castle1_hp = 500
            self.castle2_hp = 500
            self.msg1 = 'dead'
            self.msg2 = 'anigilated'
            self.msg3 = 'anigilated by one punch'
            self.msg4 = 'swap'
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
            self.castles.setText('2')
            self.turnk.setText(str(self.turn))
            for u in range(8):
                for h in range(8):
                    if self.sp[u][h].text() == self.gr:
                        self.sp[u][h].setDisabled(True)

            self.button.clicked.connect(self.button_clicked)
            self.log_go.clicked.connect(self.go)

        def button_clicked(self):
            text = self.sender().text()
            if self.turn == 1:
                self.castle_hp = self.castle2_hp
            else:
                self.castle_hp = self.castle1_hp
            if self.done == 0:
                self.text_one = text
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
                        self.current_group = self.turn1
                        self.ntc = self.turn2
                    else:
                        self.current_group = self.turn2
                        self.ntc = self.turn1
                    if text not in self.units.keys():
                        self.turner = unit(text)
                        self.units[text] = self.turner.print_info()
                        self.turner = self.turner.print_info()
                    else:
                        self.turner = self.units[text]
                    self.inform = self.turner
                    if self.inform[0] in self.current_group:
                        self.idx = 0
                        self.idy = 0
                        for x in range(8):
                            for y in range(8):
                                if self.sp[x][y] == self.sender():
                                    self.idx, self.idy = x, y
                        self.done += 1
                        self.max_range = self.inform[1]
                        self.max_move = self.inform[2]
                    else:
                        self.turn_info = unit(text)
                        swindow = class_info(self.turn_info)
                        swindow.exec_()
            elif self.done == 1:
                try:
                    self.idx2 = 0
                    self.idy2 = 0
                    for q in range(8):
                        for w in range(8):
                            if self.sp[q][w] == self.sender():
                                self.idx2, self.idy2 = q, w
                    if self.idx2 == self.idx and self.idy2 == self.idy:
                        raise wrong_index
                    elif self.sender().text() in self.ntc:
                        if abs(self.idx2 - self.idx) <= self.max_range:
                            informa = self.sender().text()
                            if informa not in self.units.keys():
                                hero = unit(informa)
                                self.units[informa] = hero.print_info()
                            else:
                                hero = self.units[informa]
                            link = hero[0]
                            swindow = attack_info(self.text_one, link)
                            swindow.exec_()
                            if extra_message != '':
                                if extra_message[-1] == self.msg1:
                                    self.sp[self.idx2][self.idy2].setText('')
                                    self.log.appendPlainText('Вражеский герой повержен!')
                                elif extra_message[-1] == self.msg2:
                                    self.sp[self.idx2][self.idy2].setText('')
                                    self.log.appendPlainText('Вражеский герой жестоко анигилирован...')
                                    self.log.appendPlainText('клетка тоже не выдержала...')
                                    self.sp[self.idx2][self.idy2].setDisabled(True)
                                elif extra_message[-1] == self.msg3:
                                    self.sp[self.idx2][self.idy2].setText('')
                                    self.log.appendPlainText('Это было ожидаемо...')
                                    self.log.appendPlainText('Ничто бы не выдержало...')
                                    self.log.appendPlainText('Стоп! Воин сбежал на субботнюю распродажу!')
                                    self.sp[self.idx][self.idy].setText('')
                                    self.sp[self.idx2][self.idy2].setDisabled(True)
                                elif extra_message == self.msg4:
                                    tc = self.sp[self.idx2][self.idy2].text()
                                    self.sp[self.idx2][self.idy2].setText(tc)
                                    self.sp[self.idx][self.idy].setText(self.text_one)
                                    self.log.appendPlainText('Туша успешно сменена...')

                            self.done += 1
                        else:
                            self.log.appendPlainText('Враг слишком далеко!')
                            self.done = 0
                    elif self.sender().text() == self.zm or self.sender().text() == self.zm2:
                        if abs(self.idx2 - self.idx) <= self.max_range:
                            if self.text_one in self.turn1 and self.sender().text() == self.zm:
                                raise Its_time_to_attack_the_castle
                            elif self.text_one in self.turn2 and self.sender().text() == self.zm2:
                                raise Its_time_to_attack_the_castle
                            else:
                                raise stupid_player
                        else:
                            self.log.appendPlainText('Замок слишком далеко')
                            self.done = 0
                    elif self.idy2 != self.idy and self.idx2 != self.idx:
                        raise wrong_index
                    elif abs(self.idx - self.idx2) > self.max_move:
                        raise wrong_index
                    elif self.sender().text() == self.p:
                        self.sp[self.idx][self.idy].setText('')
                        self.sp[self.idx2][self.idy2].setText(self.p)
                        self.log.appendPlainText(self.lr)
                        self.log.appendPlainText('Юнит игрока завяз в трясине!')
                        self.log.appendPlainText('Юнит выбывает из игры!')
                        self.log.appendPlainText(self.lr)
                        raise boloto
                    elif self.sender().text() == '':
                        can = True
                        self.sp[self.idx][self.idy].setText('')
                        self.sp[self.idx2][self.idy2].setText(self.inform[0])
                        self.log.appendPlainText(self.lr)
                        self.log.appendPlainText('Игрок совершил ход с ' + str(self.idx) + ' ' + str(self.idy))
                        self.log.appendPlainText('На ' +  str(self.idx2) + ' ' + str(self.idy2))
                        self.log.appendPlainText(self.lr)
                        self.done += 1
                    elif self.sender().text() in self.current_group:
                        raise donut
                    else:
                        raise wrong_target
                except stupid_player:
                    swindow = error_info('really?')
                    swindow.exec_()
                    self.done = 0
                except donut:
                    swindow = error_info('done')
                    swindow.exec_()
                except wrong_target:
                    swindow = error_info('enemy')
                    swindow.exec_()
                    self.done = 0
                except Its_time_to_attack_the_castle:
                    if abs(self.idx2 - self.idx) <= self.max_range:
                        self.log.appendPlainText('Игрок атаковал замок!')
                        if self.turn == 1 and self.sender().text() == self.zm1:
                            self.castle1_hp -= 100
                            self.log.appendPlainText('У замка остается еще ' + str(self.castle1_hp) + ' ' + 'жизней')
                        else:
                            self.castle2_hp -= 100
                            self.log.appendPlainText('У замка остается еще ' + str(self.castle2_hp) + ' ' + 'жизней')
                        if self.castle2_hp == 0 or self.castle2_hp == 0:
                            winner = str(self.turn)
                            for o in range(8):
                                for y in range(8):
                                    self.sp[o][y].setDisabled(True)
                            swindow = game_over(winner)
                            swindow.exec_()
                    else:
                        self.log.appendPlainText('Замок слишком далеко!')
                except wrong_index:
                    self.done = 0
                    swindow = error_info('index')
                    swindow.exec_()
                except boloto:
                    pass

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
                        self.turn_info = unit(text)
                        swindow = class_info(self.turn_info)
                        swindow.exec_()

        def go(self):
            self.log.setDisabled(False)
            self.turns += 1
            self.done = 0
            txt = self.info.toPlainText()
            found = False
            if len(txt) != 0:
                for key in all_abilities.keys():
                    if key == txt:
                        info = all_abilities[key]
                        self.log.appendPlainText(str(info))
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
            self.log.appendPlainText('выберите юнита, которым хотите сходить')

            info = self.current_player.print_info()
            self.castles.setText('2')
            self.lcdNumber.display(self.turns)
            self.turnk.setText(str(self.turn))
            self.log.setDisabled(True)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec_())
game()