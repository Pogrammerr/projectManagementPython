from PyQt5 import QtWidgets
import pyrebase
from config.firebase import getFirebaseConfig
from windows.loginScreen import Ui_MainWindow
from windows.openWindow import openWindow
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

openWindow(Ui_MainWindow)