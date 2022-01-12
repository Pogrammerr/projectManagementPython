from firebase_admin import firestore
from pyrebase.pyrebase import Database


def rejectInvitation(db: Database, invitation, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  documentAdmin.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })
  documentDev.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })