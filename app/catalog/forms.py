from flask_wtf import FlaskForm

from wtforms import StringField , SubmitField , IntegerField , FloatField, TimeField

from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError

from wtforms.validators import DataRequired

from wtforms_components import TimeField

from app.catalog.models import EmpDetails


class EditDetailsForm(FlaskForm):
    emp_name=StringField('Name',validators=[DataRequired(),Length(3,60,message='Between 3 to 15 characters')])
    emp_login=TimeField('Login Time',validators=[DataRequired()])
    emp_logout = TimeField('Deviation Time', validators=[DataRequired()])
    submit=SubmitField('Update')


class CreateBookForm(FlaskForm):
    emps_id=IntegerField('Enter EmpId',validators=[DataRequired()])
    submit = SubmitField('Create')