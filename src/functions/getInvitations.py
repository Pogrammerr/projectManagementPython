from firebase_admin import firestore
from pyrebase.pyrebase import Database


def getInvitations(db: Database, username):
  return db.collection("users").document(username).get().to_dict()["Invitations"]