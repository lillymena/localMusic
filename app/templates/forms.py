from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField, BooleanField, DateField, \
    SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import User


class ArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    hometown = StringField('hometown', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('submit')


class EventForm(FlaskForm):
    eventName = StringField('event name:', validators=[DataRequired()])
    date = DateField("date", format="%Y-%m-%d", validators=[DataRequired()])
    venueName = SelectField('venue', coerce=int, validators=[DataRequired()])
    artists = SelectMultipleField('artists', coerce=int, validators=[DataRequired()])
    submit = SubmitField('create new event')


class VenueForm(FlaskForm):
    venueName = StringField('venue name:', validators=[DataRequired()])
    date = DateField("date", format="%Y-%m-%d", validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    tickets = StringField('tickets', validators=[DataRequired()])
    submit = SubmitField('Create New Venue')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')