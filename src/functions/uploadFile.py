from tkinter import filedialog
import tkinter
from firebase_admin import firestore
from oauth2client.client import Error
from pyrebase.pyrebase import Database, Storage
from functions.getUserInfo import getUserInfo

from functions.updateTask import updateTask

def uploadFile(task, storage: Storage, db: Database, updateTamamlananGorevSayisi):
  try:
    root = tkinter.Tk()
    root.withdraw()
    # Prompting the user to choose files to upload.
    filePaths = filedialog.askopenfiles(initialdir='/',  title="Select file(s)")
    if not filePaths:
      print("No File Chosen.")
      return 0

    # Uploading each chosen file to Firebase Storage.
    taskFileUrls = task["TaskFileURLs"].copy()
    for filePath in filePaths:
      file = open(filePath.name, 'r')
      fileName = file.name.split("/")[-1]
      bucket = storage.bucket()
      blob = bucket.blob(str(task["TaskId"]) + '/' + fileName)
      blob.upload_from_filename(filePath.name)
      blob.make_public()
      taskFileUrls.append(blob.public_url)
    
    # Declaring a newTask dict to replace the oldTask.
    newTask = {
      "TaskName": task["TaskName"],
      "TaskDeadline": task["TaskDeadline"],
      "TaskDetails": task["TaskDetails"],
      "TaskId": task["TaskId"],
      "TaskStatus": "Tamamlandı",
      "From" : task["From"],
      "To": task["To"],
      "TaskFileURLs": taskFileUrls,
    }
    
    # Updating the oldTask with the newTask
    updateTask(db, oldTask=task, newTask=newTask, adminUsername=task["From"], devUsername=task["To"])

    # Incrementing the completedTaskAmounts for both the developer and the administrator.
    db.collection("users").document(task["To"]).update({
      "CompletedTaskAmount": firestore.Increment(1),
    })
    db.collection("users").document(task["From"]).update({
      "CompletedTaskAmount": firestore.Increment(1),
    })

    updateTamamlananGorevSayisi(getUserInfo(db, task["To"])["CompletedTaskAmount"])

  except Error as e:
    print("Error occured while uploading file.", e)
    return 0

  return newTask