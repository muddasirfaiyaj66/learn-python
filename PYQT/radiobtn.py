from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton, QLabel
from PyQt6.QtGui import QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500,200,500,500)

        self.radio_btn()

        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.label = QLabel(self)

        self.label.setGeometry(100,350,300,50)

        vbox.addWidget(self.label)



        self.setLayout(vbox)
    def radio_btn(self):
        self.grpbox = QGroupBox("Choose Programming Language")
        self.grpbox.setFont(QFont("Times New Roman",15))

        hbox = QHBoxLayout()
        
        self.rad1 = QRadioButton("Python")
        self.rad1.setChecked(True)
        self.rad1.setFont(QFont("Times New Roman",13))
        self.rad1.toggled.connect(self.on_selected)

        self.rad2 = QRadioButton("Java")
        self.rad2.setFont(QFont("Times New Roman",13))
        self.rad2.toggled.connect(self.on_selected)

        self.rad3 = QRadioButton("JavaScript")
        self.rad3.setFont(QFont("Times New Roman",13))
        self.rad3.toggled.connect(self.on_selected)

        self.rad4 = QRadioButton("C++")
        self.rad4.setFont(QFont("Times New Roman",13))
        self.rad4.toggled.connect(self.on_selected)

        self.rad5 = QRadioButton("C")
        self.rad5.setFont(QFont("Times New Roman",13))
        self.rad5.toggled.connect(self.on_selected)

        hbox.addWidget(self.rad1)
        hbox.addWidget(self.rad2)
        hbox.addWidget(self.rad3)
        hbox.addWidget(self.rad4)
        hbox.addWidget(self.rad5)
        

        self.grpbox.setLayout(hbox)


    def on_selected(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(f"You have selected: {radio.text()}")


app = QApplication(sys.argv)

ui = Window()
ui.show()

sys.exit(app.exec())