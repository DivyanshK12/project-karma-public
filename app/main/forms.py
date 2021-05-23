#form imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ImageForm(FlaskForm):
    upload = FileField(validators=[FileRequired()])
    caption = StringField(validators=[DataRequired("Please Enter a valid Caption")])

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired("Please enter a valid Username")])
    fullname = StringField(validators=[DataRequired("Please enter valid name")])
    password = PasswordField('Set Password', validators = [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Confirm Password')
    email = StringField(validators=[DataRequired("Please Enter an Email")])#, Email("Please enter a valid email")])
    #Email requires additional module, will do it later

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired("Please enter a valid Username")])
    password = PasswordField('Enter Password', validators = [InputRequired()])

class CommentForm(FlaskForm):
    comment = StringField(validators=[DataRequired("Please enter a valid comment")])