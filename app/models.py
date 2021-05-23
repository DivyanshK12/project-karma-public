from . import db

class User(db.Model):
    __tablename__ = 'userbase'
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    uid_string = db.Column(db.String(256), unique = True, nullable = False)
    username = db.Column(db.String(256), unique = True, nullable = False)
    allposts = db.relationship('Post', backref='user')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    poster_name = db.Column(db.String(256), db.ForeignKey('userbase.username'), nullable = False)
    posted = db.Column(db.DateTime, unique = True, nullable = False)
    post_path =  db.Column(db.String(256), unique = True, nullable = False)

    def toJSON(self):
        return {'id':self.id, 'poster_name':self.poster_name, 'posted':self.posted, 'post_path':self.post_path}

    def __repr__(self):
        return f"ID : {self.id}, User : {self.poster_name}"
