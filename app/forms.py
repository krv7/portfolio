from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput, TextArea

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], widget=TextArea())
    description = StringField('Description', validators=[DataRequired()], widget=TextArea())
    content = StringField('Content', widget=TextArea())
    cat = StringField('Cat', widget=TextArea())
    image = StringField('Image', widget=TextArea())
    submit = SubmitField('Create')

class ProjectUpdateForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    title = StringField('Title', validators=[DataRequired()], widget=TextArea())
    description = StringField('Description', validators=[DataRequired()], widget=TextArea())
    content = StringField('Content', widget=TextArea())
    cat = StringField('Cat', widget=TextArea())
    image = StringField('Image', widget=TextArea())
    submit = SubmitField('Update')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], widget=TextArea())
    description = StringField('Description', validators=[DataRequired()], widget=TextArea())
    content = StringField('Content', widget=TextArea())
    cat = StringField('Cat', widget=TextArea())
    image = StringField('Image', widget=TextArea())
    submit = SubmitField('Create')

class BlogUpdateForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    title = StringField('Title', validators=[DataRequired()], widget=TextArea())
    description = StringField('Description', validators=[DataRequired()], widget=TextArea())
    content = StringField('Content', widget=TextArea())
    cat = StringField('Cat', widget=TextArea())
    image = StringField('Image', widget=TextArea())
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')