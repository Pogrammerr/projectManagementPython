from pyrebase.pyrebase import Database


def getLatestTaskId(db: Database):
  return db.collection("tasks").document("latestTaskId").get().to_dict()["id"]