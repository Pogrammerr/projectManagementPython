from firebase_admin import firestore
from pyrebase.pyrebase import Database

from functions.getInvitations import getInvitations


def rejectInvitation(db: Database, invitation):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(invitation["From"])
  documentDev = collectionUsers.document(invitation["To"])

  try:
    documentAdmin.update({
      "Invitations": firestore.ArrayRemove([invitation])
    })
    documentDev.update({
      "Invitations": firestore.ArrayRemove([invitation])
    })
  except Exception as e:
    print("Hata olustu: " + e)

  return len(getInvitations(db, invitation["To"]))