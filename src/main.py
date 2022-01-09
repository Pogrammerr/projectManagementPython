from PyQt5 import QtWidgets
import pyrebase
from config.firebase import firebaseConfig
from windows.loginScreen import Ui_MainWindow
from windows.openWindow import openWindow

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

openWindow(Ui_MainWindow)