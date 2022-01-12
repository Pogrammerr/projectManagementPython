from firebase_admin import firestore
from pyrebase.pyrebase import Database


def removeUser(db: Database, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  documentAdmin.update({
    "Users": firestore.ArrayRemove([devUsername])
  })
  documentDev.update({
    "Users": firestore.ArrayRemove([adminUsername])
  })