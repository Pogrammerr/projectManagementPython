from firebase_admin import firestore
from pyrebase.pyrebase import Database


def inviteUser(db: Database, details, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  invitation = {
    "From": adminUsername,
    "To": devUsername,
    "Details": details,
  }

  documentAdmin.update({
    "Invitations": firestore.ArrayUnion([invitation])
  })
  documentDev.update({
    "Invitations": firestore.ArrayUnion([invitation])
  })