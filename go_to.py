from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout
from PyQt5 import uic

class empty_info(QDialog):
    def __init__(self, parent=None):
        super(empty_info, self).__init__(parent)
        uic.loadUi('empty_design.ui', self)
        self.pushButtom.clicked.connect(self.btnClosed)
        self.go_to_button.clicked.connect(self.go_go)
