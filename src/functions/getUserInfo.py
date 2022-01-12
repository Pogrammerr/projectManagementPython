from firebase_admin import firestore
from pyrebase.pyrebase import Database

# User = {
#   CompletedTaskAmount: 0,
#   E-posta: "fdsjkf@gmail.com",
#   Invitations: [{From: admin, To: dev, Details: "Come"}],
#   KullaniciAdi: "fdsjkf",
#   Sifre: "123456",
#   Tasks: [{PLEASE LOOK AT addTask.py FOR TASK TYPE}],
#   Users: [],
#   Yonetici: False
# }


def getUserInfo(db: Database, username):
  return db.collection("users").document(username).get().to_dict()