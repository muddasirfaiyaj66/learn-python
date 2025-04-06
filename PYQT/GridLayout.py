from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout,QPushButton

import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")
        btn6 = QPushButton("Button 6")
        btn7 = QPushButton("Button 7")
        btn8 = QPushButton("Button 8")
        btn9 = QPushButton("Button 9")

        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3,0,2)

        grid.addWidget(btn4,1,0)
        grid.addWidget(btn5,1,1)
        grid.addWidget(btn6,1,2)

        grid.addWidget(btn7,2,0)
        grid.addWidget(btn8,2,1)
        grid.addWidget(btn9,2,2)

        self.setLayout(grid)
       
       
       

    


app = QApplication(sys.argv)

window = UI()

window.show()
sys.exit(app.exec())