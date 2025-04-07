from PyQt6.QtWidgets import QApplication , QWidget , QComboBox, QVBoxLayout, QLabel


import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,250,500,500)
        vbox = QVBoxLayout()
        
        self.combo= QComboBox()
        
        self.combo.addItem("PyQt6")
        self.combo.addItem("PySide2")
        self.combo.addItem("TKinter")
        self.combo.addItem("Kivy")
        self.combo.addItem("wxPython")
        
        self.combo.currentTextChanged.connect(self.select_item)
        vbox.addWidget(self.combo)
        
        self.text= QLabel("Hello")
        vbox.addWidget(self.text)
        self.setLayout(vbox)

    
    def select_item(self):
        text = self.combo.currentText()
        self.text.setText(f"You have selected {text}")

app = QApplication(sys.argv)

window = UI()
window.show()
sys.exit(app.exec())