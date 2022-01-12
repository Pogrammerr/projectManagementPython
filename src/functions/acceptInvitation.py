from firebase_admin import firestore
from pyrebase.pyrebase import Database


def acceptInvitation(db: Database, invitation, adminUsername, devUsername):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(adminUsername)
  documentDev = collectionUsers.document(devUsername)

  documentAdmin.update({
    "Users": firestore.ArrayUnion([devUsername])
  })
  documentDev.update({
    "Users": firestore.ArrayUnion([adminUsername])
  })

  documentAdmin.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })
  documentDev.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })