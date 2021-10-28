import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


def generate_map():
    class MyWidget(QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('designvr1.ui', self)
            self.sp = []
            self.o = '⛹'
            self.zm = '⛫-⛫'
            self.g = ''
            self.p = '༉༉༉'
            self.vr = '⌛'
            x = 10
            y = 10
            for i in range(8):
                kt = []
                for j in range(8):
                    self.button = QPushButton(self)
                    self.button.resize(50, 50)
                    self.button.move(x, y)
                    self.plainTextEdit.setDisabled(True)
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

            self.button.clicked.connect(self.button_clicked)

        def button_clicked(self):
            pass

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyWidget()
        ex.show()
        sys.exit(app.exec_())