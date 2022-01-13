from firebase_admin import firestore
from pyrebase.pyrebase import Database

from functions.getTasks import getTasks

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

def addTask(db: Database, task, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)
  documentTasks = db.collection("tasks").document("latestTaskId")

  for taskInDev in getTasks(db, devUsername):
    print("AAAAA: ", task ,"BBBBBB", taskInDev)
    if task["TaskName"] == taskInDev["TaskName"]:
      print("Kullanicinin ayni isimde bir gorevi var.")
      return 0

  try:
    documentAdmin.update({
      "Tasks": firestore.ArrayUnion([task])
    })
    documentDev.update({
      "Tasks": firestore.ArrayUnion([task])
    })
    documentTasks.update({
      "id": firestore.Increment(1)
    })
  except Exception as e:
    print("Hata olustu: ", e)
    return 0

  return 1