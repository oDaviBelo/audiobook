from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class Transform(FlaskForm):
    txt = StringField("Type your text",validators=[DataRequired()])
    send = SubmitField('Send')