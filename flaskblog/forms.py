from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo
from flaskblog.models import User
'''
FlaskForm is a library to create forms 
validators are inbuilt classes to help put validation checks on i/p
DataRequired field is used when form field cannot be empty
Email to check whether correct email syntax
Length to put a min, max on the form field i/p
EqualTo check whether 2 fields are equal
'''

class RegistrationForm(FlaskForm):
    username = StringField('UserName',
                            validators=[DataRequired(),
                            Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already taken')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('You already have an account with this email. Please log in')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class UpdateAccountForm(FlaskForm):
    username = StringField('UserName',
                            validators=[DataRequired(),
                            Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
   
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('username already taken')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('You already have an account with this email. Please log in')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content=StringField('Content', validators=[DataRequired(),Length(max=200)])
    submit=SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    submit=SubmitField('Request Password Reset')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('You do not have an account, please register')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
        

