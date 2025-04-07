from PyQt6.QtWidgets import QApplication , QMainWindow
from PyQt6.QtGui import QAction, QIcon

import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,250,500,500)

        self.create_menu()
    def create_menu(self):
        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu("File")
        

        newAction  =QAction(QIcon("./PYQT/icons/icons8-plus-48.png"),"New", self)
        newAction.setShortcut("Ctrl+N")
        fileMenu.addAction(newAction)
        
        copyAction  =QAction(QIcon("./PYQT/icons/icons8-copy-48.png"),"Copy", self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)
        
        saveAction  =QAction(QIcon("./PYQT/icons/icons8-save-94.png"),"Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        
        fileMenu.addSeparator()
        
        exitAction  =QAction(QIcon("./PYQT/icons/icons8-exit-48.png"),"Exit", self)
        exitAction.triggered.connect(self.closeWindow)
        fileMenu.addAction(exitAction)
        
    def closeWindow(self):
        self.close()

app = QApplication(sys.argv)

window = UI()
window.show()
sys.exit(app.exec())