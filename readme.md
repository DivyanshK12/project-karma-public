# Description
Flask App that takes image from the user and uploads it to firebase.

Final view can be seen at : https://project-karma-dk.herokuapp.com/

# Initial Steps
* Create a virtual environment using:
``` 
python -m venv venv\
```

* In the environment install dependencies from requirements.txt
```
pip install -r requirements.txt
```

* The vader_lexicon might need to be installed seperately for local development

# Firebase :
Get config files for firebase and use them in
* app/static/js/firebase_init.js
* app/main/utils/firebase_init.py
* app/main/utils/project-firebase.json

Reference structure has been kept here to make setting up easier. 
Note : The .py file imports the .json file as well
Refer official documentation for firebase_sdk for python and using firebase on web.

* Create a migration using the following commands :

* python manage.py db init
* python manage.py db migrate
* python manage.py db upgrade

# Important steps while deploying
* In the migrations/ folder, put an empty .keep file in versions/ if initally there is no migration as the folder would then not be created
* Change secret key in config.py

# TODO
* Update access rules to firestorage to allow only authenticated reads (Updated this, still not sure)
* Add friends feature in relational db
* Make the UI better, as some images are displayed smaller due to rigid flexbox rules
* Update Navbar text to be on the right side (d-flex solution tried-> Failed)

# NAVIGATION 
* Go to 127:0:0:1::5000/register
* Register an account, this takes you to the login page
* At login page enter email id and password
* You arrive at upload_files/, just upload an image, this is where a user would make a new post
* Visiting "/all" would get images/posts