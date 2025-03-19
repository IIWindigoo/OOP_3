from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPen, QPainter
from PyQt6.QtCore import Qt

import sys


class CCircle:
    def __init__(self, x, y, radius=30):
        self.x = x
        self.y = y
        self.radius = radius
        self.selected = False
    
    def contains(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.radius ** 2
    
    def draw(self, painter: QPainter):
        pen = QPen(Qt.GlobalColor.red if self.selected else Qt.GlobalColor.black, 2)
        painter.setPen(pen)
        painter.drawEllipse(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

class Storage:
    def __init__(self):
        self.__data = []
    def add(self, obj):
        self.__data.append(obj)
    def remove(self, obj):
        self.__data.remove(obj)
    def get_all(self):
        return self.__data[:]

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисуем круги")
        self.setGeometry(300, 300, 640, 480)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())