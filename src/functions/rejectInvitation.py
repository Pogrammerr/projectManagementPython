from firebase_admin import firestore
from pyrebase.pyrebase import Database


def rejectInvitation(db: Database, invitation):
  collectionUsers = db.collection("users")
  documentAdmin = collectionUsers.document(invitation["From"])
  documentDev = collectionUsers.document(invitation["To"])

  documentAdmin.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })
  documentDev.update({
    "Invitations": firestore.ArrayRemove([invitation])
  })