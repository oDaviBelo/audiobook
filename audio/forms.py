from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired


class Transform(FlaskForm):
    txt = TextAreaField("Text to Speech (max:200 char)",validators=[DataRequired()])
    send = SubmitField('Transform')
    