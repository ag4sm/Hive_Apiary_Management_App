from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import InputRequired, DataRequired
from datetime import date

class HiveForm(FlaskForm):
    
    hive_name = StringField("Hive Name/ID: ")
    numOfDeeps = StringField("Number of Deeps: ")
    numOfMediums = StringField("Number of Mediums: ")
    numOfShallows = StringField("Number of Shallows: ")
    notes = TextAreaField("Notes: ")
    submit = SubmitField("Submit")

class InspectionForm(FlaskForm):

    hive_name = StringField("Hive Name/ID: ")
    inspect_date = DateField("Inspection Date", default=date.today(), format='%m,%d,%y', validators=[DataRequired(message="You need to enter a valid date")])
    queen = SelectField("Queen Status: ", choices=[('Present-Active'), ('Present-NonActive'), ('Not Present')])
    health = SelectField("General Health: ", choices=[('Poor'), ('Average'), ('Good')])
    temperment = SelectField("Temperment: ", choices=[('Calm'), ('Neutral'), ('Aggressive')])
    notes = TextAreaField("Inspection Notes: ")
    submit = SubmitField("Save Inspection")

class WeatherForm(FlaskForm):

    zip = IntegerField("Zip Code: ")
    submit = SubmitField("Search")
