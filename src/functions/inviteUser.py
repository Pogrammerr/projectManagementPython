from firebase_admin import firestore
from pyrebase.pyrebase import Database

from functions.getInvitations import getInvitations


def inviteUser(db: Database, details, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  invitation = {
    "From": adminUsername,
    "To": devUsername,
    "Details": details,
  }
  
  if invitation in getInvitations(db, adminUsername):
    print("Same invitation already exists.")
    return 0

  try:
    documentAdmin.update({
      "Invitations": firestore.ArrayUnion([invitation])
    })
    documentDev.update({
      "Invitations": firestore.ArrayUnion([invitation])
    })
  except Exception as e:
    print("Error occured: ", e)
    return 0

  return 1