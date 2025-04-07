from PyQt6.QtWidgets import QApplication, QWidget,QListWidget, QVBoxLayout, QLabel

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        vbox = QVBoxLayout()
        
        self.list_widget = QListWidget()
        
        self.list_widget.insertItem(0, "PyQt6")
        self.list_widget.insertItem(1, "wxPython")
        self.list_widget.insertItem(2, "Kivy")
        self.list_widget.insertItem(3, "TKinter")
        self.list_widget.insertItem(4, "PySide2")
        
        self.list_widget.clicked.connect(self.item_selected)
        
        self.label = QLabel("Hello")
        
        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)
        
        self.setLayout(vbox)
    
    
    def item_selected(self):
        item = self.list_widget.currentItem()
        self.label.setText(f"You have selected : {item.text()}")
        
app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec())
