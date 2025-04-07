from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,250,500,500)
        vbox = QVBoxLayout()
        
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        
        tableWidget.setItem(0,0,QTableWidgetItem("FName"))
        tableWidget.setItem(0,1,QTableWidgetItem("LName"))
        tableWidget.setItem(0,2,QTableWidgetItem("Email"))
        
        tableWidget.setItem(1,0,QTableWidgetItem("Hasan"))
        tableWidget.setItem(1,1,QTableWidgetItem("Afridi"))
        tableWidget.setItem(1,2,QTableWidgetItem("hasanafridi@gmail.com"))
        
        
        tableWidget.setItem(2,0,QTableWidgetItem("John"))
        tableWidget.setItem(2,1,QTableWidgetItem("Smith"))
        tableWidget.setItem(2,2,QTableWidgetItem("johnsmith@gmail.com"))
        
        vbox.addWidget(tableWidget)
        
        self.setLayout(vbox)


app = QApplication(sys.argv)

ui = Window()
ui.show()

sys.exit(app.exec())