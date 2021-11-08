from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from UploadFromBD import all_heroes, all_abilities
extra_message = []



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
            self.label.setPixmap(pixmap)
            race = 'раса: эльфы'
        else:
            pixmap = QPixmap('orctown.jpg')
            self.label.setPixmap(pixmap)
            race = 'раса: орки'
        self.label_2.setText(player_town + ' ' + str(info[0]))
        self.label_4.setText(race)
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
        elif error == 'done':
            self.label.setText('вы уже выбрали, кем будете ходить.')
            self.go_to_button.setText('спасибо, а то я забыл')
        elif error == 'really?':
            self.label.setText('Вы делаете что-то неверно, подумайте')
            self.go_to_button.setText('аааа, наверное я уже победил?')
        self.go_to_button.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


class class_info(QDialog):
    def __init__(self, human, parent=None):
        super(class_info, self).__init__(parent)
        info = human.print_info()
        uic.loadUi('class_design.ui', self)
        self.progressBar.setValue(info[4] // info[-1])
        self.power.setText('сила: ' + str(info[3]))
        self.race.setText('раса: ' + str(info[-2]))
        self.type.setText('класс: ' + str(info[-3]))
        cls = info[-3]
        if cls == 'mage':
            pixmap = QPixmap('mage.jpg')
        elif cls == 'warrior':
            pixmap = QPixmap('warrior_image.jpg')
        else:
            pixmap = QPixmap('archer_image.jpg')
        self.label_5.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()

    def go_go(self):
        pass


class attack_info(QDialog):
    def __init__(self, killer, human, parent=None):
        global extra_message
        super(attack_info, self).__init__(parent)
        uic.loadUi('attack_design.ui', self)
        self.human = human
        self.killer = killer
        self.info1 = all_heroes[killer]
        self.clas = self.info1[6]
        self.abilities = []
        self.info2 = all_heroes[human]
        k = 1
        for key in all_abilities.keys():
            if self.clas in all_abilities[key]:
                if k == 1:
                    self.first_ability.setText(key)
                    k += 1
                elif k == 2:
                    self.second_ability.setText(key)
                    k += 1
                else:
                    self.third_ability.setText(key)
                self.abilities.append(all_abilities[key])
        print(self.abilities)
        self.first_ability.clicked.connect(self.f_a)
        self.second_ability.clicked.connect(self.s_a)
        self.third_ability.clicked.connect(self.t_a)
        self.pushButton.clicked.connect(self.btnClosed)

    def f_a(self):
        global extra_message
        if self.clas == 'mage':
            print(1)
            print(all_heroes[self.killer][4])
            all_heroes[self.killer][4] -= self.abilities[0][1]
            print(1)
            all_heroes[self.human][4] -= self.abilities[0][1] // 7 - self.info1[3]
            if all_heroes[self.human][4] <= 0:
                extra_message.append('dead')
            else:
                extra_message.append('')
        elif self.clas == 'warrior':
            all_abilities['УДАААААР!!!'][1] = 0
            extra_message.append('anigilated by one punch')
        else:
            print('удар', self.abilities[0][1] + self.info1[3])
            all_heroes[self.human][4] -= self.abilities[0][1] + self.info1[3]
            if all_heroes[self.human][4] <= 0:
                extra_message.append('dead')
            else:
                extra_message.append('')
        self.close()

    def s_a(self):
        global extra_message
        if self.clas == 'warrior':
            all_heroes[self.human][3] += 15
            extra_message.append('')
        elif self.clas == 'mage':
            all_abilities['разрывная!!!'][1] = 0
            extra_message.append('anigilated')
        elif self.clas == 'archer':
            print(extra_message)
            extra_message.append('swap')
        if all_heroes[self.human][4] <= 0 and extra_message[-1] != 'anigilated':
            extra_message.append('dead')
        elif extra_message[-1] != 'swap':
            extra_message.append('')
        self.close()

    def t_a(self):
        global extra_message
        all_heroes[self.human][4] -= self.abilities[2][1] + self.info1[3]
        if all_heroes[self.human][4] <= 0:
            extra_message.append('dead')
        else:
            extra_message.append('')
        self.close()

    def btnClosed(self):
        self.close()


class game_over(QDialog):
    def __init__(self, winner, parent=None):
        super(game_over, self).__init__(parent)
        uic.loadUi('game_over.ui', self)
        self.label.setText('Игра окончена, победил игрок ' + winner)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()

