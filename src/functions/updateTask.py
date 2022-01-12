from firebase_admin import firestore
from pyrebase.pyrebase import Database

# Task = {
#   "TaskName": "nfjksd",
#   "TaskDeadline": "25.01.2022",
#   "TaskDetails": "Urgent",
#   "From" : "adminUsername",
#   "To": "devUsername",
# }

def updateTask(db: Database, oldTask, newTask, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  try:
    documentAdmin.update({
      "Tasks": firestore.ArrayRemove([oldTask])
    })
    documentDev.update({
      "Tasks": firestore.ArrayRemove([oldTask])
    })
  except:
    print("Task not found!")

  documentAdmin.update({
    "Tasks": firestore.ArrayUnion([newTask])
  })
  documentDev.update({
    "Tasks": firestore.ArrayUnion([newTask])
  })