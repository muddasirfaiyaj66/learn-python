from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout, QCheckBox, QLabel
from PyQt6.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,500,500)
        self.create_checkbox()
        


    def updateLabel(self):
        value = self.sender()
        if value.isChecked():
            self.label.setText(f"You have selected: {value.text()}")
            
    def create_checkbox(self):
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setFont(QFont("Times New Roman",15))
        self.check1.toggled.connect(self.updateLabel)
        hbox.addWidget(self.check1)
        
        self.check2 = QCheckBox("Java")
        self.check2.setFont(QFont("Times New Roman",15))
        self.check2.toggled.connect(self.updateLabel)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("JavaScript")
        self.check3.setFont(QFont("Times New Roman",15))
        self.check3.toggled.connect(self.updateLabel)
        hbox.addWidget(self.check3)

        self.check4 = QCheckBox("C++")
        self.check4.setFont(QFont("Times New Roman",15))
        self.check4.toggled.connect(self.updateLabel)
        hbox.addWidget(self.check4)

        self.check5 = QCheckBox("C")
        self.check5.setFont(QFont("Times New Roman",15))
        self.check5.toggled.connect(self.updateLabel)
        hbox.addWidget(self.check5)

        vbox = QVBoxLayout()
        self.label = QLabel()
        self.label.setFont(QFont("Times New Roman",12))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

app = QApplication(sys.argv)
ui = Window()
ui.show()

sys.exit(app.exec())




