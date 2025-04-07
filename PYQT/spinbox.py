from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLineEdit, QLabel

from PyQt6.QtGui import QIcon

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,250,500,500)
        self.create_spin()
    
    def create_spin(self):
        hbox = QHBoxLayout()
        
        label = QLabel("Laptop Price: ")
        self.lineEdit =  QLineEdit()  
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        
        self.result = QLineEdit()
        
        hbox.addWidget(label) 
        hbox.addWidget(self.lineEdit) 
        hbox.addWidget(self.spinbox) 
        hbox.addWidget(self.result)
        
        self.setLayout(hbox) 
        
    def spin_selected(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            total =self.spinbox.value() * price
            
            self.result.setText(str(total))


app = QApplication(sys.argv)

ui = Window()

ui.show()
sys.exit(app.exec())

