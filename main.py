import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import uic
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor("yellow"))
        a = random.randint(1, 20) * 2
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())