# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTask.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTaskWindow(object):
    def setupUi(self, NewTaskWindow):
        NewTaskWindow.setObjectName("NewTaskWindow")
        NewTaskWindow.resize(370, 411)
        NewTaskWindow.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(NewTaskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NewTaskLabel = QtWidgets.QLabel(self.centralwidget)
        self.NewTaskLabel.setGeometry(QtCore.QRect(70, 30, 241, 41))
        self.NewTaskLabel.setStyleSheet("font-size: 32px;\n"
"color: rgb(0, 80, 255);")
        self.NewTaskLabel.setObjectName("NewTaskLabel")
        self.TaskNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.TaskNameLabel.setGeometry(QtCore.QRect(80, 90, 51, 21))
        self.TaskNameLabel.setObjectName("TaskNameLabel")
        self.TaskNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TaskNameEdit.setGeometry(QtCore.QRect(140, 90, 151, 21))
        self.TaskNameEdit.setObjectName("TaskNameEdit")
        self.DeadlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.DeadlineLabel.setGeometry(QtCore.QRect(80, 130, 51, 21))
        self.DeadlineLabel.setObjectName("DeadlineLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 130, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.DetailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.DetailsLabel.setGeometry(QtCore.QRect(80, 200, 47, 13))
        self.DetailsLabel.setObjectName("DetailsLabel")
        self.GiveTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.GiveTaskButton.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.GiveTaskButton.setStyleSheet("background-color: rgb(200, 250, 200);\n"
"")
        self.GiveTaskButton.setObjectName("GiveTaskButton")
        self.DetailsEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.DetailsEdit.setGeometry(QtCore.QRect(140, 170, 151, 81))
        self.DetailsEdit.setPlaceholderText("")
        self.DetailsEdit.setObjectName("DetailsEdit")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(80, 290, 51, 21))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.UsernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameEdit.setGeometry(QtCore.QRect(140, 290, 151, 21))
        self.UsernameEdit.setReadOnly(True)
        self.UsernameEdit.setObjectName("UsernameEdit")
        NewTaskWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewTaskWindow)
        self.statusbar.setObjectName("statusbar")
        NewTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(NewTaskWindow)

    def retranslateUi(self, NewTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        NewTaskWindow.setWindowTitle(_translate("NewTaskWindow", "MainWindow"))
        self.NewTaskLabel.setText(_translate("NewTaskWindow", "Yeni Görev Verin"))
        self.TaskNameLabel.setText(_translate("NewTaskWindow", "Görev Adı:"))
        self.DeadlineLabel.setText(_translate("NewTaskWindow", "Bitiş Tarihi:"))
        self.DetailsLabel.setText(_translate("NewTaskWindow", "Açıklama:"))
        self.GiveTaskButton.setText(_translate("NewTaskWindow", "Görevi Ver"))
        self.UsernameLabel.setText(_translate("NewTaskWindow", "Kullanıcı:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTaskWindow = QtWidgets.QMainWindow()
    ui = Ui_NewTaskWindow()
    ui.setupUi(NewTaskWindow)
    NewTaskWindow.show()
    sys.exit(app.exec_())
