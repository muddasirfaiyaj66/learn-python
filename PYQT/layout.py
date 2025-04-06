from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout")
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(100,200,500,500)

        vbox = QVBoxLayout()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)





app = QApplication(sys.argv)

window = UI()
window.show()
sys.exit(app.exec())