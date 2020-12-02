from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ArtistForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    hometown = StringField('hometown', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('submit')

