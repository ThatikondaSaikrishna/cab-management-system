from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField , PasswordField , BooleanField ,IntegerField , TimeField , TextAreaField

from wtforms_components import TimeField

from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError

from app.auth.models import EmpDetails

def id_exists(form,field):
    empid=EmpDetails.query.filter_by(emp_id=field.data).first()
    if empid:
        raise ValidationError('Your details are Already Exists')

class CreateBookForm(FlaskForm):
    emps_id=IntegerField('Enter EmpId',validators=[DataRequired()])
    submit = SubmitField('Create')

class RegistrationForm(FlaskForm):
    empid = IntegerField('EmpId', validators=[DataRequired()])
    name=StringField('Name',validators=[DataRequired(),Length(3,60,message='Between 3 to 15 characters')])
    email=StringField("E-mail",validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    login = TimeField('LogIn', validators=[DataRequired()])
    logout = TimeField('LogOut', validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo('confirm',message='password must match')])
    confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    hno = StringField("H.No/Street", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    pincode = IntegerField("PinCode", validators=[DataRequired()])
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    empid = IntegerField('Emp Id',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit=SubmitField('LogIn')



