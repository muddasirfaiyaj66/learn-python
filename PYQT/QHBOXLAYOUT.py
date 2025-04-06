from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,400,500,500)
        hbox = QHBoxLayout()

        btn1 = QPushButton("Button 1 ")
        btn2 = QPushButton("Button 2 ")
        btn3 = QPushButton("Button 3 ")
        btn4 = QPushButton("Button 4 ")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.setLayout(hbox)
       



app = QApplication(sys.argv)

window = UI()
window.show()

sys.exit(app.exec())