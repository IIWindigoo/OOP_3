from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPen, QPainter, QMouseEvent, QKeyEvent
from PyQt6.QtCore import Qt, QRectF

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
        painter.drawEllipse(QRectF(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))

class Storage:
    def __init__(self):
        self.__data = []
    def add(self, obj):
        self.__data.append(obj)
    def remove(self, obj):
        self.__data.remove(obj)
    def get_all(self):
        return self.__data[:]
    def select(self, event: QMouseEvent):
        pos = event.position()
        x = pos.x()
        y = pos.y()
        clicked_on_object = False
        for circle in reversed(self.get_all()):
            if circle.contains(x, y):
                if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
                    circle.selected = not circle.selected
                else:
                    for c in self.get_all():
                        c.selected = False
                    # выделение всех пересекающихся кругов
                    # for other in self.get_all():
                    #     if other.contains(x, y):
                    #         other.selected = True
                    circle.selected = True
                clicked_on_object = True
                break
        if not clicked_on_object:
            for c in self.get_all():
                c.selected = False
            self.add(CCircle(x, y))
    def delete_selected(self):
        to_remove = [c for c in self.get_all() if c.selected]
        for c in to_remove:
            self.remove(c)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисуем круги")
        self.setGeometry(300, 300, 640, 480)
        self.storage = Storage()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.show()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.storage.get_all():
            circle.draw(painter)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.storage.select(event)
            self.update()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Backspace:
            self.storage.delete_selected()
            self.update()
    
    def resizeEvent(self, a0):
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())