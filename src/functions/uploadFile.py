from logging import error
from tkinter import filedialog
import tkinter
from firebase_admin import firestore
from oauth2client.client import Error
from pyrebase.pyrebase import Database, Storage

from functions.updateTask import updateTask

def uploadFile(task, storage: Storage, db: Database):
  print(task)
  try:
    root = tkinter.Tk()
    root.withdraw()
    # Prompting the user to choose files to upload.
    filePaths = filedialog.askopenfiles(initialdir='/',  title="Select file(s)")

    # Uploading each chosen file to Firebase Storage.
    for filePath in filePaths:
      file = open(filePath.name, 'r')
      fileName = file.name.split("/")[-1]
      bucket = storage.bucket()
      print(bucket)
      blob = bucket.blob(task["TaskName"] + '/' + fileName)
      blob.upload_from_filename(filePath.name)
      blob.make_public()
      task["TaskFileURLs"].append(blob.public_url)

      print("fileUrl", blob.public_url)
    
    # Declaring a newTask dict to replace the oldTask.
    newTask = {
      "TaskName": task["TaskName"],
      "TaskDeadline": task["TaskDeadline"],
      "TaskDetails": task["TaskDetails"],
      "TaskId": task["TaskId"],
      "TaskStatus": "Tamamlandı",
      "From" : task["From"],
      "To": task["To"],
      "TaskFileURLs": task["TaskFileURLs"],
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

  except Error as e:
    print("Error occured while uploading file.", e)