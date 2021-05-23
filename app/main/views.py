from flask import (
    render_template, session, redirect, url_for, flash, request,
    send_from_directory, jsonify)
from . import main
from .forms import ImageForm, RegisterForm, LoginForm, CommentForm
from .. import db as rdb
from ..models import User, Post
from .utils import *
from werkzeug.utils import secure_filename

from .utils.handy import *
from .utils.firebase_init import *
from .utils.firebase_auth import *
from .utils.firebase_store import *
from .utils.firebase_db import *

import os
import requests
import datetime

@main.route('/api/getuser', methods = ["POST"])
def getuser():
    if "uid" in request.args:
        uid = request.args["uid"]
        user = User.query.filter_by(uid_string=uid).first()
        session['username'] = user.username
        session['login'] = True
        return jsonify({"state":"true"})

@main.route('/api/putfile', methods= ["POST"])
def putfile():
    if "caption" in request.args:
        username = session['username']
        caption = request.args['caption']
        raw_filename = random_name_16(username[0])
        to_upload_path = username + "/" + raw_filename
        
        add_post(username, raw_filename, caption)
        
        post = Post(poster_name=username, posted=datetime.datetime.now(), post_path=f"/{username}/{raw_filename}")
        rdb.session.add(post)
        rdb.session.commit()
        return jsonify({"path":to_upload_path})

@main.route('/api/getposts')
def getposts():
    if 'lastviewed' in request.args:
        posts = Post.query.all()[int(request.args["lastviewed"]):]
        posts.reverse() # Inplace reverse to get latest first
        result = jsonify(list(map(Post.toJSON, posts)))
        return result

@main.route('/api/getimage')
def getimage():
    if 'id' in request.args:
        post = Post.query.filter_by(id = request.args['id']).first()
        return jsonify(post.toJSON())

@main.route('/api/karma')
def sentiment():
    if 'text' in request.args:
        text = request.args['text']
        sm = getsentiment(text)
        pos = sm['pos'] + (sm["neu"]/2)
        pos = int(pos*10)
        color = colors[pos]
        return jsonify({"color":color,"sender":session['username']})

@main.before_request
def security():
    exceptions = ['main.login', 'main.register',  'main.getuser', 'main.sentiment', 'main.getimage', 'main.getposts']
    if "login" not in session and (request.endpoint not in exceptions):
        return redirect(url_for('.login'))

@main.route('/')
def landing():
    return redirect(url_for('.home'))

@main.route('/home')
def home():
    return render_template('index.html', username = session['username'])

@main.route('/all')
def all():
    return render_template('all.html', username = session['username'])

@main.route('/<poster_name>/<uid>')
def viewpost(poster_name,uid):
    form = CommentForm()
    post = Post.query.filter_by(id = uid).first()
    return render_template('post.html', post=post, username=session['username'], form=form)

@main.route('/upload_image', methods = ['GET', 'POST'])
def upload():
    form = ImageForm()
    return render_template('upload.html', form=form, username=session['username'])

@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # check if the post request has the file part
        if User.query.filter_by(username=form.username.data).first() is None:
            user = user_setter(email = form.email.data, password = form.password.data,name = form.fullname.data)
            db_user = User(username=form.username.data, uid_string = user.uid)
            rdb.session.add(db_user)
            rdb.session.commit()
        else:
            flash("Username already in use")
        return redirect(url_for(".login"))

    return render_template('register.html', form=form)

@main.route('/login', methods = ['GET', 'POST'])
def login():
    session.pop('login', None)
    form = LoginForm()
    return render_template("login.html", form = form)