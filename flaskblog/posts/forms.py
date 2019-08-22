from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content=StringField('Content', validators=[DataRequired(),Length(max=200)])
    submit=SubmitField('Post')