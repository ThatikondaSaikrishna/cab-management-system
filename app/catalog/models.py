from app import db , bcrypt  # app/__init__.py

from datetime import datetime

class EmpIds(db.Model):
    _tablename__ = 'empids'

    id = db.Column(db.Integer, primary_key=True)
    emps_id = db.Column(db.Integer, nullable=False)

    def __init__(self, emps_id):
        self.emps_id = emps_id

    def __repr__(self):
        return 'EmpIds {}'.format(self.emps_id)


class EmpDetails(db.Model):
    __tablename__ = 'empdetails'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer,unique=True)
    emp_name = db.Column(db.String(60))
    emp_email = db.Column(db.String(60), unique=True, index=True)
    emp_gender = db.Column(db.String(10))
    emp_login = db.Column(db.Time)
    emp_logout = db.Column(db.Time)
    emp_dev = db.Column(db.Time)
    user_password = db.Column(db.String(200))
    confirm_password = db.Column(db.String(200))
    emp_hno = db.Column(db.String(200))
    emp_address = db.Column(db.String(200))
    emp_pincode = db.Column(db.Integer)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    # Relationship
    #emp_id = db.Column(db.Integer, db.ForeignKey('EmpIds.emps_id'))

    def __init__(self, emp_id, emp_name, emp_email, emp_gender, emp_login, emp_logout, emp_dev,user_password,confirm_password,emp_hno,emp_address,emp_pincode):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.emp_gender = emp_gender
        self.emp_login = emp_login
        self.emp_logout = emp_logout
        self.emp_dev = emp_dev
        self.user_password = user_password
        self.confirm_password = confirm_password
        self.emp_hno = emp_hno
        self.emp_address = emp_address
        self.emp_pincode = emp_pincode

    def __repr__(self):
        return '{} by {}'.format(self.emp_id, self.emp_name)