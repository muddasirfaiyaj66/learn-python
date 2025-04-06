from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt 6 Window")
        self.setWindowIcon(QIcon("logo.png"))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)
        self.setGeometry(500,300,500,500)
        # self.setStyleSheet('background-color:red')
        stylesheet =(
            'background-color:red'
        )
        # self.setStyleSheet(stylesheet)





app = QApplication([])

window = Window()

window.show()
sys.exit(app.exec())