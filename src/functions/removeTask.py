from firebase_admin import firestore
from pyrebase.pyrebase import Database

# Task = {
#   "TaskName": "nfjksd",
#   "TaskDeadline": "25.01.2022",
#   "TaskDetails": "Urgent",
#   "TaskStatus": "Bekleniyor",
#   "TaskId": "Task5"
#   "From" : "adminUsername",
#   "To": "devUsername",
#   "TaskFileURLs": [],
# }


def removeTask(db: Database, task, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  try:
    documentAdmin.update({
      "Tasks": firestore.ArrayRemove([task])
    })
    documentDev.update({
      "Tasks": firestore.ArrayRemove([task])
    })
  except:
    print("Task not found!")
    return 0

  return 1
    