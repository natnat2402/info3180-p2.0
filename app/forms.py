from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DecimalField, FileField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect
from flask import Flask

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)

class SearchForm(FlaskForm):

    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    submitbtn = SubmitField("Search")