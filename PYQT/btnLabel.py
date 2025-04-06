from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon , QFont

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Btn Label")
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(400,100,500,500)

        self.create_widgets()
    def create_widgets(self):
        btn = QPushButton("Click Me",self)
        # btn.move(100,100)
        btn.setGeometry(200,100,80,30)
        btnStyles ='''

           background-color:white;
           color:black 
        '''
            
           
        
        btn.setStyleSheet(btnStyles)
        btn.setIcon(QIcon('icon1.png'))
        btn.clicked.connect(self.changeLabelText)

        self.label = QLabel("My Label", self)
        # self.label.move(200,130)
        self.label.setGeometry(200,130,150,50)
        self.label.setStyleSheet('color:red ; font:bold')
        self.label.setFont(QFont("Times New Roman",15))
    
    def changeLabelText(self):
        self.label.setText("The text is Changed")
        self.label.setStyleSheet("color:white")

app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())