import firebase_admin
from firebase_admin import credentials, auth, db, storage

cred = credentials.Certificate('app/main/utils/project-firebase.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'project.appspot.com/',
    'databaseURL': 'https://project.firebaseio.com/'
})

bucket_name = 'project.appspot.com'