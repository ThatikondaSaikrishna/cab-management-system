from flask import render_template,request , flash , redirect , url_for

from flask_login import login_user , logout_user , login_required , current_user

from app.auth.forms import RegistrationForm , LoginForm  , CreateBookForm

from app.auth import authentication as at

from app.auth.send_email import send_email

from app import db

from app.catalog import main

from app.auth.models import EmpDetails , EmpIdscheck

@at.route('/register' , methods=['GET','POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    if form.validate_on_submit():
       EmpDetails.create_user(
           empid=form.empid.data,
           name=form.name.data,
           email=form.email.data,
           gender=form.gender.data,
           login=form.login.data,
           logout=form.logout.data,
           password=form.password.data,
           confirm=form.confirm.data,
           hno=form.hno.data,
           address=form.address.data,
           pincode=form.pincode.data )
       flash('Registration Successful')
       return redirect(url_for('authentication.do_the_login'))

    return render_template('registration.html',form=form,count=0)


@at.route('/login', methods=['GET','POST'])
def do_the_login():

    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))

    form=LoginForm()

    if form.validate_on_submit():
        empdetails=EmpDetails.query.filter_by(emp_id=form.empid.data).first()
        if not empdetails or not empdetails.check_password(form.password.data):
            flash('Invalid Credentials , Please try again')
            return redirect(url_for('authentication.do_the_login'))
        login_user(empdetails,form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html',form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))


@at.route('/details')
@login_required
def details_user():
    empdetails = EmpDetails.query.all()
    if current_user.is_authenticated:
        return render_template('table.html', empdetails=empdetails)

@at.route('/profile')
@login_required
def profile_user():
    if current_user.is_authenticated:
        return render_template('profile.html')

@at.route('/details/<logout>',methods=['GET','POST'])
@login_required
def logout_emps(logout):
    empdetails = EmpDetails.query.all()
    if current_user.is_authenticated:
        return render_template('table.html', empdetails=empdetails,logout=logout)


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


