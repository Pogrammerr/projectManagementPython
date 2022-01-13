from pyrebase.pyrebase import Database


def getUsers(db: Database, username):
  return db.collection("users").document(username).get().to_dict()["Users"]