import sys
import random
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self) 
        self.button.clicked.connect(self.draw_circle) 
        self.circles = []  

    def draw_circle(self):
        x = random.randint(50, 300)
        y = random.randint(50, 300)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()  

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())