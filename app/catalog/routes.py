from app.catalog import main

from app import db

from app.catalog.models import EmpDetails , EmpIds

from app.auth.models import EmpDetails

from flask_login import login_user , logout_user , login_required , current_user

from flask import render_template,request , flash , redirect , url_for

from flask import render_template

from app.catalog.forms import EditDetailsForm , CreateBookForm

from app.auth.send_email import send_email

from app.auth.send_manager_email import send_manager_email


@main.route('/')
def display_books():
    empdetail = EmpDetails.query.all()
    return render_template('home.html', empdetail=empdetail)

@main.route('/edit/details/<book_id>', methods=['GET','POST'])
@login_required

def edit_details(book_id):
    empdetails = EmpDetails.query.filter_by(emp_id=book_id).first()
    form = EditDetailsForm(obj=empdetails)
    if form.validate_on_submit():
        empdetails.emp_name = form.emp_name.data
        empdetails.emp_login = form.emp_login.data
        empdetails.emp_logout = form.emp_logout.data

        send_email(empdetails.emp_email, empdetails.emp_name)

        send_manager_email(empdetails.emp_logout, empdetails.emp_name, manager_email="bharathrajklp007@gmail.com")
        
        db.session.add(empdetails)
        db.session.commit()
        flash('Details Edited Successfully')
        return redirect(url_for('main.display_books'))
    return render_template('editdetails.html', form=form)
