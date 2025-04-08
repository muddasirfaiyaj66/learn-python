

from PyQt6 import QtCore, QtGui, QtWidgets

import mysql.connector as mc
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dbCreate = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbCreate.setFont(font)
        self.dbCreate.setObjectName("dbCreate")
        self.dbCreate.clicked.connect(self.create_database)
        self.horizontalLayout_2.addWidget(self.dbCreate)
        self.dbConnection = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbConnection.setFont(font)
        self.dbConnection.setObjectName("dbConnection")
        self.dbConnection.clicked.connect(self.connect_database)
        self.horizontalLayout_2.addWidget(self.dbConnection)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def create_database(self):
        try:
            myDB= mc.connect(
                host="localhost",
                user="root",
                password=""
                
                
            )
            cursor = myDB.cursor()
            dbName= self.lineEdit.text()
            cursor.execute("CREATE DATABASE {}".format(dbName))
            self.label_2.setText("Database {} created".format(dbName))
        except mc.Error as e:
            self.label_2.setText("Database Creation Failed")
            
    def connect_database(self):
        try:
            myDB= mc.connect(
                host="localhost",
                user="root",
                password="",
                database="pyqt6"
                
                
            )
            
            
            self.label_2.setText("Database Connected")
        except mc.Error as e:
            self.label_2.setText("Database Connection Failed")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database Name:"))
        self.dbCreate.setText(_translate("Form", "Database Creation"))
        self.dbConnection.setText(_translate("Form", "Databbase Connection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())