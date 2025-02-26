import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисование случайных окружностей")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Добавить окружность", self)
        self.button.setFixedHeight(50)  
        self.button.clicked.connect(self.draw_circle)
        layout.addWidget(self.button)
        self.circles = []

    def draw_circle(self):
        x = random.randint(50, 700)  
        y = random.randint(100, 500)  
        diameter = random.randint(20, 100)  
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  
        self.circles.append((x, y, diameter, color))
        self.update()  

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())