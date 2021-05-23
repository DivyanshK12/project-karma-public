import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# As an admin, the app has access to read and write all data, regradless of Security Rules

def add_post(username, filename, caption):
    ref = db.reference(f"{username}/{filename}/")
    post = {"caption":caption, "image":f"{username}/{filename}"}
    ref.set(post)
