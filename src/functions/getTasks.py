from pyrebase.pyrebase import Database


def getTasks(db: Database, username):
  return db.collection("users").document(username).get().to_dict()["Tasks"]