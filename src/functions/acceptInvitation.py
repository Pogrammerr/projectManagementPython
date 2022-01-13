from firebase_admin import firestore
from pyrebase.pyrebase import Database

from functions.getInvitations import getInvitations


def acceptInvitation(db: Database, invitation):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(invitation["From"])
  documentDev = collectionUsers.document(invitation["To"])

  try:
    documentAdmin.update({
      "Users": firestore.ArrayUnion([invitation["To"]])
    })
    documentDev.update({
      "Users": firestore.ArrayUnion([invitation["From"]])
    })

    documentAdmin.update({
      "Invitations": firestore.ArrayRemove([invitation])
    })
    documentDev.update({
      "Invitations": firestore.ArrayRemove([invitation])
    })
  except Exception as e:
    print("Hata olustu: ", e)
    return

  return len(getInvitations(db, invitation["To"]))