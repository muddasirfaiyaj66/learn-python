from PyQt6.QtWidgets import QApplication, QWidget , QPushButton, QLabel, QLineEdit

import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,500)
        self.text = QLineEdit(self)
        self.pushBtn = QPushButton("Click ME",self)
        self.pushBtn.setGeometry(0,100,150,50)

        self.label = QLabel(self)
        self.label.setGeometry(200,100,500,50)

        self.pushBtn.clicked.connect(self.showText)
    def showText(self):
        textInput = self.text.text()
        self.label.setText(textInput)




app = QApplication(sys.argv)

ui = UI()
ui.show()

sys.exit(app.exec())